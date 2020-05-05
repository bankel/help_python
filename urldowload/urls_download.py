#  coding=utf-8

"""urls_download.py: download url from remote server."""

__author__ = "Banks li"
__copyright__ = "Copyright 2020, Planet Earth"

import json
import os
import re
import time
import sys
import requests

pattern = re.compile(
    r'(?i)\b((?:https?:\/|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))')

flatten = lambda *n: (e for a in n
                      for e in (flatten(*a) if isinstance(a, (tuple, list)) else (a,)))


def parse_jsonfile(json_file):
    json_object = json.load(open(json_file))
    # print(type(json_object))

    string = json.dumps(json_object)
    # print(type(string))

    url = re.findall(pattern, string)

    lists = flatten(url)

    lists = filter(bool, lists)
    # change filter to list
    lists = list(lists)
    print("before filter size %s" % len(lists))
    # for item in lists:
    #     print(item)

    temp_list = []

    args = sys.argv
    filter_type = ()
    if len(args) >= 4:
        filter_type = str(args[3]).split(',')
        print("download file that is belong to %s " % filter_type)

    if len(filter_type):
        temp_list = list(x for x in lists if str(x).split('.')[-1].lower() in filter_type)
    else:
        temp_list = lists

    dif_list = list(set(lists).difference(set(temp_list)))
    print("filter---")
    for dif in dif_list:
        print(dif)
    print("filter---")
    print("after filter size %s \n" % len(lists))
    # for item in filter_list:
    #     print(item)
    return temp_list


def __download(dir, url_list):
    count = 0
    failed_list = []
    for url in url_list:
        # name of folder
        try:

            # save remote data to destination
            parent = str(url).split('/')[-2]

            folder = os.path.join(os.path.sep, os.getcwd(), dir, parent)
            # print("folder ", folder)
            if not os.path.exists(folder):
                try:
                    os.makedirs(folder)
                except Exception as e:
                    print("create folder error %s " % e)

                    raise e

            # file to download
            file_name = str(url).split('/')[-1]
            local_file = os.path.join(os.path.sep, folder, file_name)
            if os.path.exists(local_file) and os.path.getsize(local_file) > 0:
                # print("%s exists " % file_name)
                count += 1
                continue

            data = None
            request_time = 0
            while True:
                try:

                    # proxies = get_proxy()
                    # print('代理IP: %s' % proxies)
                    res = requests.get(url, timeout=3)
                    # print('response : %s, url: %s' % (res.status_code, url))
                    if res.status_code == 200:
                        data = res.content
                        break
                    else:
                        request_time += 1
                        if request_time > 5:
                            print('error response : %s, url: %s' % (res.status_code, url))
                            break
                except Exception as e:
                    print('numbers for request: %s (%s)' % (request_time, e))

                    request_time += 1
                    if request_time > 5:

                        res = requests.get(url)
                        if res.status_code == 200:
                            data = res.content
                        break
                    continue

            # print(local_file)
            if data:
                with open(local_file, 'wb') as f:
                    f.write(data)
                    print('download %s to %s successful: ' % (url, local_file))
                    count += 1
                    time.sleep(0.3)
            else:
                failed_list.append(url)
        except Exception as e:
            print('download error:, (%s)' % e)
            failed_list.append(url)
            continue

    print("successful download %s , failed %s " % (count, len(failed_list)))
    if len(failed_list) > 0:
        print("failed =======:")
        for fail_url in failed_list:
            print("%s" % fail_url)
        print("failed =======:")



def get_proxy():
    try:
        get_proxy_utl = 'http://91.225.165.4/57021'
        res = requests.get(get_proxy_utl)
        if res.status_code == 200:
            print('get ip from proxy pool: %s' % res.text)
            proxies = {'http': 'http://' + res.text}
            return proxies
        else:
            return None
    except Exception as e:
        print('error when get id from proxy pool！！ %s' % e)
        return None


def download_url():
    args = sys.argv
    if len(args) < 3:
        raise Exception("must provide source file and destination folder")

    print("source: %s, target folder: %s " % (args[1], args[2]))

    # check source file exists
    current_work_path = os.getcwd()
    path = os.path.join(os.path.sep, current_work_path, args[1])
    if not os.path.exists(path):
        print("%s is not exists" % path)
        return

    url_lists = parse_jsonfile(args[1])
    __download(args[2], url_lists)


def test_sys_args():
    args = sys.argv
    for arg in args:
        print(arg)

    args = sys.argv
    filter_type = ()
    if len(args) >= 4:
        filter_type = str(args[3]).split(',')

    if len(filter_type):
        print("filter file type %s " % filter_type)


if __name__ == "__main__":
    # test_sys_args()
    download_url()
