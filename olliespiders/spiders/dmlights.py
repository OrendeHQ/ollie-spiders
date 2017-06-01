# -*- coding: utf-8 -*-
import scrapy


class DmlightsSpider(scrapy.Spider):
    name = 'dmlights'
    allowed_domains = ['www.dmlights.com']
    start_urls = ['https://www.dmlights.com/megaman?page=1&viewType=list']

    def parse(self, response):
        for item in response.css('div.dmProductSideActionBlock__list'):
            yield {
                'product_name': item.css('div.productTitle a::text').extract_first(),
                'price': float(item.css('div.productPrice div.text-right::text').extract_first().strip()[4:]) * 1.4
            }
        
        next_page = response.css('a[aria-label="Next"]::attr(href)').extract_first()
        print(next_page)
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        pass
