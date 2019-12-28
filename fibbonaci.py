# Recursividade

'''
3! = 3 * 2 * 1 = 6

fat(3)
	3 * fat(2) => 3 * 2 = 6
	fat(2)
		2 * fat(1) => 2 * 1 = 2
		fat(1)
			1 * fat(0) => 1 * 1 = 1
			fat(0) --> 1
'''
# Fibbonaci
def fat(n):
	if n == 0:
		return 1
	return n * fat(n-1)
