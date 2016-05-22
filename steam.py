import requests
import json
from bs4 import BeautifulSoup

class Steam:
    def __init__(self, id):
        url = 'http://steamcommunity.com/profiles/|/wishlist/'
        self.url = url.replace('|', str(id))
        self.wishlist = []
    def get(self):
        r = requests.get(self.url)
        parsed_html = BeautifulSoup(r.text, "html.parser");
        for x in parsed_html.body.findAll('div', attrs={'class':'wishlistRow'}):
            item = {
                'name': x.find('div', attrs={'class': 'wishlistRowItem'}).h4.text,
                'link': x.find('div', attrs={'class': 'gameListRowLogo'}).a['href']
            }
            # print x.find('div', attrs={'class': 'gameListPriceData'}).div['class']
            if x.find('div', attrs={'class': 'gameListPriceData'}).div['class'][0] == 'price':
                item['price'] = x.find('div', attrs={'class': 'gameListPriceData'}).div.text.strip().replace('$', '')
                item['discount'] = 0
            else:
                item['price'] = x.find('div', attrs={'class': 'gameListPriceData', 'class': 'discount_final_price'}).text
                item['discount'] = x.find('div', attrs={'class': 'gameListPriceData', 'class': 'discount_block'}).div.text.replace('-', '.').replace('%', '')
            self.wishlist.append(item)

steam = Steam(76561197968229753)
steam.get()
print steam.wishlist

# steam.get()
