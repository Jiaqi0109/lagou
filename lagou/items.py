import scrapy
from scrapy import Field


class CompanyItem(scrapy.Item):
    table_name = 'companies'

    cid = Field()
    name = Field()
    full_name = Field()
    city = Field()
    logo = Field()
    industry = Field()
    finance_stage = Field()
    scale = Field()
    crawl_time = Field()


# class PositionItem(scrapy.Item):
#     table_name = 'positions'

#     pid = Field()
#     cid = Field()
#     # 通过name包含字段所属职业
#     name = Field()
#     city = Field()
#     publish_time = Field()
#     salary = Field()
#     c_name = Field()
#     c_full_name = Field()
#     crawl_time = Field()


class PositionItem(scrapy.Item):
    table_name = 'positions'

    pid = Field()
    cid = Field()
    name = Field()
    city = Field()
    salary = Field()
    workyear = Field()
    education = Field()
    jobnature = Field()
    temptation = Field()
    description = Field()
    publish_time = Field()
    crawl_time = Field()
