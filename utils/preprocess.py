from PIL import Image
import os
import random
import csv
from pathlib import Path
from colorama import Fore, init

init()


def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    size = size, size
    resized_image = original_image.resize(size)
    resized_image.save(output_image_path)


def image_resizer():
    path = os.path.dirname(os.path.realpath(__file__))
    for root, dirs, files in os.walk(path):
        for filename in files:
            if filename.endswith(".py") or filename.endswith(".txt") or filename.endswith(".json") \
                    or filename.endswith(".csv"):
                continue
            image_location = os.path.join(root, filename).replace("\\", "/")
            resize_image(image_location, image_location, 512)


def rename():
    dir_path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
    for filename in os.listdir(dir_path):
        i = 0
        if filename.endswith(".py"):
            continue
        for files in os.listdir(filename):
            if files.endswith(".py"):
                continue
            else:
                # dst = filename + "(" + str(i) + ").jpg"
                dst = "abc" + "(" + str(i) + ").jpg"
                src = dir_path + "/" + filename + "/" + files
                dst = dir_path + "/" + filename + "/" + dst
                os.rename(src, dst)
                i += 1


def csvCreator():
    path = os.path.dirname(os.path.realpath(__file__))

    with open('train.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['image_location', 'label', 'weight'])
        for root, dirs, files in os.walk(path):
            for filename in files:
                if filename.endswith(".py") or filename.endswith(".csv"):
                    pass
                else:
                    image_location = os.path.join(root, filename).split("\\", 3)[3].replace("\\", "/")
                    label = os.path.join(root, filename).split("\\", 4)[3]
                    writer.writerow(["./" + image_location, label, random.uniform(0, 1)])


def preprocess():
    print(Fore.CYAN + "************ Resizing Dataset Images ************")
    # image_resizer()
    print(Fore.GREEN + "************ Resizing Dataset Images Done ************")
    print(Fore.CYAN + "************ Renaming Dataset Images ************")
    rename()
    print(Fore.GREEN + "************ Renaming Dataset Images Done ************")
    print(Fore.CYAN + "************ Creating Dataset CSV ************")
    csvCreator()
    print(Fore.GREEN + "************ Creating Dataset CSV Done ************")


if __name__ == '__main__':
    preprocess()
