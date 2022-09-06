import os
from shutil import copyfile

folders = os.listdir("test")
for folder in folders:
    files = os.listdir(f"test/{folder}")
    for idx,file in enumerate(files):
        copyfile(f"test/{folder}/{file}", f"test_eng/{folder}/{idx}.png")