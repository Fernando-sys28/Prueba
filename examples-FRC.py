## fernando rivera castillo id 171707

import numpy as np
#from scipy import linalg 
##also we can uncomment the library scipy and then we can run the code without errors
from sympy import *
import pprint as pp


########################### Exercise 1a
A = np.array([[2, -3, 1], [1, -1, 2], [3, 1, -1]])
#print(A)
b = np.array([-1, -3, 9])
#print(b)

x = np.linalg.solve(A,b)
print("the result of x is ",x)

u = np.linalg.solve(A,b) # we use np.linalg to run the code, from the library numpy
print(u)

detA = np.linalg.det(A)
print(detA)

########################### Exercise 2
A = np.array([[1, -1, 4],
              [3, 0, 1],
              [-1, 1, -4]])
b = np.array([-5, 0, 20])

detA = np.linalg.det(A)
print("Determinant of exercise 2",detA)

##x = np.linalg.solve(A, b) ## if we uncomment this line, the code doesn't run because the determinant is equal to 0.
##print(x) ## the matrix is singular 

########################### Exercise 3
A = np.array([[-1, 1, 2],
              [1, 2, 1],
              [-2, -1, 1]])
b = np.array([0, 6, -6])

detA = np.linalg.det(A)
print("determinant of exercise 3: ",detA)

#x = np.linalg.solve(A, b)



########################### Exercise 1b

print('\n Ejemplos con una única solución \n')

print('\n Ejemplo 1. \n')

augmented_A = Matrix([[2, -3, 1, -1],
                      [1, -1, 2, -3],
                      [3, 1, -1, 9]])

print('(A|b)')
pp.pprint(augmented_A)
A_new = augmented_A.rref()[0] #this part of the code, is equal if we use row reduce in wolfram alpha
print('Result:')
pp.pprint(A_new)

########################### Exercise 4

print('\n Ejemplos sin solución\n')

print('\n Ejemplo 2. \n')

augmented_A = Matrix([[1, -1, 4, -5],
                      [3, 0, 1, 0],
                      [-1, 1, -4, 20]])

print('(A|b)', augmented_A)
A_new = augmented_A.rref()[0]
print('Result:', A_new)

print('(A|b)')
pp.pprint(augmented_A)
A_new = augmented_A.rref()[0]
print('Result:')
pp.pprint(A_new)

########################### Exercise 5

print('\n Ejemplos con infinitas soluciones \n')

print('\n Ejemplo 3. \n')

augmented_A = Matrix([[-1, 1, 2, 0],
                      [1, 2, 1, 6],
                      [-2, -1, 1, -6]])

print('(A|b)')
pp.pprint(augmented_A)
A_new = augmented_A.rref()[0]
print('Result:')
pp.pprint(A_new)


########################### Exercise 6 

print('\n Ejemplo de una unica solucion de 6x6 ecuaciones, donde n= 6x7 \n')

augmented_A = Matrix([[1, 2, -1, 3, 0 ,-2, 1],
                      [1 , 0, -2, 1, -3, 3, 2],
                      [3, 2, 1, -4, 5, 1, -2],
                      [0, 2, -2,-4, 3, 1, 3],
                      [0,-2, 1,-5, 4, 3, 0],
                      [6, 4,-2, 1, 0, 3, -3]])

print('(A|b)')
pp.pprint(augmented_A)
A_new = augmented_A.rref()[0]
print('Result:')
pp.pprint(A_new)



########################### Exercise 7

print('\n Modelo cerrado de Leontief. \n')

augmented_A = Matrix([[-0.6, 0.20, 0.20, 0],
                      [0.10, -0.30, 0.20, 0],
                      [0.50, 0.10, -0.40, 0]])

print('(A|b)')
pp.pprint(augmented_A)
A_new = augmented_A.rref()[0]
print('Result:')
pp.pprint(A_new)

'''
########################### Exercise 8

print('\n Problema 1-3. \n')

#augmented_A = Matrix([[], []])

print('(A|b)')
#pp.pprint(augmented_A)
#A_new = augmented_A.rref()[0]
print('Result:')
#pp.pprint(A_new)

########################### Exercise 9

print('\n Problema 2-3. \n')

#augmented_A = Matrix([[],[],[]])

print('(A|b)')
#pp.pprint(augmented_A)
#A_new = augmented_A.rref()[0]
#A_new = A_new.applyfunc(lambda x: round(x,3))
print('Result:')
#pp.pprint(A_new)

########################### Exercise 10

print('\n Problema 3-3. \n')

augmented_A = Matrix([[],[],[],[]])

print('(A|b)')
#pp.pprint(augmented_A)
#A_new = augmented_A.rref()[0]
print('Result:')
#pp.pprint(A_new)
'''