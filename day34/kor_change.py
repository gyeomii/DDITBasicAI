import os
from shutil import copyfile

folders = os.listdir("train")
for folder in folders:
    files = os.listdir(f"train/{folder}")
    for idx,file in enumerate(files):
        copyfile(f"train/{folder}/{file}", f"train_eng/{folder}/{idx}.png")