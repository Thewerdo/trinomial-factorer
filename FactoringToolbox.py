from math import *

def factor(a, b, c):
  CoEf = getcommonfactors(int(a), int(b), int(c))
  a = int(a) / CoEf
  b = int(b) / CoEf
  c = int(c) / CoEf
  if a < 0: #a always has to be larger than 0
    a *= -1
    b *= -1
    c *= -1
    CoEf *= -1
  return  a, b, c, CoEf

def qaudratic_equation(a, b, c):
  #Checking if there are valid solutions
  rootnumber =  b ** 2 - 4 * a * c 
  rootnumber = 0 if rootnumber < 0 else 2
  return rootnumber

def getabcvalues(trinomal):
  array1 = []
  array2 = []
  array3 = []
  trinomal1 = list(trinomal)
  i = 0 # i is the value of the list that we are currently on
  a = 0 
  b = 0
  c = 0
  digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

  #this finds the value of a
  while trinomal1[i] != "x":
    if trinomal1[i] in digits:
      array1.append(int(trinomal1[i]))
    i += 1
  for j in range (len(array1)):
    array1[j] = 10 ** (len(array1) - (j + 1)) * array1[j]
    a += array1[j]
  #if there is nothing in a, a = 1
  if a == 0:
    a = 1
  #if there is a negative sign on the first value, make a negative
  if trinomal1[0] == "-":
    a *= -1
  i += 6 #(x^2 + )is 6 spaces long

  while trinomal1[i] != "x": #find b
    array2.append(int(trinomal1[i]))
    i += 1
  for j in range(len(array2)):
    array2[j] = 10 ** (len(array2) - (j + 1)) * array2[j]
    b += array2[j]
  #if there is a negative sign, make b negative
  if trinomal1[i - len(array2) - 2] == "-":
    b *= -1
  i += 4 #(x + )is 4 spaces long

  while trinomal1[i] < trinomal[i:]: #find c
    array3.append(int(trinomal1[i]))
    i += 1
  for j in range(len(array3)):
    array3[j] = 10 ** (len(array3) - (j + 1)) * array3[j]
    c += array3[j]
  #Appending the last value because it doesnt work for some reason lol
  c *= 10
  c += int(trinomal1[-1])
  #if there is a negative sign, make c negative
  if trinomal1[i - len(array3) - 2] == "-":
    c *= -1
  return a, b, c

def getcommonfactors(a, b, c):
  #Checking for negatives
  if a < 0:
    a *= -1
  if b < 0:
    b *= -1
  if c < 0:
    c *= -1
  #Finding the GCD of 3 numbers
  d = gcd(a, b)
  e = gcd(c, d)
  return e  

def quadraticFormula(a, b, c): #quadratic formula

  zero_1 = (- 1 * b + sqrt(b**2 - 4*a*c)) / (2 * a)
  zero_2 = (- 1 * b - sqrt(b**2 - 4*a*c)) / (2 * a)
  return (zero_1, zero_2)

def finalFunction (zero_1, zero_2, coef):
  a = 1
  b = 1

  #if any of the values are fractions
  if int(zero_1) != zero_1:
    n = zero_1
    if n < 0:
      n *= -1
    while n > 1:
      n -= 1
    coef1 = 1 / n 
    a = coef1
    zero_1 *= a

  if int(zero_2) != zero_2:
    n = zero_2
    if n < 0:
      n *= -1
    while n > 1:
      n -= 1
    coef2 = 1 / n 
    b = coef2
    zero_2 *= b

  a = round(a, 4)
  b = round(b, 4)
  zero_1 = round(zero_1, 4)
  zero_2 = round(zero_2, 4)
  strzero1 = str(zero_1)
  strzero2 = str(zero_2)
  stra = str(a)
  strb = str(b)
  i = 1
  j = 1
  
  #if any of the values are fractions cont'd, this makes them all integers
  while int(zero_1) != zero_1 or int(a) != a:
    zero_1 *= i
    a *= i

    round(zero_1, 4)
    round(a, 4)
    strzero1 = str(zero_1)
    stra = str(a)
    i += 1

  while int(zero_2) != zero_2 or int(b) != b:
    zero_2 *= j
    b *= j

    round(zero_2, 4)
    round(b, 4)
    strzero2 = str(zero_2)
    strb = str(b)
    j += 1

  #simplify it down
  a = int(a)
  b = int(b)
  zero_1 = int(zero_1)
  zero_2 = int(zero_2)
  i = gcd(a, zero_1)
  j = gcd(b, zero_2)
  a = a/i
  zero_1 /= i
  b /= j
  zero_2 /= j

  #if a or b is one hide it
  if a == 1:
    a = ""
  if b == 1:
    b = ""

  #return the final product
  if zero_1 > 0:
    m = f"({a}x - {zero_1})"
  elif zero_1 < 0:
    m = f"({a}x + {zero_1 * -1})"
  else:
    m = f"{a}x"
  if zero_2 > 0:
    n = f"({b}x - {zero_2})"
  elif zero_2 < 0:
    n = f"({b}x + {zero_2 * -1})"
  else:
    n = f"{b}x"
  if m == n:
    m = m + "^2"
    n = ""
  if coef == 1:
    coef = ""
  return str(coef) + m + n

def factorman(i):
  abc = getabcvalues(i)
  listabc = list(abc)
  a = listabc[0]
  b = listabc[1]
  c = listabc[2] #set a b and c
  
  factored = factor(a, b, c)
  factored2 = list(factored)
  a = factored2[0]
  b = factored2[1]
  c=  factored2[2]
  coef = factored2[3] #factor them down for common factoring

  zeronumber = qaudratic_equation(a, b, c) #all of this is for that last bit
  if zeronumber == 0: #do this before using the formula as sqrt negatives are not possible in python
    if coef == 1:
      print("Can't be factored")
    else:
      print(f"{coef}{abc}")
  else:
    zero1 = sqrt(b ** 2 - 4 * a * c)
    strzero1 = str(zero1)
    if strzero1[-2:] == ".0":
      zero1 = int(zero1)
    if zero1 != int(zero1): #make sure that it is factorable 
      if coef == 1:
        print("Can't be factored")
      else:
        if a == 1:
          a = ""
        if b < 0 and c < 0: #these go thru all the cases if b and c are negative
          print(f"{coef}({a}x^2 - {b}x - {c})")  
        elif b < 0:
          print(f"{coef}({a}x^2 - {b}x + {c})")
        elif c < 0:
          print(f"{coef}({a}x^2 + {b}x - {c})")
        else:
          print(f"{coef}({a}x^2 + {b}x + {c})") 
    else:
      zeros = quadraticFormula(a, b, c)
      zeroes = list(zeros)
      zero1 = zeroes[1]
      zero2 = zeroes[0] #swapped around cause the test cases were a little weird 
      print(finalFunction(zero1, zero2, coef))