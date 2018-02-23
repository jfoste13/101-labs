def my_strspn(w1, w2):
    counter = 0
    for c in w1:
        if c in w2:
            counter += 1
        else:
            break
    return counter
