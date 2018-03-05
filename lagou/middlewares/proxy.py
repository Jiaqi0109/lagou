import random
import logging
from scrapy.exceptions import NotConfigured
from urllib.request import _parse_proxy

logger = logging.getLogger(__name__)


def _parse(proxy_url):
    proxy_type, user, password, hostport = _parse_proxy(proxy_url)
    return '%s://%s' % (proxy_type, hostport)


class RandomProxyMiddleware(object):
    def __init__(self, settings):
        self.proxies = settings.getlist('PROXIES')
        self.max_failed = settings.getint('PROXY_MAX_FAILED', 1)
        self.stats = {}.fromkeys(map(_parse, self.proxies), 0)

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool('HTTPPROXY_ENABLED'):
            raise NotConfigured
        if not crawler.settings.getlist('PROXIES'):
            raise NotConfigured
        return cls(crawler.settings)

    def process_request(self, request, spider):
        if 'proxy' not in request.meta:
            request.meta['proxy'] = random.choice(self.proxies)

    def process_response(self, request, response, spider):
        cur_proxy = request.meta['proxy']
        if response.status >= 400:
            self.stats[cur_proxy] += 1
            logger.info('%s failed %s' % (cur_proxy, self.stats[cur_proxy]))
        if self.stats[cur_proxy] >= self.max_failed:
            for proxy in self.proxies:
                *_, hostport = _parse_proxy(proxy)
                if cur_proxy.endswith(hostport):
                    self.proxies.remove(proxy)
                    logger.warning(
                        'proxy %s removed from proxies.' % cur_proxy)
                    break
        return response
