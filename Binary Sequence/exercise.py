ntestCases = int(input())

for i in range(ntestCases):
    array = list(map(int, input().split(' ')))
    if array[0]*array[1] == array[2] + array[3]:
        print("Yes")
    else:
        print("No")