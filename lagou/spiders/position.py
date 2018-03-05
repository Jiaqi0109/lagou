# -*- coding: utf-8 -*-
import json
from datetime import datetime
from urllib import parse

import scrapy
from scrapy import Request
from scrapy import FormRequest

from scrapy.conf import settings

from lagou.items import PositionItem, CompanyItem, DetailItem
from lagou.helper import deal_position_desc, deal_position_temptation


class PositionSpider(scrapy.Spider):
    name = 'position'
    allowed_domains = ['m.lagou.com']


    meta = settings['META']
    cookies = settings['COOKIES']
    # referer 问题导致302跳转到验证页面，不能从json页面跳转
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1',
        'Host': 'm.lagou.com',
        'Referer': 'https://m.lagou.com/search.html',
    }


    def start_requests(self):
        with open('./KEYWORDS/category.txt', 'r') as f:
            keywords = f.readlines()
        for keyword in keywords:
            # 字符转码(urlEncode)
            keyword = parse.quote(keyword.strip())
            city = parse.quote('全国')
            url = 'https://m.lagou.com/search.json?city=%s&positionName=%s&pageNo=%s&pageSize=15'

            # 获取最大页数
            request = Request(url % (city, keyword, 1), callback=self.max_page_number)
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
                request = Request(url % (city, keyword, 1), cookies=self.cookies, callback=self.max_page_number)
                request.meta['url'] = url
                request.meta['keyword'] = keyword
                request.meta['city'] = city
                yield request
        else:
            page_number = int(total_count / 15 + 1)
            for i in range(1, page_number + 1):
                request = Request(url % (city, keyword, i), cookies=self.cookies, callback=self.parse_positions)
                yield request


    def parse_positions(self, response):
        data = json.loads(response.body_as_unicode())
        positions = data['content']['data']['page']['result']
        for p in positions:
            position = PositionItem()
            pid = p['positionId']
            position['pid'] = pid
            position['name'] = p['positionName']
            position['city'] = p['city']
            position['publish_time'] = p['createTime']
            position['salary'] = p['salary']
            cid = p['companyId']
            position['cid'] = cid
            position['c_name'] = p['companyName']
            position['c_full_name'] = p['companyFullName']
            position['crawl_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            yield position


            # 工作详情页，获取job详情和company详情
            detail_url = 'https://m.lagou.com/jobs/%s.html'
            # 需要设置cookie, headers防止302
            # 需要手动添加headers
            reqeust = FormRequest(detail_url % pid, headers=self.headers, meta=self.meta, cookies=self.cookies, callback=self.parse_detail)
            reqeust.meta['cid'] = cid
            reqeust.meta['pid'] = pid
            yield reqeust


    def parse_detail(self, response):

        detail = DetailItem()
        d_content = response.xpath('//div[@class="detail"]')
        detail['pid'] = response.meta['pid']
        detail['workyear'] = d_content.xpath('.//span[contains(@class, "workyear")]/span/text()').extract_first().strip()
        detail['education'] = d_content.xpath('.//span[contains(@class, "education")]/span/text()').extract_first().strip()
        detail['jobnature'] = d_content.xpath('.//span[contains(@class, "jobnature")]/span/text()').extract_first().strip()
        temptation = d_content.xpath('./div[@class="temptation"]/text()').extract_first().strip()
        detail['temptation'] = deal_position_temptation(temptation)
        descriptions = response.xpath('//div[@class="positiondesc"]/div/p/text()').extract()
        detail['description'] = deal_position_desc(descriptions)
        detail['crawl_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        yield detail


        company = CompanyItem()
        c_content = response.xpath('//div[contains(@class, "company")]')
        company['cid'] = response.meta['cid']
        company['logo'] = c_content.xpath('./img/@src').extract_first()
        if company['logo']:
            company['logo'] = 'https:' + company['logo']
        desc = c_content.xpath('./div[@class="desc"]//p[@class="info"]/text()').extract_first()
        desc = desc.split('/')
        company['industry'] = desc[0].strip()
        company['scale'] = desc[2].strip()
        company['finance_stage'] = desc[1].strip()
        yield company
