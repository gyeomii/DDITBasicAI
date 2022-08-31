
arr = [0,1,3,1,1, 1,2,2,2,2]

max = -1
for i in arr:
    if max < i:
        max = i
        
print("max",max)

myidx = -1

for idx,i in enumerate(arr):
    if max == i:
        myidx = idx
        
print("myidx",myidx)
# 2