import driver

def letter(col, row):
    if col != 9:
        return 'G'
    elif col == 9:
        if row == 9:
            return 'Z'
        else:
            return 'G'


if __name__ == '__main__':
    driver.comparePatterns(letter)
