import os
import csv
from pathlib import Path
import random

path = os.path.dirname(os.path.realpath(__file__))

with open('train.csv', 'w', newline='') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['image_location', 'label', 'weight'])
	for root, dirs, files in os.walk(path):
		for filename in files:
			if filename.endswith(".py") or filename.endswith(".csv"):
				pass
			else:
				image_location = os.path.join(root, filename).split("\\",3)[3].replace("\\", "/")
				label = os.path.join(root,filename).split("\\", 4)[3]
				writer.writerow(["./" + image_location, label, random.uniform(0, 1)])
