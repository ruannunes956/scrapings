import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'q'

    def start_requests(self):
    
        url = 'https://quotes.toscrape.com/'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
    
        blocos = response.xpath('//div[@class="quote"]')
        for bloco in blocos:
            texto = bloco.xpath('./span[@class="text"]/text()').get()
            author = bloco.xpath('.//small/text()').get()
            tags = bloco.xpath('.//a[@class="tag"]/text()').getall()
            yield {
                'texto': texto,
                'author': author,
                'tags': tags
            }
        
        proxima_pagina = response.xpath('//li[@class="next"]/a/@href').get()
        if proxima_pagina:
            next_page_url = response.urljoin(proxima_pagina)
            yield scrapy.Request(next_page_url, callback=self.parse)


