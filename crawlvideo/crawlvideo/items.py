# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from dataclasses import dataclass
from itemadapter import ItemAdapter
from typing import List

class CrawlvideoItem(scrapy.Item):
    # title: scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()


# class NewsItem:
#     publisher_username: str
#     main_category: str
#     second_category: str

#     text: List
#     tags: List
#     source_url: str

