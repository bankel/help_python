import os
import shutil

old_name = '矩形 2.png'
new_name = 'home_page_top_bg.png'
new_path = '/Users/lyf/AndroidStudioProjects/github/PaintArt/app/src/main/res'


def copy(path):
    for file in os.listdir(path):
        if file.startswith('.'):
            continue
        if os.path.isdir(os.path.join(path, file)):
            copy(os.path.join(path, file))

        else:  # start to rename and copy
            if file == old_name:
                consist = file.split('.')
                new_file = new_name.split('.')[0] + "." + consist[-1]
                os.rename(os.path.join(path, file), os.path.join(path, new_file))

                copy_file = os.path.join(path, new_file)
                parent_path = copy_file.split(os.sep)[-2]
                des_path = os.path.join(new_path, parent_path)

                if not os.path.exists(des_path):
                    os.mkdir(des_path)

                des_file = os.path.join(des_path, new_file)
                shutil.copy(copy_file, des_file)


def only_copy(path):
    for file in os.listdir(path):
        if file.startswith('.'):
            continue
        if os.path.isdir(os.path.join(path, file)):
            only_copy(os.path.join(path, file))

        else:  # start to rename and copy
            if file == new_name:

                copy_file = os.path.join(path, file)
                parent_path = copy_file.split(os.sep)[-2]
                des_path = os.path.join(new_path, parent_path)

                if not os.path.exists(des_path):
                    os.mkdir(des_path)

                des_file = os.path.join(des_path, file)
                shutil.copy(copy_file, des_file)


if __name__ == '__main__':
    path = "/Users/lyf/Downloads/首页改/assets/"
    # copy(path)
    copy(path)
