#  coding=utf-8

import re
import json
import os

pattern = re.compile(r'(?i)\b((?:https?:\/|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))')

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


if __name__ == "__main__":
    file = "C:/Users/lyf/Desktop/temp"
    lists = parse_jsonfile(file)
    for item in lists:
        print(item)

