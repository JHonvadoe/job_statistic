import os
import csv
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from fake_useragent import UserAgent

ua = UserAgent()
url = os.environ['MORPH_HOST']
selector = os.environ['MORPH_SELECTOR']
session = HTMLSession()
session.headers = ua.random 

r.html.render()

vip_companies = r.html.select(selector)


for row in vip_companies:
    company = row.find('a span').text
    for pos in row.select('ul li'):
        print('has position ',pos.text)
    print('\n')




#with requests.Session() as s:
#    download = s.get(CSV_URL,ua)
#
#    decoded_content = download.content.decode('utf-8')
#
#    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
#    my_list = list(cr)
#    for row in my_list:
#        print(row)

