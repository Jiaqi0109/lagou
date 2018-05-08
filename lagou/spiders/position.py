# -*- coding: utf-8 -*-
import json
from datetime import datetime
from urllib import parse

import scrapy
from lagou.helper import (deal_position_desc, deal_position_pubtime,
                          deal_position_temptation)
from lagou.items import CompanyItem, PositionItem
from scrapy import FormRequest, Request
from scrapy.conf import settings
from scrapy.exceptions import CloseSpider


class PositionSpider(scrapy.Spider):
    name = 'position'
    allowed_domains = ['m.lagou.com']

    meta = settings['META']
    cookies = settings['COOKIES']
    max_error_num = settings['MAX_ERROR_NUM']
    # referer 问题导致302跳转到验证页面，不能从json页面跳转
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Host': 'm.lagou.com',
        'Referer': 'https://m.lagou.com/home.html',
    }

    def start_requests(self):
        with open('./KEYWORDS/tech.txt', 'r') as f:
            keywords = f.readlines()
        for keyword in keywords:
            # 字符转码(urlEncode)
            keyword = parse.quote(keyword.strip())
            city = parse.quote('全国')
            url = 'https://m.lagou.com/search.json?city=%s&positionName=%s&pageNo=%s&pageSize=15'

            # 获取最大页数
            request = Request(url % (city, keyword, 1), callback=self.max_page_number, errback=self.handle_error)
            request.meta['url'] = url
            request.meta['keyword'] = keyword
            request.meta['city'] = city
            yield request

    def max_page_number(self, response):
        data = json.loads(response.body_as_unicode())
        url = response.meta['url']
        keyword = response.meta['keyword']
        city = response.meta['city']

        total_count = data['content']['data']['page']['totalCount']
        # 处理职位关键字
        # if int(total_count) <= 20000 and int(total_count) >= 200:
        #     with open('./KEYWORDS/category.txt', 'a') as f:
        #         f.write(parse.unquote(keyword) + '\n')
        #     print(parse.unquote(keyword) + ':' + total_count)

        # 判断是否有数据
        if not total_count:
            total_count = 0
        total_count = int(total_count)
        # 若全国职位数据大于5000，拆分城市爬取
        if total_count > 5000 and city == parse.quote('全国'):
            with open('./KEYWORDS/city.txt', 'r') as f:
                cities = f.readlines()
            for city in cities:
                city = parse.quote(city.strip())
                request = Request(url % (city, keyword, 1), cookies=self.cookies, callback=self.max_page_number, errback=self.handle_error)
                request.meta['url'] = url
                request.meta['keyword'] = keyword
                request.meta['city'] = city
                yield request
        else:
            page_number = int(total_count / 15 + 1)
            for i in range(1, page_number + 1):
                request = Request(url % (city, keyword, i), cookies=self.cookies, callback=self.parse_positions, errback=self.handle_error)
                yield request

    def parse_positions(self, response):
        data = json.loads(response.body_as_unicode())
        positions = data['content']['data']['page']['result']
        for p in positions:
            pid = p['positionId']
            positionName = p['positionName']
            city = p['city']
            publish_time = p['createTime']
            publish_time = deal_position_pubtime(publish_time)
            salary = p['salary']
            cid = p['companyId']
            companyName = p['companyName']
            companyFullName = p['companyFullName']

            # 工作详情页，获取job详情和company详情
            detail_url = 'https://m.lagou.com/jobs/%s.html'
            company_url = 'https://m.lagou.com/gongsi/%s.html'
            # 需要设置cookie, headers防止302
            # 需要手动添加headers
            p_reqeust = FormRequest(detail_url % pid, headers=self.headers, meta=self.meta, cookies=self.cookies, callback=self.parse_detail, errback=self.handle_error)
            c_reqeust = FormRequest(company_url % cid, headers=self.headers, meta=self.meta, cookies=self.cookies, callback=self.parse_company, errback=self.handle_error)

            p_reqeust.meta['pid'] = pid
            p_reqeust.meta['city'] = city
            p_reqeust.meta['positionName'] = positionName
            p_reqeust.meta['publish_time'] = publish_time
            p_reqeust.meta['salary'] = salary
            p_reqeust.meta['cid'] = cid
            yield p_reqeust

            c_reqeust.meta['cid'] = cid
            c_reqeust.meta['companyName'] = companyName
            c_reqeust.meta['companyFullName'] = companyFullName
            yield c_reqeust

    def parse_detail(self, response):

        position = PositionItem()
        d_content = response.xpath('//div[@class="detail"]')
        position['pid'] = response.meta['pid']
        position['cid'] = response.meta['cid']
        position['name'] = response.meta['positionName']
        position['city'] = response.meta['city']
        position['publish_time'] = response.meta['publish_time']
        position['salary'] = response.meta['salary']

        position['workyear'] = d_content.xpath('.//span[contains(@class, "workyear")]/span/text()').extract_first().strip()
        position['education'] = d_content.xpath('.//span[contains(@class, "education")]/span/text()').extract_first().strip()
        position['jobnature'] = d_content.xpath('.//span[contains(@class, "jobnature")]/span/text()').extract_first().strip()
        temptation = d_content.xpath('./div[@class="temptation"]/text()').extract_first().strip()
        position['temptation'] = deal_position_temptation(temptation)
        descriptions = response.xpath('//div[@class="positiondesc"]/div/p/text()').extract()
        # detail['description'] = deal_position_desc(descriptions)
        position['description'] = '\n'.join(descriptions)
        position['crawl_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        yield position



    def parse_company(self, response):
        company = CompanyItem()
        c_content = response.xpath('//div[@id="content"]/div[@class="info"]')
        company['cid'] = response.meta['cid']
        company['name'] = response.meta['companyName']
        company['full_name'] = response.meta['companyFullName']

        company['logo'] = c_content.xpath('./img/@src').extract_first()
        if company['logo']:
            company['logo'] = 'https:' + company['logo']
        company['city'] = c_content.xpath('.//p[@class="position"]/span/text()').extract_first().strip()
        desc = c_content.xpath('.//p[@class="desc"]/text()').extract_first()
        desc = desc.split('/')
        company['industry'] = desc[0].strip()
        company['finance_stage'] = desc[1].strip()
        company['scale'] = desc[2].strip()
        company['crawl_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        yield company


    def handle_error(self, response):
        self.max_error_num -= 1
        if self.max_error_num < 0:
            raise CloseSpider()
