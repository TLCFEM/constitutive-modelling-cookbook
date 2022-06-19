import sympy as sym
from sympy import Matrix
from sympy import Array
from sympy import latex
from sympy import shape, eye, diag

s11 = sym.Symbol('s11')
s22 = sym.Symbol('s22')
s33 = sym.Symbol('s33')
s12 = sym.Symbol('s12')
s23 = sym.Symbol('s23')
s31 = sym.Symbol('s31')

# s = Matrix([[s11], [s22], [s33], [s12], [s23], [s31]])
s = Array([s11, s22, s33, s12, s23, s31])
norm = sym.sqrt(s11**2+s22**2+s33**2+2*s12**2+2*s23**2+2*s31**2)
n = s/norm

dnds = sym.diff(n, s)
sdnds = sym.simplify((dnds*norm**3).tomatrix()-eye(6)*norm**2).transpose()
print(latex(sdnds))
