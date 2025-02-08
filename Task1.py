def prime_divisor(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def divisors(n):
    list = []
    for i in range(1, n+1):
        if n % i == 0:
            list.append(i)
    return list


def non_prime_divisors(n):
    list = []
    for i in divisors(n):
        if not(prime_divisor(i)):
            list.append(i)
    return list


def func1(n):
    summ = 0
    for i in non_prime_divisors(n):
        summ += i
    return summ


print('Sum of non prime divisors: ', func1(int(input('Provide a number: '))))
