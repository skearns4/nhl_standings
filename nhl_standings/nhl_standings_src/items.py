# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NhlStandingsItem(scrapy.Item):
    team = scrapy.Field()
    position = scrapy.Field()
    gamesPlayed = scrapy.Field()
    gamesWon = scrapy.Field()
    gamesLost = scrapy.Field()
    otGamesLost = scrapy.Field()
    points = scrapy.Field()