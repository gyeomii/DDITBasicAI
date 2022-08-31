f = open("0_0_1_2.psq", 'r')
lines = f.readlines()
for line in lines:
    arr_split = line.split(",")
    mylen = len(arr_split)
    if mylen == 3:
        try:
            i = int(arr_split[0])
            j = int(arr_split[1])
            print(i,j)
        except:
            print("error")
f.close()