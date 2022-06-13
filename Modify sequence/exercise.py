import numpy as np

def workArray(array):
    for i in range(len(array) - 1):
        if array[i] == 0:
            continue
        array[i + 1] -= array[i]
        if(array[i + 1] < 0):
            print("NO")
            return
        array[i] = 0
    print("YES")


nlength = int(input())
array = list(map(int, input().split(' ')))

total = np.sum(array)

if total % 2 != 0 or (nlength < 2 and total != 0):
    print ("NO")
else:
    workArray(array)