#  coding=utf-8
import os

path = '/Users/lyf/Desktop/转化图'


def rename(path):
    for root, dirs, files in os.walk(path):
        number_sequence = 1
        for file in files:
            if not file.startswith("."):
                file_p = os.path.join(root, file)
                suffix = os.path.splitext(file_p)[-1]
                new_file_name = os.path.join(root, "%03d%s" % (number_sequence, suffix))
                os.rename(file_p, new_file_name)
                print("%s rename to %s" % (file, new_file_name))
                number_sequence += 1


if __name__ == "__main__":
    rename(path)
