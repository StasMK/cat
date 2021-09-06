from bs4 import BeautifulSoup
import requests
import csv
from itertools import groupby
import pandas as pd

# import Threading
c_list = []
c_list1 = []
c_list_clr = []
c_list_clr1 = []

response = requests.get("https://catalog.onliner.by")
soup = BeautifulSoup(response.content, "lxml")
page_2 = soup.find_all("a")
for item in page_2:
    item_url = item.get("href")
    if item_url != "#" and item_url != None:
        if item_url.find("https://catalog.onliner.by/") == 0:
            if item_url.find("?") <= 0:
                if item_url.count("/") <= 3:
                    if item_url != "https://catalog.onliner.by/":
                        c_list.append(item_url)
c_list.sort()
new_c_list = [el for el, _ in groupby(c_list)]
c_list = new_c_list
with open("c:/www/MyWeb/file_list_1.csv", 'w', newline='') as f:
    fc = csv.writer(f, delimiter='\n')
    fc.writerow(c_list)

k = 0
for i in c_list:
    if k < 2:
        response = requests.get(i)
        soup = BeautifulSoup(response.content, "lxml")
        # page_1 = soup.find("div", class_="catalog-navigation-list__dropdown-list").find("a").attrs.get("href")
        page_3 = soup.find_all("a")
        for item in page_3:
            item_url_1 = item.get("href")
            if item_url_1 != "#" and item_url_1 != None:
                if item_url_1.find(i) == 0:
                    if item_url_1.find("?") <= 0:
                        if item_url_1.count("/") >= 5:
                            c_list1.append(item_url_1)
                            k = k + 1
c_list1.sort()
new_c_list = [el for el, _ in groupby(c_list1)]
with open("c:/www/MyWeb/file_name.csv", 'w', newline='') as f:
    fc = csv.writer(f, delimiter='\n')
    fc.writerow(new_c_list)

# df = pd.DataFrame(c_list1)
# writer = pd.ExcelWriter('c:/www/MyWeb/test.xlsx', engine='xlsxwriter')
# df.to_excel(writer, sheet_name='welcome', index=False)
# writer.save()


'''
class="schema-product__group"
class="schema-product"
class="schema-product__part schema-product__part_2"
class="schema-product__part schema-product__part_3"
class="schema-product__price-group"
class="schema-product__line"
class="schema-product__offers"
class="schema-product__button button button_orange"
получаем ссылку

class="product-main"
class="product-primary js-product-primary"
class="product-primary-i"
class="product-gallery__main"
class="product-gallery__thumbs fotorama__nav--thumbs js-gallery-thumbs mCustomScrollbar _mCS_1 mCS_no_scrollbar"
class="mCustomScrollBox mCS-light mCSB_horizontal mCSB_inside"
class="mCSB_container mCS_x_hidden mCS_no_scrollbar_x"
class="product-gallery__shaft"
product-gallery__thumb js-gallery-thumb
ищем src=""

так тысячи раз и котик найден










'''
