numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime and i > 1:
        primes.append(i)
    else:
        not_primes.append(i)
not_primes.remove(1)
print(f'Primes: {primes}')
print(f'Not primes: {not_primes}')
