def print_primes():
    primes = [2, 3]
    i = 4
    while len(primes) < 1000:
        for p in primes:
            if i%p == 0:
                break
            if p == primes[-1]:
                primes.append(i)
        i += 1
    return sum(primes)

sys.stdout.write(str(print_primes()))