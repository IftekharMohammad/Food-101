from PIL import Image
import os
from pathlib import Path
import random


def image_resizer():
    path = os.path.dirname(os.path.realpath(__file__))
    for root, dirs, files in os.walk(path):
        for filename in files:
            if filename.endswith(".py") or filename.endswith(".txt") or filename.endswith(".json") \
                    or filename.endswith(".csv"):
                continue
            image_location = os.path.join(root, filename).replace("\\", "/")
            resize_image(image_location, image_location, 512)


def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    print('The original image is {path}'.format(path=input_image_path))
    size = size, size
    resized_image = original_image.resize(size)
    resized_image.save(output_image_path)
    print('The resized image Saved in: {path}'.format(path=output_image_path))


if __name__ == '__main__':
    image_resizer()
