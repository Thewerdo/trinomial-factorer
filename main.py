#This program uses special functions to factor quadratic equations/trinomials. It only accepts integers as values for a, b, and c.

from FactoringToolbox import*

equations = ["x^2 + 18x + 32", "x^2 + 17x + 32", "x^2 - 16x + 63", "x^2 + 5x - 24", "x^2 - 5x - 24", "x^2 + 0x - 9", "x^2 + 0x - 10", "x^2 - 0x + 9", "2x^2 + 11x + 5", "12x^2 - 7x - 10", "87x^2 - 29x + 143", "9x^2 - 0x - 100", "9x^2 + 0x + 1", "3x^2 + 12x + 6", "2x^2 + 10x + 8", "5x^2 + 0x - 500", "x^2 + 7x - 0", "-10x^2 + 5x - 0"] 

for i in range (len(equations)):
  factorman(equations[i])