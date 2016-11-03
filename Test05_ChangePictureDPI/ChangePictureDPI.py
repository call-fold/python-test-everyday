__author__ = "call_fold"

from PIL import Image
import os
import Common.FileCommon


def change_picture_dpi(source_path, target_path, kind_of_picture):
    iphone5_size = (1136, 640)
    picture_list = Common.FileCommon.get_file_name_list_by_kind(source_path, kind_of_picture)
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
    change_picture_dpi(os.path.abspath('.') + '/pictures',
                       Common.FileCommon.check_folder(os.path.abspath('.'), 'pictures_new'), 'jpg')
