# -*- coding: utf-8 -*-

# Scrapy settings for pccrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'pccrawler'
SPIDER_MODULES = ['pccrawler.spiders']
NEWSPIDER_MODULE = 'pccrawler.spiders'
ITEM_PIPELINES = ['pccrawler.pipelines.PccrawlerPipeline',]
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "components"
MONGODB_COLLECTION = "processoren"
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pccrawler (+http://www.yourdomain.com)'