import urllib.request
from lxml import etree
import re
import time

import Cons
from DB import DBProvider

dbProvider = DBProvider()

def get_tree(url):
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/51.0.2704.103 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=header)
    page = urllib.request.urlopen(req).read().decode('UTF-8')
    # print(page)
    tree = etree.HTML(page)
    return tree


def get_chengjiao():
    tree = get_tree(Cons.URL_CHENGJIAO)
    data1 = tree.xpath('//div[@class="title"]/a')
    data2 = tree.xpath('//div[@class="totalPrice"]/span')
    data3 = tree.xpath('//div[@class="unitPrice"]/span')
    for x in range(len(data1)):
        '''
            data1: 小区名 x室y厅 面积
            data2: 总价
            data3: 单价
            data4: url
            data5: 关注 / 看房 / 发布日期

            '''
        titles = data1.text.split(' ')
        unit_price = get_re_digits(Cons.ERSHOU, data3[x].text)
        url = get_re_digits(Cons.ERSHOU, data4[x])
        visit = get_re_digits(Cons.ERSHOU, arry2[1])

        dic = {'name': titles[0],
               'total_price': data2[x].text,
               'unit_price': data3,
               'url': url,
               'bedroom': titles[1][0],
               'livingroom': titles[1][2],
               'area': titles[2][:-2],
               'toward': arry1[3],
               'fitment': arry1[4],
               'follows': arry2[0][:-3],
               'visit_time': visit,
               'pub_date': arry2[2],
               }
        print(dic)
        print('---------------------------')

        # titles = item.text.split(' ')
        # print('小区:%s' % titles[0])
        # print('室:%s' % titles[1][0])
        # print('厅:%s' % titles[1][2])
        # print('面积:%s' % titles[2][:1])



def get_ershou():
    list = []
    num = 0
    dbProvider.db_conn()
    for i in range(1,100):
        tree = get_tree(Cons.URL_ERSHOU + '/pg' + str(i) + '/')
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
            unit_price = get_re_digits(Cons.UNIT_PRICE, data3[x].text)
            url = get_re_digits(Cons.ERSHOU, data4[x])

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
    # get_chengjiao()
    get_ershou()
