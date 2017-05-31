# -*- coding: utf-8 -*-
import scrapy


class LazadaSpider(scrapy.Spider):
    name = 'lazada'
    allowed_domains = ['www.lazada.sg']
    start_urls = ['http://www.lazada.sg/shop-lighting/megaman/?spm=a2o42.category-060000000000.0.0.RQNq72&searchredirect=megaman']

    def parse(self, response):
        for item in response.css('div.c-product-list__item'):
            yield {
                'product_name': item.css('a.c-product-card__name::text').extract_first(),
                'price': item.css('span.c-product-card__price-final::text').extract_first()[4:]
            }
        pass
