from scrapy import Request, Spider


class SiteSpider(Spider):
    name = 'khabarvarzeshi_video'
    start_urls = [
         'https://www.khabarvarzeshi.com/service/video'
     ]

    def parse(self, response):
        news_links = response.css('li.video div.desc h3 a ::attr(href)').getall()
        for news_link in news_links:
            joined_news_link = response.urljoin(news_link)
            yield Request(url=joined_news_link, callback=self.achive_media)

    @staticmethod
    def achive_media(response):

        video = []
        for vid in response.css('div.video-download'):
            video_link = vid.css('a ::attr(href)').get()
            start = video_link.find('?ts')
            if start != -1:
                video_link = video_link[:start]
            video.append(video_link)
        title_ = response.css('div.item-title h1.title a ::text').get()

        yield {
            'Title': title_,
            'file_urls': video
        }




