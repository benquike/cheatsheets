# Prime Number

## Definition

A prime number is a natural number greater than 1 that has no other
divisors other than 1 and itself.[^1]

The property of being prime is called primality.

## Coprime integers

Two numbers are called `coprime` if the `greatest commond divisor`[^3]
is 1[^2].


### Important properties of Prime Numbers

1. two prime numbers are coprime
2. if a number is a prime, all numbers that are not multiple of it are its coprime number
3. for all number n, n+1 is its coprime number
4. for all `odd` number n, n+2 is its coprime number


## Euler's work

### Euler's function

	For all number n, the number of numbers that are less than n and are coprime
	of n is called Euler's function, denoted by phi(n).[^4]

	Assuming that k1, k2, ..., km are prime numbers that are factors of n, then
	phi(n) = n (1 - 1/k1) (1 - 1/k2) ... (1 - 1/k3)

### Euler's theory

	if a and n are coprime, then

	(a^phi(n)) % n == 1

[^1]: https://en.wikipedia.org/wiki/Prime_number
[^2]: https://en.wikipedia.org/wiki/Coprime_integers
[^3]: https://en.wikipedia.org/wiki/Greatest_common_divisor
[^4]: http://www.ruanyifeng.com/blog/2013/06/rsa_algorithm_part_one.html
