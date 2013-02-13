# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt
prime = 600851475143

i = int(sqrt(prime))
number = 2
divisibles = []

while number<i:
	if prime%number != 0:
		number += 1
	else:
		#print number
		divisibles.append(prime/number)
		divisibles.append(number)
		number += 1

print divisibles


def prime(number):
	rangemax = int(sqrt(number))
	for x in range(2, rangemax):
		if number % x == 0:
			return 1
	return number

primes = []
for i in divisibles:
	primecheck = prime(i)
	primes.append(primecheck)

m = max(primes)
print m	

			


		