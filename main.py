import urllib.request
from lxml import etree
import re
import time

from consts import const
from db import DBProvider

dbProvider = DBProvider()

def get_tree(url):
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/51.0.2704.103 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=header)
    page = urllib.request.urlopen(req).read().decode(const.ENCODE_FORM)
    # print(page)
    tree = etree.HTML(page)
    return tree


def get_chengjiao():
    tree = get_tree(const.URL_CHENGJIAO)
    data1 = tree.xpath('//div[@class="title"]/a')
    data2 = tree.xpath('//div[@class="totalPrice"]/span')
    data3 = tree.xpath('//div[@class="unitPrice"]/span')
    data4 = tree.xpath('//div[@class="title"]/a/@href')
    data5 = tree.xpath('//div[@class="houseInfo"]/text()')
    data6 = tree.xpath('//div[@class="positionInfo"]/text()')
    data7 = tree.xpath('//span[@class="dealHouseTxt"]/span')
    data8 = tree.xpath('//div[@class="dealDate"]/text()')
    for x in range(len(data1)):
        '''
            data1: 小区名 x室y厅 面积
            data2: 总价
            data3: 单价
            data4: url
            data5: 关注 / 看房 / 发布日期

            '''
        titles = data1[x].text.split(' ')
        url = get_re_digits(const.CHENGJIAO, data4[x])
        houseInfo = data5[x].split(' | ')


        dic = {'name': titles[0],
               'total_price': data2[x].text,
               'unit_price': data3[x].text,
               'url': url,
               'bedroom': titles[1][0],
               'livingroom': titles[1][2],
               'area': titles[2][:-2],
               'toward': houseInfo[0],
               'fitment': houseInfo[1],
               'floor': data6[x][0],
               'deal_date': data8[x]
               }
        print(dic)
        print('---------------------------')



def get_ershou():
    list = []
    num = 0
    dbProvider.db_conn()
    for i in range(1,100):
        tree = get_tree(const.URL_ERSHOU + '/pg' + str(i) + '/')
        data1 = tree.xpath('//div[@class="houseInfo"]/a')
        data2 = tree.xpath('//div[@class="totalPrice"]/span')
        data3 = tree.xpath('//div[@class="unitPrice"]/span')
        data4 = tree.xpath('//div[@class="title"]/a/@href')
        data5 = tree.xpath('//div[@class="followInfo"]/span')
        for x in range(len(data1)):
            '''
            data1: 小区名 | x室y厅 | 面积 | 朝向 | 装修
            data2: 总价
            data3: 单价
            data4: url
            data5: 关注 / 看房 / 发布日期

            '''
            arry1 = data1[x].tail.split(' | ')
            arry2 = data5[x].tail.split(' / ')
            unit_price = get_re_digits(const.UNIT_PRICE, data3[x].text)
            url = get_re_digits(const.ERSHOU, data4[x])

            dic = {'name': data1[x].text,
                   'total_price': data2[x].text,
                   'unit_price': unit_price,
                   'url': url,
                   'bedroom': arry1[1][0],
                   'livingroom': arry1[1][2],
                   'area': arry1[2][:-2],
                   'toward': arry1[3],
                   'fitment': arry1[4],
                   'follows': arry2[0][:-3],
                   'visit_times': arry2[1][1:-3],
                   'pub_date': arry2[2],
                   'remarks': ''
                   }
            dbProvider.add_ershou(dic)
            num=num+1
            print('input: ' + str(num))
            # list.append(dic)
    # print(len(list))
    dbProvider.db_close()



def get_re_digits(pre_str, target_str):
    SEARCH_DATA4 = re.compile(r'' + pre_str + '\/*(\d+)')
    value_search = SEARCH_DATA4.search(target_str)
    value=''
    if value_search != None:
        value = value_search.group(1)
    return value


if __name__ == '__main__':

    get_chengjiao()
    #get_ershou()
