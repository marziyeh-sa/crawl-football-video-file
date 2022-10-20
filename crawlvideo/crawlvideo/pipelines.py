
from scrapy.pipelines.files import FilesPipeline

# class CrawlvideoPipeline:
#     def process_item(self, item, spider):
#         return item


class CustomFilePipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        return item.get('Title') + '.mp4'



