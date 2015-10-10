__author__ = 'brendan'
import scrapy
from carss.items import CarssItem
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import re

USER_AGENT = "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)"
REQUEST_HEADERS = {'User-agent': USER_AGENT,}


class CarSpider(scrapy.Spider):
    max_price = 1000

    name = 'car'
    allowed_domains = ['gumtree.co.uk', 'gumtree.com']
    start_urls = [
        'https://www.gumtree.com/search?sort=date&page=1&distance=0&guess_search_category=cars&q=&search_category=cars&search_location=edinburgh&vehicle_make=&vehicle_model=&vehicle_registration_year=&vehicle_mileage=&seller_type=&vehicle_body_type=&vehicle_fuel_type=&vehicle_transmission=&vehicle_engine_size=&min_price=&max_price=1000'
    ]

    def parse(self, response):
        filename = response.url.split('/')[-2] + '.html'
        items = Selector(text=response.body).css('article').extract()
        for i in items:
            car = CarssItem()
            item = Selector(text=i)
            car['description'] = item.css('.listing-description').xpath('text()').extract()[0]
            car['title'] = item.css('.listing-title').xpath('text()').extract()[0]
            car['year'] = item.css('span[itemprop=releaseDate]::text').extract()[0]
            car['fuel'] = item.css('span[itemprop=vehicleFuelType]::text').extract()[0]
            car['thumb'] = item.css('.listing-thumbnail img::attr(src)').extract()[0]
            mileage = int(''.join(item.css('span[itemprop=vehicleMileage]::text').re('[0-9]*')))

            if mileage < 999:
                mileage *= 1000
            car['mileage'] = mileage
            car['price'] = int(item.css('.listing-price::text').re('[0-9]*')[1])
            car['location'] = item.css('.listing-location span::text').extract()[0]
            car['link'] = 'https://www.gumtree.com' + item.css('.listing-link::attr(href)').extract()[0]
            car['ref'] = item.css('::attr(data-q)').extract()[0].split('-')[1]
            yield car