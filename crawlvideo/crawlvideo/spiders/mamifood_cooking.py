from scrapy import Request, Spider

class SiteSPider(Spider):
    name = 'mamifood_cooking'
    start_urls = [
        'https://www.scrapebay.com/ebooks'
    ]

def parse(self, response):
    for book in response.css('.col'):
        title = book.css('h5 ::text').get()
        link = response.urljoin(
            book.css('a.pdf ::attr(href)').get()
        )
        yield {
            'title': title,
            'file_urls': [link]
        }
