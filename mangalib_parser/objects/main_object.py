from mangalib_parser.data import sites
from mangalib_parser.data.sites import Site
from mangalib_parser.utils import get_pages

class MainObject:

    site = sites.MANGALIB

    def parse(self, url: str, count, site:Site=sites.MANGALIB, **params) -> dict:
        return get_pages(url=url, headers=site.headers, params=params, max_count=count)
    
    def get_url(self) -> str:
        return 'https://' + self.site.domain + '/' + self.model + '/' + (self.id if self.model=='user' else self.slug_url)