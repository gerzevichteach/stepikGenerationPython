def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

def get_next_prime(num):
    next_num = num + 1
    while not(is_prime(next_num)):
        next_num += 1
    return next_num

n = int(input())

print(get_next_prime(n))