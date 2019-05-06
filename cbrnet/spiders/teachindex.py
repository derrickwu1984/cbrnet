# -*- coding: utf-8 -*-
import scrapy,requests,re
from lxml import etree

class TeachindexSpider(scrapy.Spider):
    name = 'teachindex'
    allowed_domains = ['www.cbrnetechindex.com']
    start_urls = ['http://www.cbrnetechindex.com']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.FormRequest(url=url,
                                 method="POST", callback=self.get_total_urls)
    def get_total_urls(self,response):
        html = etree.HTML(response.body)
        list_content = html.xpath("//ul[@class ='list_content']/div[@class='main_column']/li/a/@href")
        print (type(list_content))
        # for url in list_content:
        #     yield scrapy.FormRequest(url=url, method="POST", callback=self.get_items_urls)
    def get_items_urls(self,response):

        pass
    def parse(self, response):
        pass
