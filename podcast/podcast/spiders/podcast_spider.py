import urlparse
import scrapy
from podcast.items import PodcastItem

class PodcastSpider(scrapy.Spider):
    name = "podcast"
    allowed_domains = ["tfm.co.jp", "fmtoyama.co.jp", "tbsradio.jp"]
#    start_urls = [ "http://www.tfm.co.jp/podcasts/" ]
#                   "http://www.fmtoyama.co.jp/" ]
#start_urls = [ "http://www.fmtoyama.co.jp/" ]
    start_urls = ["https://radiocloud.jp/"]
    visited = list(start_urls)

    def parse(self, response):
        self.logger.info("parse: "+response.url)
        self.visited.append(response.url)
        content_type = response.headers['Content-Type']
        if content_type.startswith("text/html"):
            links = response.xpath("//a/@href").extract()
            #
            # radiocloud(tbs): toppage -> /archive/ -> rss
            podcast_pages = filter(lambda x: "xml" in x or "podcast" in x or ("radiocloud" in x and "/archive/" in x), list(set(links)))
            for url in podcast_pages:
                next_url = response.urljoin(url.strip())
                if next_url not in self.visited and not next_url.endswith(".mp3"):
                    self.logger.info("next: " + next_url)
                    self.visited.append(next_url)
                    yield scrapy.Request(next_url, callback=self.parse)
        elif content_type.startswith("application/rss+xml") or content_type.startswith("text/xml") or content_type.startswith("application/xml"):
            title = response.xpath("//channel/title/text()").extract()[0]
            link = response.xpath("//channel/link/text()").extract()[0]
            enctag = response.xpath("//enclosure")
            has_audio = False
            for tag in enctag:
                mimetypel = tag.xpath("@type").extract()
                if len(mimetypel) > 0 and mimetypel[0].startswith("audio/"):
                    has_audio = True
                    break
            self.logger.info("hasAudio: "+ str(has_audio) + " " + response.url)
            if has_audio:
                item = PodcastItem()
                item['title'] = title
                item['url'] = response.url.decode('utf-8')
                item['link'] = link
                yield item
               
