queries = ['tshirt for men', ‘tshirt for women’]
class AmazonSpider(scrapy.Spider):
    def start_requests(self):
        for query in queries:
            url = 'https://www.amazon.com/s?' + urlencode({'k': query})
            yield scrapy.Request(url=url, callback=self.parse_keyword_response)
