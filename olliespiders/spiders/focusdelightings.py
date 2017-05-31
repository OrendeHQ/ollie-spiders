# -*- coding: utf-8 -*-
import scrapy


class FocusdelightingsSpider(scrapy.Spider):
    name = 'focusdelightings'
    allowed_domains = ['www.focusdelightings.com.sg']
    start_urls = ['https://www.focusdelightings.com.sg/collections/megaman-led']

    def parse(self, response):
        for item in response.css('.product_image + .info'):
            yield {
                'product_name': item.css('span.title::text').extract_first(),
                'price': item.css('span.price span.money::text').extract_first()[1:]
            }
        
        next_page = response.css('div.paginate span.next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        pass
