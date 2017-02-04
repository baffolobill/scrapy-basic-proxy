__author__ = "baffolobill"
__license__ = "MIT"
__version__ = "0.1"


class ProxyMiddleware(object):
    def __init__(self, settings):
        self.proxy = settings.get('HTTP_PROXY')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_request(self, request, spider):
        # Don't overwrite with a random one (server-side state for IP)
        if 'proxy' in request.meta:
            if request.meta["exception"] is False:
                return
        request.meta["exception"] = False
        request.meta['proxy'] = self.proxy

