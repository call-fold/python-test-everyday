__author__ = "call_fold"

from PIL import Image
import os
import glob

def get_files_name(source_path, kind_of_file):
    target_picture_list = []
    for file in glob.glob(source_path + "/*." + kind_of_file):
        file_path, file_name = os.path.split(file)
        target_picture_list.append(file_name)
    return target_picture_list

def check_folder(target_dir):
    current_path = os.path.abspath('.')
    target_dir_path = current_path + '/' + target_dir
    if not os.path.isdir(target_dir_path):
        os.mkdir(target_dir_path)
    return target_dir_path

def change_picture_dpi(source_path, target_path):
    iphone5_size = (1136, 640)
    picture_list = get_files_name(source_path, 'jpg')
    for picture in picture_list:
        image = Image.open(source_path + '/%s' % picture)
        current_size = image.size
        if iphone5_size[0] / current_size[0] < iphone5_size[1] / current_size[1]:
            if int(current_size[1] / current_size[0] * 1136) < 640:
                current_size = (1136, int(current_size[1] / current_size[0] * 1136))
            else:
                current_size = iphone5_size
        else:
            if int(current_size[0] / current_size[1] * 640) < 1136:
                current_size = (int(current_size[0] / current_size[1] * 640), 640)
            else:
                current_size = iphone5_size
        print(picture)
        print(current_size)
        new_image = image.resize(current_size)
        new_image.save(target_path + '/%s' % picture)

if __name__ == '__main__':
    change_picture_dpi(os.path.abspath('.') + '/pictures', check_folder('pictures_new'))

