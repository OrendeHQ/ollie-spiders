# -*- coding: utf-8 -*-
import scrapy


class ThreecubesSpider(scrapy.Spider):
    name = 'threecubes'
    start_urls = ['https://www.threecubes.com.sg/search?page=1&q=megaman&type=product/']

    def parse(self, response):
        for item in response.css('div.grid-item.search-result'):
            product_name = item.css('.product-grid-item p::text').extract_first()
            price = item.css('.product-grid-item span.money::text').extract_first()
            if (product_name is not None) and (price is not None):
                yield {
                    'product_name': product_name,
                    'price': price[1:-4]
                }
        
        next_page = response.css('ul.pagination-custom li:last-child a::attr(href)').extract_first()
        print(next_page)
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        pass
