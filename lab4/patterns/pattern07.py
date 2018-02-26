import driver

def letter(row, col):
    if row <= 5:
        if (col >= 7 and col <= 9) and (row == 5 or row == 4):
            return 'X'
        elif (col >= 4 and col <= 9) and (row >= 2 and row <= 5):
            return 'Z'
        elif (col >= 10 and col <= 12) and (row == 4 or row == 5):
            return 'B'
        else:
            return 'T'
    else:
        if (col >= 7 and col <= 12) and row == 6:
            return 'B'
        else:
            return 'T'



if __name__ == '__main__':
    driver.comparePatterns(letter)
