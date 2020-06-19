import random

def generate(num):
    arr = [[999999]*num]*num
    for i in range(num):
        for j in range(num):
            if i==j:
                continue
            else:
                val = random.randint(1, 200)
                arr[i][j] = val
                arr[j][i] = val
    arr[0][num-1] = 999999999
    print(arr)
    return arr

