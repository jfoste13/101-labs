def are_positive(inputList):
    return [n for n in inputList if n > 0]
def are_greater_than_n(inputList, n):
    returnList = []
    for i in range(len(inputList)):
        if inputList[i] > n:
            returnList.append(inputList[i])
    return returnList
def are_divisible_by_n(inputList, n):
    returnList = []
    counter = 0
    while counter < len(inputList):
        if inputList[counter] % n == 0:
            returnList.append(inputList[counter])
        counter += 1
    return returnList
