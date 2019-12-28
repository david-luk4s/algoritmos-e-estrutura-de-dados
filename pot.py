lista = [x for x in range(5)]
lista.sort()
lista.reverse()

def pot(base, exp):
	if exp == 0:
		return 1
	return base * pot(base, exp - 1)
