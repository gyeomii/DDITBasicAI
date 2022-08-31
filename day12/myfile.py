f = open("0_0_1_2.psq", 'r')
lines = f.readlines()
for line in lines:
    print(line,end="")
f.close()