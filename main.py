import urllib.request
from lxml import etree
import re

import Cons


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
    data = tree.xpath('//div[@class="title"]/a')
    for item in data:
        # titles = item.text.split(' ')
        # print('小区:%s' % titles[0])
        # print('室:%s' % titles[1][0])
        # print('厅:%s' % titles[1][2])
        # print('面积:%s' % titles[2][:1])
        print(item.text)
        print('---------------------------')


def get_ershou():
    tree = get_tree(Cons.URL_ERSHOU)
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
        dic={'name' : data1[x].text,
             'total_price':data2[x].text,
             'unit_price':data3[x].text,
             'url': data4[x],
             'bedroom':arry1[1][0],
             'livingroom':arry1[1][2],
             'area':arry1[2][:-2],
             'toward':arry1[3],
             'fitment':arry1[4],
             'follows':arry2[0][:-3],
             'visit_time':arry2[1][:-3],
             'pub_date': arry2[2][:-3],
             }
        # print(data1[x].text)
        #
        # print(arry1[1][0])
        # print(arry1[1][2])
        # print(arry1[2][:-2])
        # print(arry1[3])
        # print(arry1[4])
        # # print(data1[x].tail)
        #
        # print(data2[x].text)
        # print(data3[x].text)
        #
        # print(data4[x])
        # print(data5[x].tail)
        print(dic)
        print('---------------------------')

    # for item in data:
    #     # titles = item.text.split(' ')
    #     # print('小区:%s' % titles[0])
    #     # print('室:%s' % titles[1][0])
    #     # print('厅:%s' % titles[1][2])
    #     # print('面积:%s' % titles[2][:1])
    #     print(item.text)
    #     print('---------------------------')


if __name__ == '__main__':
    # get_chengjiao()
    get_ershou()




