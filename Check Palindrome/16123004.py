def is_palindrome(c):
	j=''
	for o in c:
		j=o+j
	if(j==c):
		print("Its a palindrome")
	else: 
		print("Its not a palindrome")

		
is_palindrome('racecar')
is_palindrome('poppy')
		
