def my_strspn(w1, w2):
    counter = 0
    for c in w1:
        if c in w2:
            counter += 1
        else:
            break
    return counter

# Run the unit tests.

def main():
    s1 = input('Enter string1:  ')
    s2 = input('Enter string2:  ')
    print('Result:  %.0f' % my_strspn(s1, s2))

if __name__ == '__main__':
    main()
