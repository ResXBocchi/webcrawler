import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    rules = (Rule(LinkExtractor(deny_domains=('google.com')), callback='parse_page',follow=True),)
    #if the follow parameter is set to True, it will go in every link extracted and extract more link, repeating the cycle. If it is set do False, the crawler will extract only the original url links.
    #we can pass the dony_domains('domain'), in order to avoid some scraping unnecessary domains. 
    #we could pass also the allow=('argument') parameter to LinkExtractor(), in order to only crawl especific urls that has the argument inside it.
    
    def parse_page(self, response):
        yield {'URL': response.url}
    
    #can be used to scrape emails too.
