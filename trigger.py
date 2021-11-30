from PIL import Image
import os

TRIGGERED_PATH = 'src/triggered.png'
TRIGGERED_HEIGHT = 60


def get_new_image(base, overlay):
    new_image = Image.new('RGB', base.size, (0, 0, 0, 0))
    new_image.paste(base, (0, 0))
    new_image.paste(overlay, (0, 0), overlay)
    return new_image


def save_result(image, name):
    image.save('output/' + name, optimize=True, quality=100)


def trigger(image_path):
    base_image = Image.open(image_path)
    triggered_image = Image.open(TRIGGERED_PATH)

    base_image = base_image.resize(triggered_image.size)

    new_image = get_new_image(base_image, triggered_image)

    save_result(new_image, os.path.basename(image_path))


path = input('Enter the path to the image:')
trigger(path)
