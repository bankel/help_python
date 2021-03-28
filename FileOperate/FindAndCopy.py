import os
import subprocess
import shutil


def find_and_copy():
    rootpath = "/Users/lyf/Downloads/daxigua-1.0-2.0/res/raw-assets"
    os.chdir(rootpath)

    images = (
        "ebdc0e91-9eb2-40b6-8211-5061a73bb542.png",
        "856267d0-6891-4660-a28a-3eb110bf6395.png",
        "d314aef5-920d-44f4-aa26-423c3664acc6.mp3"
    )

    pendding_command = "find ./ -name {0}"
    for image in images:
        command = pendding_command.format(image)
        output = subprocess.getoutput(command)

        command = "cp %s ~/Desktop/temp/mergeWaterMelon/" % output
        os.system(command)
    pass


def collect_files():
    source_path = "/Users/lyf/Downloads/daxigua-1.0-2.0/res/raw-assets"
    target_path = "/Users/lyf/Desktop/temp/mergeWaterMelon/sources"
    for root, dirs, files in os.walk(source_path):
        for file in files:
            f = os.path.join(root, file)
            target_file = os.path.join(target_path, file)
            shutil.copyfile(f, target_file)


    pass


if __name__ == "__main__":
    collect_files()