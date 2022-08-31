import numpy as np

arr =[ 
        [1,2,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [0,0,0,0,0]
]

arr_n = np.array(arr)
arr_n90 =  np.rot90(arr_n)
arr_n180 =  np.rot90(arr_n90)
arr_n270 =  np.rot90(arr_n180)


arr_n_lr =  np.fliplr(arr_n)
arr_n90_lr =  np.fliplr(arr_n90)
arr_n180_lr =  np.fliplr(arr_n180)
arr_n270_lr =  np.fliplr(arr_n270)

print(arr_n)
print(arr_n90)
print(arr_n180)
print(arr_n270)

print(arr_n_lr)
print(arr_n90_lr)
print(arr_n180_lr)
print(arr_n270_lr)

