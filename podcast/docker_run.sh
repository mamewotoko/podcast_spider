#! /bin/sh
IMAGE=allanfann/scrapy
docker pull ${IMAGE}
docker run -v `pwd`:/app ${IMAGE} sh run.sh
