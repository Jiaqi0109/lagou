import scrapy
from scrapy import Field


class CompanyItem(scrapy.Item):
    table_name = 'companies'

    cid = Field()
    logo = Field()
    industry = Field()
    scale = Field()
    finance_stage = Field()


class PositionItem(scrapy.Item):
    table_name = 'positions'

    pid = Field()
    cid = Field()
    # 通过name包含字段所属职业
    name = Field()
    city = Field()
    publish_time = Field()
    salary = Field()
    c_name = Field()
    c_full_name = Field()
    crawl_time = Field()


class DetailItem(scrapy.Item):
    table_name = 'details'

    pid = Field()
    workyear = Field()
    education = Field()
    jobnature = Field()
    temptation = Field()
    description = Field()
    crawl_time = Field()
