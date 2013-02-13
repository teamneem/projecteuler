# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

list = [1, 2]

while list[-1] < 4000000:
	list.append(list[-1] + list[-2])
	
print list

even_sum = 0
for i in list:
	if i%2 == 0:
		even_sum += i
		
print even_sum