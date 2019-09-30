import requests
import pandas as pd
import csv
import ssl
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import HTTPError

num = 29343
def print_stock_price(page_num, headers, num):
    for n in range(921840, 930000):
        title_des_dict = dict()
        try:
            r = urlopen('https://www.archdaily.com/' + str(n) + "/error.html")
        except HTTPError as e:
            continue
        try:
            r = urlopen('https://www.archdaily.com/' + str(n) + "/error.html")
        except ssl.SSLEOFError as e:
            continue
        r = requests.get('https://www.archdaily.com/' + str(n) + "/", headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser', from_encoding='utf-8')
        print(n, "번째 페이지 값 = -----Ok-----")
        if soup.find("h1", {
            "class": "afd-title-big afd-title-big--left afd-title-big--"
                     "full afd-title-big--bmargin-small afd-relativeposition"}) == None:
            continue
        title_ = soup.find("h1", {
            "class": "afd-title-big afd-title-big--left afd-title-big--"
                     "full afd-title-big--bmargin-small afd-relativeposition"}).text
        title_ = title_.replace("\n", "")
        title = []
        title.append(title_)

        description = ''
        des_ = soup.find("article", {"class": "afd-post-content"}).text.split('\n')
        for i in range(len(des_)):
            if len(des_[i]) < 150:
                des_[i] = "none"
        our_des_data = []
        for i in range(len(des_)):
            if des_[i] != 'none':
                our_des_data.append(des_[i])
        for i in range(len(our_des_data)):
            description += our_des_data[i]

        f_des = []
        f_des.append(description)

        title_des_list = []
        title_des_dict['Row'] = str(num)
        title_des_dict['Name'] = title[0]
        title_des_dict['Des'] = f_des[0]
        title_des_list.append(title_des_dict)

        with open('ArchDaily.csv', 'a', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=csv_columns)
            for data in title_des_list:
                writer.writerow(data)
        num += 1


headers = {'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; rv:11.0) like Gecko'}

pages = 100
csv_columns = ['Row', 'Name', 'Des']
print_stock_price(pages, headers, num)

# with open('ArchDaily.csv', 'w', encoding='utf-8') as f:
#     writer = csv.DictWriter(f, fieldnames=csv_columns)
#     for data in title_des_list:
#         writer.writerow(data)

# f = open('ArchDaily.csv', 'r', encoding='utf-8')
# rdr = csv.reader(f)
# for line in rdr:
#     print(line)
# f.close()

