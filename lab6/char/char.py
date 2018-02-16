def is_lower_101(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    return False

def char_rot_13(c):
    new_val = 0
    if ord(c) >= 97 and ord(c) <= 122:
        if ord(c) + 13 > 122:
            new_val = 97 + (ord(c) + 13) - 123
        else:
            new_val = ord(c) + 13


    elif ord(c) >= 65 and ord(c) <= 90:
        if ord(c) + 13 > 90:
            new_val = 65 + (ord(c) + 13) - 91
        else:
            new_val = ord(c) + 13
    return chr(new_val)
