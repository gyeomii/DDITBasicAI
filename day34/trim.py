import numpy as np

def cutMute(arr_n):
    idx_f = 0
    while True:
        if arr_n[idx_f] <= 0.1:
            pass
        else :
            break
        idx_f += 1
    
    idx_f -= 10
    
    idx_l = len(arr_n) - 1
    while True:
        if arr_n[idx_l] <= 0.1:
            pass
        else : 
            break
        idx_l -= 1
    
    idx_l += 10
    
    
    return arr_n[idx_f: idx_l]