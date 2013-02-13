def palindrome(number):
	number = str(number)
	start = 0
	end = -1
	
	if len(number)%2 == 0:
		middle = len(number)/2
	else:
		middle = int(len(number)/2) + 1	
	while number[start] == number[end]:
		start +=1
		end -=1
		if start == middle:
			return int(number)
	else:
		return 1


palindromes = []
for x in range(100, 999):
	for y in range(100, 999):
		product = x*y
		ispalindrome = palindrome(product)
		if ispalindrome != 1:
			palindromes.append(ispalindrome)
		
print palindromes
maxpal = max(palindromes)
print maxpal
		
		

			