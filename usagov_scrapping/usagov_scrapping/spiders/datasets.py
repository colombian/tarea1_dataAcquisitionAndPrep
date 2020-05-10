# -*- coding: utf-8 -*-
import scrapy
import json
from usagov_scrapping.items import UsagovScrappingItem, usagovScrappingDataset


class DatasetsSpider(scrapy.Spider):
	name = 'datasets'
	page_num = 2
	allowed_domains = ['catalog.data.gov']
	start_urls = ['https://catalog.data.gov/dataset?page=1']
	gov = list()

	def parse(self, response):
		for url in response.css(".dataset-heading > a"):
			link = f"{url.attrib.get('href')}"
			title = link
			yield response.follow(link, callback=self.parse_dataset, meta={'link':link,'title':title})

		next_page = 'https://catalog.data.gov/dataset?page='+str(DatasetsSpider.page_num)
		if DatasetsSpider.page_num < 4:
			DatasetsSpider.page_num += 1
			yield scrapy.Request(next_page, callback=self.parse)

	def parse_dataset(self, response):
		page = UsagovScrappingItem()
		dataset = usagovScrappingDataset()

		page['link'] = response.meta['link']
		dataset['title'] = response.meta['title']
		dataset['paragraph'] = list()

		for text in response.css(".notes > p::text").extract():
			dataset["paragraph"].append(text)
		page["body"]=dataset
		return page