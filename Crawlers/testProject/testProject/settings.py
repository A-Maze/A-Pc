# -*- coding: utf-8 -*-

# Scrapy settings for testProject project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'testProject'

SPIDER_MODULES = ['testProject.spiders']
NEWSPIDER_MODULE = 'testProject.spiders'

ITEM_PIPELINES = ['testProject.pipelines.TestprojectPipeline',]

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "azerty"
MONGODB_COLLECTION = "processoren"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'testProject (+http://www.yourdomain.com)'
