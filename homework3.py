import csv
import json
import os
import pickle
import shutil
import numpy as np

if not os.path.isdir(r"C:\Users\Legendalf\Downloads\hw3"):
     os.mkdir(r"C:\Users\Legendalf\Downloads\hw3")
os.chdir("hw3")

file = open("file.txt", "w")
file.write("Do you believe in Heaven above?\nDo you believe in love?\nDon't tell a lie, don't be false or untrue\nIt all comes back to you")     
file.close()

json_string = """
{
    "movies": [
        {
            "name": "Полночь в Париже",
            "release_year": 2011,
            "director": "Вуди Аллен"
        },
        {
            "name": "Гравити Фолз",
            "release_year": 2012,
            "creator": "Алекс Хирш"
        },
        {
            "name": "Окно во двор",
            "release_year": 1954,
            "director": "Альфред Хичкок"
        }
    ]
}
"""
movies = json.loads(json_string)
with open("file.json", "w") as out:
    json.dump(movies, out, indent=4, ensure_ascii=False)

cancerdata = [
            ["Cancer Type","D-Loop","mRNAs","tRNAs","rRNAs","Nucleotide Position of Deletions","Increase of mtDNA copy #","Decrease of mtDNA copy #"],
            ["Bladder","1","1","0","1","15642-15662","0","0"],
            ["Breast","1","1","1","1","8470-13447 and 8482-13459","0","1"],
            ["Oral","1","1","0","0","8470-13447 and 8482-13459","0","0"]
            ]
with open("file.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(cancerdata)
        
if not os.path.isdir(r"C:\Users\Legendalf\Downloads\hw3\folder"):
     os.mkdir(r"C:\Users\Legendalf\Downloads\hw3\folder")

path = r"C:\Users\Legendalf\Downloads\hw3"
from os import listdir
from os.path import isfile, join
files = [f for f in listdir(path) if isfile(join(path, f))]
files.sort(key=lambda x: os.path.getctime(x))
files.reverse()
print(' '.join(files))

os.chdir(r"C:\Users\Legendalf\Downloads")
shutil.rmtree("hw3")
