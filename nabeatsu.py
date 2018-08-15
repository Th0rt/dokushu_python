def nabeatsu(num):
    if int(num) % 3 == 0:
        return('aho')
    elif '3' in str(num):
        return('aho')
    return(num)


num = int(input('数字を入力してください'))

print(nabeatsu(num))
