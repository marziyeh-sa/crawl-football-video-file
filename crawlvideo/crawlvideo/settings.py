# Scrapy settings for crawlvideo project

BOT_NAME = 'crawlvideo'

SPIDER_MODULES = ['crawlvideo.spiders']
NEWSPIDER_MODULE = 'crawlvideo.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#     'scrapy.pipelines.files.FilesPipeline': 1,
# }
ITEM_PIPELINES = {'crawlvideo.pipelines.CustomFilePipeline': 1}
DOWNLOAD_TIMEOUT = 1200

FILES_STORE = r"video/"
