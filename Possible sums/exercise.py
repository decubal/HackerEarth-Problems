
def getPossibleSums(array):
    if(len(array) == 1):
        return {array[0]}
    
    futureArray = getPossibleSums(array[1:])

    return set(map(lambda x: x + array[0], futureArray)).union(futureArray, {array[0]})


ntestCases = int(input())

for i in range(ntestCases):
    arraySize = int(input())
    array = list(map(int, input().split(' ')))

    sumsSet = getPossibleSums(array)

    if(0 in sumsSet):
        print(len(sumsSet))
    else:
        print(len(sumsSet) + 1) #add 0