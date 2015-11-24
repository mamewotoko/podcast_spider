podcast_spider
==============
Overview
--------
* crawl web pages
* get link to podcast xml
  * check content-type is application/rss+xml
  * check it has enclosure tag with mugic file 
* output podcast xml
  * title
  * url

Install
-------
1. install scrapy

How to run
----------
```bash
cd podcast
scrapy crawl podcast -o - -t json -s DOWNLOAD_DELAY=5.0 -s LOG_LEVEL=DEBUG > items.json
```
title, url, link of podcast xml if saved in items.json

TODO
-----
* add image of podcast
  * //channel/image/link
  * //channel/itunes:image/@href
* add selected podcast url to podplayer

----
Takashi Masuyama < mamewotoko@gmail.com >
