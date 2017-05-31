# -*- coding: utf-8 -*-
import scrapy


class HomefixSpider(scrapy.Spider):
    name = 'homefix'
    allowed_domains = ['home-fix.com']
    start_urls = ['http://home-fix.com/estore/home-fix-brands/m-s/megaman.html']
    
    def parse(self, response):
        for item in response.css('li.item'):
            yield {
                'product_name': item.css('h2.product-name a::text').extract_first(),
                'price': item.css('div.price-box span.price::text').extract_first()[2:]
            }
        
        next_page = response.css('li a.next::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        pass
