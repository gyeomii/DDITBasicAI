import os

for i in range(100,123):
    mystr = str(i)[1:3]
    os.makedirs("image/"+mystr)