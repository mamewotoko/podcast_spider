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

How to run
----------
1. install scrapy
2. run
```bash
cd podcast
#scrapy crawl podcast -o - -t json -s DOWNLOAD_DELAY=5.0 -s LOG_LEVEL=DEBUG > items.json
sh run.sh
```
title, url, link of podcast xml if saved in items.json

How to run (on docker)
----------------------
```bash
cd podcast
sh docker_run.sh
```

TODO
-----
* add QR code
  * https://github.com/oostendo/python-zxing
* improve select podcast performance of html
  * update by difference
* add image of podcast
  * //channel/image/link
  * //channel/itunes:image/@href
* add selected podcast url to podplayer

----
Takashi Masuyama < mamewotoko@gmail.com >
http://mamewo.ddo.jp/
