__author__ = "call_fold"

import Common.CrawlerToHTML
import os


def picture_crawler(url, reg, target_path, target_dir):
    image_list = Common.CrawlerToHTML.images_crawler(url, reg)
    Common.CrawlerToHTML.save_images(image_list, target_path, target_dir)

if __name__ == '__main__':
    # my_url = 'http://tieba.baidu.com/p/2166231880'
    # reg = r'src="(.+?\.jpg)" bdwater='
    # picture_crawler(my_url, reg, os.path.abspath('.'), 'images_shanbenyoumei')
    my_url = 'http://tieba.baidu.com/p/1792419362'
    reg = r'<img class="BDE_Image" src="(.+?\.jpg)"'
    picture_crawler(my_url, reg, os.path.abspath('.'), 'images_boduoyejieyi')