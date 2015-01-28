'''
This is a spider that specifically crawls for the NHL Standings in the Metropolitan Division
'''


import scrapy


class NhlStandingsSpider(scrapy.Spider):
    name = "nhl"
    allowed_domains = ["nhl.com"]
    start_urls = [
        "http://www.nhl.com/ice/standings.htm",
    ]

    def parse(self, response):
        table = response.xpath('//*[@id="wideCol"]/div[5]/table[2]/tbody')
        td = '//*[@id="wideCol"]/div[5]/table[2]/tbody/tr['

        f = open('output.txt', 'w')

        f.write('      ' + " P" + '   ' + "GP" + '  ' + "W " + '  ' + "L " + '  ' + "OT\n")
        for position in range(1, 9):
            team = table.xpath(td+str(position)+']/td[2]/a[2]/@rel').extract()[0]
            gamesPlayed = table.xpath(td+str(position)+']/td[3]/text()').extract()[0]
            gamesWon = table.xpath(td+str(position)+']/td[4]/text()').extract()[0]
            gamesLost = table.xpath(td+str(position)+']/td[5]/text()').extract()[0]
            otGamesLost = table.xpath(td+str(position)+']/td[6]/text()').extract()[0]
            points = table.xpath(td+str(position)+']/td[7]/text()').extract()[0]

            f.write(str(position) + ' ' + team + '  ' + points + '  ' + gamesPlayed + '  ' + gamesWon + '  ' + gamesLost + '  ' + otGamesLost + '\n')
        f.close()
