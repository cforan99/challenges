var primes = [2, 3];
var total = 5;
var is_prime = true;

for (var i = 4; primes.length < 10; i++) {
  for (var p in primes) {
    if (i % primes[p] == 0) {
      is_prime = false;
      break;
    } else {
      is_prime = true;
    }
  }
  if (is_prime) {
    primes.push(i);
    total += i;
  }
}