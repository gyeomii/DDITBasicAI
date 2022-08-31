def changeInt(a):
    a = 3
    
def changeTuple(a):
    a[0]=3
    
def mytuple():    
    return 1,1

b = 1
bb = mytuple()

print(b)
print(bb)
changeInt(b)
changeTuple(bb)
print(b)
print(bb[0])