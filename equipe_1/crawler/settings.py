# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'
COOKIES_ENABLED = False
DOWNLOAD_DELAY = 2
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = { 'crawler.pipelines.CleanPipeline': 300, }
				   # 'crawler.pipelines.RemoveAccentsPipeline': 100 ,}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
