import random


def random_array(length):
    result = []
    for i in range(length):
        result.append(random.randint(0, 100))
    return result


print(random_array(7))
