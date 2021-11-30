from PIL import Image
from PIL import ImageFilter
import os

TRIGGERED_PATH = 'src/triggered.png'
RED_OVERLAY_PATH = 'src/red_overlay.png'


def get_new_image(base, overlay):
    new_image = Image.new('RGB', base.size, (0, 0, 0, 0))
    new_image.paste(base, (0, 0))
    new_image.paste(overlay, (0, 0), overlay)
    return new_image


def save_result(image, name):
    if not os.path.isdir("output"):
        os.mkdir("output")
    image.save('output/' + name, optimize=True, quality=100)


def trigger(image_path):
    base_image = Image.open(image_path)
    triggered_image = Image.open(TRIGGERED_PATH)
    red_overlay = Image.open(RED_OVERLAY_PATH)

    base_image = base_image.resize(triggered_image.size)
    base_image = base_image.filter(ImageFilter.DETAIL)

    new_image = get_new_image(base_image, red_overlay)
    new_image = get_new_image(new_image, triggered_image)

    save_result(new_image, os.path.basename(image_path))
