__author__ = "call_fold"

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import Common.Random
import random
import os


def make_random_num_pic(font_type_path, str, out_path, width=400, height=200):
    im = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(font_type_path, width // 4)
    font_width, font_height = font.getsize(str)
    # print(font_width, font_height)
    str_len = len(str)
    x = (width - font_width) // 2
    y = (height - font_height) // 2
    # print(x, y)
    total_dex = 0
    for char in str:
        draw.text((x, y), char, Common.Random.create_random_color_RGB(), font)
        temp = random.randint(-15, 15)
        total_dex += temp
        # rotate an angle
        im = im.rotate(temp)
        draw = ImageDraw.Draw(im)
        x += font_width / str_len
    im = im.rotate(-total_dex)
    # im.save('test1.jpg')
    draw = ImageDraw.Draw(im)
    # add random lines
    draw.line(
        [(random.randint(0, width // 4),
          random.randint(0, height // 4)
          ),
         (random.randint(width // 4 * 3, width),
          random.randint(height // 4 * 3, height)
          )],
        Common.Random.create_random_color_RGB(),
        width // 80
    )
    draw.line(
        [(random.randint(0, width // 4),
          random.randint(height // 4 * 3, height)
          ),
         (random.randint(width // 3 * 2, width),
          random.randint(0, height // 3)
          )],
        Common.Random.create_random_color_RGB(),
        width // 80
    )
    draw.line(
        [(random.randint(width // 4 * 3, width),
          random.randint(height // 4 * 3, height)
          ),
         (random.randint(width // 3 * 2, width),
          random.randint(0, height // 3)
          )],
        Common.Random.create_random_color_RGB(),
        width // 80
    )
    # im.save('test2.jpg')
    # random color pixel
    for x in range(width):
        for y in range(height):
            col = im.getpixel((x, y))
            if col == (255, 255, 255) or col == (0, 0, 0):
                draw.point((x, y), Common.Random.create_random_color_RGB())
    # im.save('test3.jpg')
    # ImageFilter
    im = im.filter(ImageFilter.BLUR)
    # im.save('test4.jpg')
    im.save(out_path)


if __name__ == '__main__':
    random_str = Common.Random.create_random_num_list(1, 4)[0]
    make_random_num_pic('arial.ttf', random_str, os.path.abspath('.') + '/out.jpg')
