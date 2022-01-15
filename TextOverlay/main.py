import sys
from PIL import Image, ImageDraw, ImageFont


def add_text_to_img(texts):
    src_dir = 'assets/'
    dest_dir = 'results/'
    img_name = 'hdimage'
    postfix = '.png'
    idx_beg = 31
    idx_end = 162
    images = []
    canvas = Image.open(src_dir + 'canvas.png')
    image = Image.open(src_dir + img_name + str(idx_beg) + postfix)
    width, height = image.size

    # resize canvas
    nof_canvas = len(texts)
    x_gap = 150  # x gap between canvas
    canvas_width = int((width - x_gap) / nof_canvas - x_gap)

    y_ratio = 0.3  # y percentage of the table area
    y_gap = 300  # y gap between canvas
    canvas_height = int(height * y_ratio - y_gap * 2)

    canvas = canvas.resize((canvas_width, canvas_height), Image.ANTIALIAS)
    x_canvas = int(x_gap)
    y_canvas = int(height * (1 - y_ratio) + y_gap)

    x_text_gap = 200
    y_text_gap = 200
    y_text = 150
    color = (255, 255, 255)
    font_size = 120
    font = ImageFont.truetype('assets/PersonnBold-x3l4R.ttf', font_size)

    for idx in range(idx_beg, idx_end, 1):
        image = Image.open(src_dir + img_name + str(idx) + postfix)
        for j in range(0, nof_canvas, 1):
            image.paste(canvas, (x_canvas, y_canvas))

            image_draw = ImageDraw.Draw(image)
            text_pos_x = x_canvas + x_text_gap
            text_pos_y = y_canvas + y_text_gap
            for text in texts[j]:
                image_draw.text((text_pos_x, text_pos_y), text, font=font, fill=color)
                text_pos_y += y_text

            x_canvas += canvas_width + x_gap
        image.save(dest_dir + img_name + str(idx) + postfix)
        image.close()
    canvas.close()


if __name__ == '__main__':
    test_texts = (("area: 21 chunks", "land coverage: 87.2%"),
                  ("diamond: 2.19%", "gold: 3.14%"),
                  ("fossil", "mineshaft", "temple"))
    add_text_to_img(test_texts)
