#Add all the natural numbers below one thousand that are multiples of 3 or 5.

add = 0

for i in range(1000):
	#print i
	if i%3 == 0:
		add += i
		#print add
		
	if i%5 == 0 and i%3 !=0:
		add += i
		#print i
		#print add
		
print add