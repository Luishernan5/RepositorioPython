from sympy import symbols,Eq,solve
c1,c2,c3=symbols('c1 c2 c3')
e1 = Eq(c1+0*c2+2*c3,1)
e2 = Eq(0*c1-c2+3*c3, 2)
e3 = Eq(c1+2*c2-5*c3,-1)
resultado1=solve((e1,e2, e3),(c1, c2, c3))
print (resultado1)