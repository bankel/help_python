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
