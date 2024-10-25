import numpy as np
from random import *

a = np.arange(12).reshape((2,6))
a1=['ewr','YniOOOUUnn']
a2=['sdgqg']
print(a1+a2)
print(np.char.add(a1,a2))
print(i*3 for i in a1)
print(np.char.multiply(a1,4))
capitalized_case = np.char.capitalize(a1)
lowered_case = np.char.lower(a1)
uppered_case = np.char.upper(a1)
swapcased_case = np.char.swapcase(a1)
titlecased_case = np.char.title(a1)
print(capitalized_case,lowered_case,uppered_case,swapcased_case,titlecased_case)
centered = np.char.center(a2, 15, fillchar='_')
left = np.char.ljust(a2, 15, fillchar='_')
right = np.char.rjust(a2, 15, fillchar='_')
print(centered, left, right)
x = np.array(['Python', 'PHP', 'JS', 'Examples', 'html5', '5'], dtype=np.str)
print("\nOriginal Array:")
print(x)
r1 = np.char.isdigit(x)
r2 = np.char.islower(x)
r3 = np.char.isupper(x)
print("Digits only =", r1)
print("Lower cases only =", r2)
print("Upper cases only =", r3)
x1 = np.array(['Python', 'PHP', 'JS', 'examples', 'html'], dtype=np.str)
print("\nOriginal Array:")
print(x1)
print("Test if each element of the said array starts with 'P':")
r = np.char.startswith(x1, "P")
print(r)
