#  coding=utf-8

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
    print(type(json_object))

    string = json.dumps(json_object)
    print(type(string))

    url = re.findall(pattern, string)

    lists = flatten(url)

    lists = filter(bool, lists)
    # for item in lists:
    #     print(item)

    filter_list = filter(lambda x: (not str(os.path.split(x)[-1]).endswith("pdf")), lists)

    # for item in filter_list:
    #     print(item)
    return filter_list


def __download(dir, list):
    for url in list:
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
                print("%s exists " % file_name)
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
                    time.sleep(0.3)

        except Exception as e:
            print('download error:, (%s)' % e)
            continue


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

    lists = parse_jsonfile(args[1])
    __download(args[2], lists)


def test_sys_args():
    path = os.getcwd()
    print(path)


if __name__ == "__main__":
    # test_sys_args()
    download_url()
