import map

def square_all(inputList):
    return [inputList[i]**2 for i in range(len(inputList))]

def add_n_all(inputList, increment):
    for i in range(len(inputList)):
        inputList[i] = inputList[i] + increment
    return inputList

def even_or_odd_all(inputList):
    counter = 0
    while counter < len(inputList):
        if inputList[counter] % 2 == 0:
            inputList[counter] = True
        else:
            inputList[counter] = False
        counter += 1
    return inputList
