"""
Created on Wed Aug 17 13:42:14 2022
Álvaro Fernando Oros Ramírez 171621
Angel Moreno Lozano 171829
Zauriel Jesus Espejel Cervantes 171888
Diego Garcia Aldaco 170908
Kitzia Ximena Carranza Alvarez 170732
@author: Equipo 8
"""
import numpy as np
from sympy.abc import x
from sympy import lambdify
#from sympy import *
#from sympy.parsing.sympy_parser import parse_expr

################################# Bisection method
def my_bisection(f,a,b,tol):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("The scalar a and b do not bound a root")
            
    m=(a + b)/2
        
    if np.abs(f(m)) < tol:
        return m
    elif np.sign(f(a))== np.sign (f(m)):
        return my_bisection(f, m, b, tol)
    elif np.sign(f(b))==np.sign(f(m)):
        return my_bisection(f, a, m, tol)
            
################################## Modified Newton
def newtonMod(f,Df,D2f,x0,epsilon,max_iter):
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        D2fxn = D2f(xn)
        
        den = Dfxn**2 - fxn * D2fxn
        
        if den == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - (fxn * Dfxn)/den
    print('Exceeded maximum iterations. No solution found.')
    return None

def newton(f,Df,x0,epsilon,max_iter):
  
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None

print("This program solves equations like the next form, f(x)=0 with bisection method, Newton y Newton modified \n")

   
ans=True
while ans:
  
    print("""\n Which option would like to try
    1. Bisection method
    2. Newton method
    3. Modified Newton method
    4.Exit/Quit
    """)
    ans = input("Type here your option:")
    if ans=="1":
############################## Example  Bisection Method
        valueABisection = int(input("You choosed the Bisección method, in order to resolve it you need to provide some parameters.Type the left end of the interval, value of a: "))
        valueBBisection = int(input("Type the right end of interval (a,b), in fact, give the value of b: "))
        toleranceBisection = float(input("Type the tolerance: "))
        function = input("Give the function:")
        f = lambdify(x,function) 

        root = my_bisection(f, valueABisection, valueBBisection, toleranceBisection)
        print("The equation have an x solution equal to: ", root)
        print("f(root)=", f(root))
      
    elif ans=="2":
        ################################# Example Newton Method
        x0 = float(input("You choosed the Newtoon method, in order to resolve it you need to provide some parameters.Type x0: "))
        epsilon = float(input("Give the stopping criteria : "))
        max_iter = int(input("Type the max iteration: "))
        f = lambdify(x,input("Give me the function: "))
        f_prime = lambdify(x,input("Give me the first derivative: "))
        
        estimate = newton(f, f_prime, x0, epsilon, max_iter)
        
        print("estimate = ", estimate)
      
    elif ans=="3":
        
        x0 = float(input("You choosed the Modified Newtoon method, in order to resolve it you need to provide some parameters, give the x0 (Initial guess for a solution f(x)=0): "))  
        epsilon = float(input("give the stopping criteria : "))
        f = lambdify(x,input("Give the function: "))
        Df = lambdify(x,input("give the first derivative: ")) 
        D2f = lambdify(x,input("give the second derivative: "))   
      
        
           
        estimate = newtonMod(f, Df, D2f, x0, epsilon, 100)
      
        print("estimate = ", estimate)
  
    elif ans=="4":
        print("\n Goodbye") 
        ans = None
    else:
        print("\n Not valid choice Try again")


