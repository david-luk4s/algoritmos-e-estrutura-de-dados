import unittest

def pot(base, exp):
	if exp == 0: return 1
	return base * pot(base, exp - 1)

def fat(n):
	if n == 1: return 1
	return n * fat(n-1)

def area_quad(side):
	return side * side


class MathTestFunctions(unittest.TestCase):

	def testPot(self):
		self.assertEqual(1024, pot(2, 10))

	def testFat(self):
		self.assertEqual(120, fat(5))

	def testQuad(self):
		self.assertEqual(25, area_quad(5))

unittest.main()