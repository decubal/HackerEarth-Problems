# import concurrent.futures

def isPalindrome(s):
    if(s in existingPalindromes):
        return False
    length = len(s)
    j = length - 1
    for i in range(length):
        if(i >= j):
            existingPalindromes.append(s)
            return True
        if(s[i] != s[j]):
            return False
        j -= 1


def getNumberPalindromes2(stringS):
    result = 0
    i = 0
    j = 2
    while(j < len(stringS)):
        for i in range(len(stringS) - j + 1):
            if(isPalindrome(stringS[i:j+i])):
                result += 1
        j += 1
    
    return result + len(stringS)

# def getNumberPalindromes(stringS):
#     result = 0
#     if len(stringS) <= 1:
#         return result

#     if isPalindrome(stringS):
#         result += 1
    
#     # with concurrent.futures.ThreadPoolExecutor() as executor:
#     #     future1 = executor.submit(getNumberPalindromes, stringS[:-1])
#     #     future2 = executor.submit(getNumberPalindromes, stringS[1:])
#     #     return_value1 = future1.result()
#     #     return_value2 = future2.result()

#     result += getNumberPalindromes(stringS[:-1])
#     result += getNumberPalindromes(stringS[1:])

#     # result += return_value1 + return_value2

#     return result



stringS = input()
existingPalindromes = []
print(getNumberPalindromes2(stringS))
