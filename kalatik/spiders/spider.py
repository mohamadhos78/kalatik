import scrapy
from kalatik.items import KalatikItem

class Mainspider(scrapy.Spider):
    name = "kalatik"
    start_urls = [
        "https://kalatik.com/21-mobile" ,
    ]
    browsed = set()
    def parse(self, response):
        links = response.xpath('/html/body/div/div[5]/div[2]/div/div[1]/div/div/ul/li/div/div[2]/h3/a/@href').extract()
        for link in links:
            if link not in self.browsed:
                self.browsed.add(link)
                yield scrapy.Request(link, callback=self.mobile_extract)
        
        next_page = response.xpath('//li[@id="pagination_next"]/a/@href').get()
        url = "https://kalatik.com" + next_page
        print(url)
        if next_page and url not in self.browsed:
            self.browsed.add(url)
            yield scrapy.Request(url, callback=self.parse)

    def mobile_extract(self,response):
        item = KalatikItem()
        item["title"] = response.xpath('//div[@id="short_description_block"]/h1/text()').get()
        item["description"] = response.xpath('//div[@id="short_description_block"]//div[2]/h2/text()').get()
        color_data = response.xpath('//ul[@id="color_to_pick_list"]//li/a/i/text()').getall()
        item["colors"] = ''
        for color in color_data:
            item['colors'] += color + ","
        price = response.xpath('//span[@id="our_price_display"]//text()').get()
        if price:
            item["price"] = price
        else:
            item["price"] = ""
        item["brand"] = response.xpath('//div[@class="spec brand"]//a//img//@alt').get()
        print(item['description'])
        return item
        