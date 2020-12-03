input = 20

def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

is_prime_list=[]
def find_prime_list_under_number(number):
    for i in range (2,number+1):
        if is_prime(i):
            is_prime_list.append(i)
    return is_prime_list


result = find_prime_list_under_number(input)
print(result)