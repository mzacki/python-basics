from sympy import simplify, symbols, pprint

r, r1, r2, v, i1, i2 = symbols("r r1 r2 v i1 i2")
i1 = v / r1
i2 = v / r2
r = v / (i1 + i2)
pprint(simplify(r))
