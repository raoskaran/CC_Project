import json, os
from pprint import pprint
import csv

cwd = os.getcwd()
coords = {}
csvdata = []
with open('coords.json', 'rb') as f:
    coords = json.load(f)


for filename in os.listdir(cwd):
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".JPG") or filename.endswith(".jpeg") or filename.endswith(".tiff") or filename.endswith(".bmp"):
                    # print(os.path.splitext(filename)[0].split()[1])
                    for key, value in coords.items():
                        if os.path.splitext(filename)[0].split()[1] == value.split()[2].encode("ascii"):
                            csvdata.append([filename, value.split()[0].encode("ascii"), value.split()[1].encode("ascii"), value.split()[2].encode("ascii")])

pprint(csvdata)
with open('table.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(csvdata)