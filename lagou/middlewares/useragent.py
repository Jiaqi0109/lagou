import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

from lagou.settings import USER_AGENT_LIST


class RotateUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        ua = random.choice(USER_AGENT_LIST)
        if ua:
            request.headers.setdefault('User-Agent', ua)
        # print(request.headers, '-------------------XXXXXXXXXXXXXXXXXXXXXXX')
