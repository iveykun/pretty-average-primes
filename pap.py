def prime(num):
	if num == 2:
		return True

	elif num == 1 or num == 0 or num%2 == 0:
		return False
	for count in range(3, int(num/2)+1, 2):
		if (num%count) == 0:
			return False
	return True

def generateprimes(goal):
	primes = []
	for x in range(3, goal):
		if prime(x):
			primes.append(x)
	return primes

def search(lst, num):
	if num in lst:
		return True
	else:
		return False
def main():
	print("Input prime number")
	goal = 2*int(input())

	primes = generateprimes(goal)

	x = 0
	while x <= len(primes)-1:
		og = primes[x]
		target = goal - og
		if search(primes, target) == True:
			print(og, target)

		x += 1

main()

