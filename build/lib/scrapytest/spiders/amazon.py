# -*- coding: utf-8 -*-
import scrapy
import os
from selenium import webdriver
from scrapytest.items import ScrapytestItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    def parse(self, response):
        test = response.xpath('//*[@id="nav-your-amazon-text"]')
        

        item = ScrapytestItem()
        item['test'] = test.extract()

        yield item
