import scrapy


class BrickSetSpider(scrapy.Spider):
    name = 'brick_spider'
    start_urls = ['https://www.bprshop.com/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA-%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D8%A7%D9%BE%D9%84',
                  "https://www.bprshop.com/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA-%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D8%A7%DB%8C%D8%B3%D9%88%D8%B3",
                  "https://www.bprshop.com/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA-%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D9%84%D9%86%D9%88%D9%88",
                  "https://www.bprshop.com/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA-%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D8%A7%D9%8A%D8%B3%D8%B1",
                  "https://www.bprshop.com/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA-%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D8%A7%DA%86-%D9%BE%D9%8A",
                  "https://www.bprshop.com/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA-%D9%85%D8%A7%DB%8C%DA%A9%D8%B1%D9%88%D8%B3%D8%A7%D9%81%D8%AA-%D8%B3%D8%B1%D9%81%DB%8C%D8%B3-%D8%A8%D9%88%DA%A9",
                  "https://www.bprshop.com/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA-%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D8%A7%D9%85-%D8%A7%D8%B3-%D8%A2%DB%8C",
                  ]

    def parse(self, response):
        # SET_SELECTOR = 'plem1-tbl wide-view'
        for brickset in response.xpath('//*[@class="plem1-tbl wide-view"]//tbody/tr'):

            #               .// dl[dt / text() = "Pieces"] / dd / a / text()
            NAME_SELECTOR = 'td[2]//text()'
            PROCESSOR_SELECTOR = 'td[3]//text()'
            RAM_SELECTOR = 'td[4]//text()'
            HARD_SELECTOR = 'td[5]//text()'
            INCH_SELECTOR = 'td[8]//text()'
            PRICE_SELECTOR = 'td[12]//text()'

            yield {
                'name': brickset.xpath(NAME_SELECTOR).extract_first(),
                'processor': brickset.xpath(PROCESSOR_SELECTOR).extract_first(),
                'ram': brickset.xpath(RAM_SELECTOR).extract_first(),
                'hard': brickset.xpath(HARD_SELECTOR).extract_first(),
                'inch': brickset.xpath(INCH_SELECTOR).extract_first(),
                'price': brickset.xpath(PRICE_SELECTOR).extract_first(),

            }
