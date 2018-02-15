def sum(lon):
    list_sum = 0
    for val in lon:
        list_sum += val
    return list_sum
def index_of_smallest(lon):
    if not lon:
        index = -1
    else:
        index = 0
    for i in range(len(lon)):
        if lon[i] < lon[index]:
            index = i
    return index
