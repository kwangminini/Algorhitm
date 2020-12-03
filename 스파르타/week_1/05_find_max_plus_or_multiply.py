input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    max_num=0
    for i in array:
        if i <= 1 or max_num <=1:
            max_num+=i
        else:
            max_num*=i
    return max_num


result = find_max_plus_or_multiply(input)
print(result)