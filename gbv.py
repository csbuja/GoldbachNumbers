#Any positive even number is the sum of any two prime numbers.

import math

def isPrime(n):
	if n <=1:
		return False
	c = 2
	while(c<=math.sqrt(n)):
		if n%c==0:
			return False
		c+=1
	return True

def GoldbachNumbers(n):
	if n%2 or n<=0:
		print "Invalid Number"
	#The 4 corner case 
	if n==4:
		print "Input is 4. The Goldbach numbers are 2 and 2."
	f = 3
	while(f <= n/2):
		if isPrime(f) and isPrime(n-f):
			print "Input is " + str(n) + ". The Goldbach numbers are " + str(f) \
			+ " and " + str(n-f) + "."
			return
		f+=1

GoldbachNumbers(12)