import os
import re

path = os.getcwd()

file = os.path.join(path, "README.md")
content = open(file)

for line in content:
    if line.startswith('versioncode'):
        name = re.search(r"\d+", line)
        print("code %s" % name.group())

    if line.startswith("versionname"):
        name = re.search(r"\d+(\.\d+)*", line)
        print("name %s " % name.group())

file = os.path.join(path, "temp")
for file in os.listdir(file):
    print("file %s" % file)

build_type = input(
    "please select build mode: 0(default,failed if exist same destination), 9(over, cover the exist destination):")

print("lyf")
print("bankle")
print("build_type %s " % build_type)
