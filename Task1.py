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


def non_divisors(n):
    list = []
    for i in range(1, n):
        if n % i != 0:
            list.append(i)
    return list


def prime_divisors(n):
    list = []
    for i in divisors(n):
        if prime_divisor(i):
            list.append(i)
    return list


def non_prime_divisors(n):
    list = []
    for i in divisors(n):
        if not(prime_divisor(i)):
            list.append(i)
    return list


def digits(n):
    list = []
    while n > 0:
        list.append(n % 10)
        n //= 10
    return list


def func1(n):
    summ = 0
    for i in non_prime_divisors(n):
        summ += i
    return summ


def func2(n):
    amount = 0
    for i in digits(n):
        if i < 3:
            amount += 1
    return amount


def mutually_prime(n1, n2):
    return n1 * (1/n2) == 1


def func3(n):
    summ = sum(digits(n))
    amount = 0
    for i in non_divisors(n):
        if not(mutually_prime(n, i)):
            if mutually_prime(i, summ):
                amount += 1
    return amount


print('Amount of numbers that are not divisors of the original number,\n'
      'are not mutually prime with it,\n'
      'and are mutually prime with the sum of the prime digits of this number: ',
      func3(int(input('Provide a number: '))))
