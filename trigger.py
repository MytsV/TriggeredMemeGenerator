from PIL import Image

TRIGGERED_PATH = 'src/triggered.png'
TRIGGERED_HEIGHT = 60;

def trigger(image_path):
    base_image = Image.open(image_path)
    triggered_image = Image.open(TRIGGERED_PATH)

    base_image = base_image.resize(triggered_image.size)
    triggered_pos = (0, triggered_image.size - TRIGGERED_HEIGHT)

