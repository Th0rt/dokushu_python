def compare_string(a, b):
    if len(a) > len(b):
        return a
    else:
        return b


str1 = 'aaa'
str2 = 'bbbb'

print(compare_string(str1, str2))
