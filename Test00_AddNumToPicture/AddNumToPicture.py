from PIL import Image, ImageDraw, ImageFont


def addNum(im):
    font = ImageFont.truetype("arial.ttf", 36)
    fillcolor = "#ff0000"
    width, height = im.size
    draw = ImageDraw.Draw(im)
    draw.text((width - 40, 0), "99", font=font, fill=fillcolor)
    im.save("result.jpg", "jpeg")


if __name__ == '__main__':
    image = Image.open('haha.jpg')
    addNum(image)