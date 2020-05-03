# -*- coding:utf-8 -*-
####################################################
#
#    Author: Chuwei Luo
#    Email: luochuwei@gmail.com
#    Date: 17/03/2016
#    Usage: Matching all urls
#
####################################################
import re


def find_all_url(sentence, show_urls=None, delete_urls=None):
    r = re.compile(
        r'(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))')
    url_list = r.findall(sentence)
    if show_urls == 1:
        print("find", str(len(url_list)), "URLs")

        for i in url_list:
            print(i[0])


    if delete_urls == 1:
        for j in url_list:
            # sentence = sentence.replace(j[0], '<URL>')
            sentence = sentence.replace(j[0], '')
        return sentence
    return 1


if __name__ == '__main__':
    s1 = '很急很关键 www.whu.edu.cn'
    s2 = '在下头很硬 http://cs.whu.edu.cn'
    s3 = 'http://goo.gl/BmT8gZ 匹配不到就删除python了https://goo.gl/MxRdMO'
    s4 = '我的邮箱是Emal:luochuwei@gmail.com 也可以联系我的武汉大学邮箱，但是不告诉你^_^'

    find_all_url(s4)
    print()
    find_all_url(s4, delete_urls=1)
    find_all_url(s4, show_urls=1)
    print()
    '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    find_all_url(s3)
    print()
    find_all_url(s3, delete_urls=1)
    find_all_url(s3, show_urls=1)

