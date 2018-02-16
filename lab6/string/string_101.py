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
    else:
        new_val = ord(c)
    return chr(new_val)

def str_rot_13(s):
    return ''.join([char_rot_13(c) for c in s])

def str_translate_101(s, old, new):
    new_string_list = []
    for char in s:
        if char == old:
            new_string_list.append(new)
        else:
            new_string_list.append(char)
    return ''.join(new_string_list)
