import math

def is_prime(num):
    """
    檢查一個數字是否為質數。
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    # 從 3 開始，只檢查奇數因子，直到 num 的平方根
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def find_primes_up_to(limit):
    """
    找出從 1 到指定上限之間的所有質數。
    """
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

if __name__ == "__main__":
    limit = 100
    prime_numbers = find_primes_up_to(limit)
    print(f"1 到 {limit} 之間的質數有：")
    print(prime_numbers)