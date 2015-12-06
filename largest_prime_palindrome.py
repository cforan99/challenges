def palindrome(num):
    string = str(num)
    i = 0
    while i < len(string)-1:
        end = string[-1]
        if string[i] != end:
            return False
        else:
            string = string[:-1]
            i += 1
    return True

def print_primes():
    primes = [2, 3]
    for i in range(4, 1001):
        for p in primes:
            if i%p == 0:
                break
            if p == primes[-1]:
                primes.append(i)
    return primes

def print_lpp():
    primes = print_primes()
    lpp = 0
    for p in primes:
        if palindrome(p):
            lpp = p
    return lpp
    
print_lpp()