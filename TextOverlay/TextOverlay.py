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
    image = Image.open(src_dir + img_name + str(idx_beg) + postfix)
    width, height = image.size

    # resize canvas
    nof_canvas = len(texts)
    x_gap = 200  # x gap between canvas
    canvas_width = int((width - x_gap) / nof_canvas - x_gap)

    y_ratio = 0.3  # y percentage of the table area
    y_gap = 200  # y gap between canvas
    canvas_height = int(height * y_ratio - y_gap * 2)

    color = (255, 255, 255)
    font_size = 150
    font = ImageFont.truetype('assets/PersonnBold-x3l4R.ttf', font_size)

    corner_width = 50
    corner_raius = 200

    for idx in range(idx_beg, idx_end, 1):
        x_canvas = int(x_gap)
        y_canvas = int(height * (1 - y_ratio) + y_gap)

        x_text_gap = 150
        y_text_gap = 150
        y_text = 150
        image = Image.open(src_dir + img_name + str(idx) + postfix)
        for j in range(0, nof_canvas, 1):
            image_draw = ImageDraw.Draw(image)
            image_draw.rounded_rectangle((x_canvas, y_canvas, x_canvas + canvas_width, y_canvas + canvas_height),
                            fill="black", outline="grey", width=corner_width, radius=corner_raius)
            text_pos_x = x_canvas + x_text_gap
            text_pos_y = y_canvas + y_text_gap
            for text in texts[j]:
                image_draw.text((text_pos_x, text_pos_y), text, font=font, fill=color)
                text_pos_y += y_text

            x_canvas += canvas_width + x_gap
        image.save(dest_dir + img_name + str(idx) + postfix)
        image.close()
    canvas.close()