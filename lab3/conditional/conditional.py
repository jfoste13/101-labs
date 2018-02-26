def max_101(n1, n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return n1

def max_of_three(f1, f2, f3):
    if f1 > f2 and f1 > f3:
        return f1
    elif f2 > f1 and f2 > f3:
        return f2
    elif f3 > f1 and f3 > f2:
        return f3
    else:
        return f1

def rental_late_fee(days):
    if days <= 0:
        return 0
    elif days <= 9:
        return 5
    elif days <= 17:
        return 7
    elif days <= 24:
        return 19
    elif days > 24:
        return 100
