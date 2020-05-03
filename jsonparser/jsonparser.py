#  coding=utf-8

import re
import json

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

    # lists = list(map(lambda m: tuple(filter(bool, m)), url))
    for item in lists:
        if item:
            print(item)


if __name__ == "__main__":
    file = "C:/Users/lyf/Desktop/temp"
    parse_jsonfile(file)


