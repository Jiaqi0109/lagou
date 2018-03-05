# -*- coding: utf-8 -*-

# Scrapy settings for lagou project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lagou'

SPIDER_MODULES = ['lagou.spiders']
NEWSPIDER_MODULE = 'lagou.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 3
COOKIES_ENABLED = True
DOWNLOAD_DELAY = 1


# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16


META = {
    'dont_redirect': True,      # 禁止网页重定向
    'handle_httpstatus_list': [301, 302]        #对哪些异常返回进行处理
}
COOKIES = {
    "user_trace_token" : "20171127161006-f1391cef-ba80-4e7e-9738-b9ef0eb17072",
    "LGUID" : "20171127161054-7d425baa-d34a-11e7-9a81-5254005c3644",
    "_ga" : "GA1.2.803724020.1511770254",
    "JSESSIONID" : "ABAAABAAADEAAFI144553923251B5C25A13E5A63C7AA95C",
    "index_location_city" : "%E5%8C%97%E4%BA%AC",
    "X_HTTP_TOKEN" : "a5020a72d4d08b715a78e4b3a35366c7",
    "ab_test_random_num" : "0",
    "hasDeliver" : "0",
    "showExpriedIndex" : "1",
    "showExpriedCompanyHome" : "1",
    "showExpriedMyPublish" : "1",
    "gate_login_token" : "",
    "Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6" : "1517760205,1520039942",
    "Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6" : "1520077315",
    "LGSID" : "20180305095550-5472db0d-2018-11e8-9c8f-525400f775ce",
    "_putrc" : "8F84CE422EA260D0",
    "login" : "true",
    "unick" : "%E6%9D%8E%E5%98%89%E7%90%A6",
    "hideSliderBanner20180305WithTopBannerC" : "1",
    "gate_login_token" : "8874f588a5a03af28df8faf1b0d2bf050767cd36a0be5b2b",
    "_gat" : "1",
    "TG-TRACK-CODE" : "index_search",
    "SEARCH_ID" : "09153e88d3ae4828b63f834d8eb9216c",
    "LGRID" : "20180305115536-0fddd954-2029-11e8-9cba-525400f775ce"
}

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Host': 'm.lagou.com',
    'Referer': 'https://m.lagou.com/search.html',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'lagou.middlewares.LagouSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'lagou.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'lagou.pipelines.MysqlPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
