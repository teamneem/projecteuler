#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from math import sqrt
numberlist= []

def prime(number):
	rangemax = int(sqrt(number))
	for x in range(2, rangemax+1):
		if number % x == 0:
			return 1
	return number
	
for x in range(2, 21):
	primenumber = prime(x)
	numberlist.append(primenumber)
#print numberlist

redundant = []
for x in numberlist:
	for y in numberlist:
		if x != y and x*y<21:
			redundant.append(x*y)	
#print redundant
redundant = set(redundant)
redundant = list(redundant)
print redundant
			
othernumbers = []
for x in range(1, 21):
	if x in numberlist:
		continue
	if x in redundant:
		continue
	else:
		othernumbers.append(x)
print othernumbers
print numberlist
numberlist2 = numberlist


for x in othernumbers:
	for y in numberlist:
		if x*y in othernumbers:
			#print y
			if x in othernumbers:
				othernumbers.remove(x)
			continue
		else:
			numberlist2.append(x)
			continue
			#print x


total = 1
for num in numberlist2:
	total = num * total
print total



