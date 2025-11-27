# vim: set ts=2 sw=2 et ai si:
import random as r
import math as m
r.seed(1)

# At probability p, for each decision a.k ∈ a, 
# then mew.k = a.k ∨ (p1 < rand() ∧ (b.k ∨ c.k )).
def de(f, n=20, d=2, cr=0.9, F=0.8, iters=100, lo=-5, hi=5):
  pop = [[r.uniform(lo,hi) for _ in range(d)] for _ in range(n)]
  for _ in range(iters):
    for i in range(n):
      a,b,c = r.sample([p for j,p in enumerate(pop) if j!=i], 3)
      j_rand = r.randrange(d)  # ensure at least one from mutant
      y = [a[j] + F*(b[j]-c[j]) if r.random()<cr or j==j_rand else pop[i][j] 
           for j in range(d)]
      if f(y) < f(pop[i]): pop[i] = y
  return min(pop, key=f)

print("\ty\tx")

# Sphere: min at (0,0)
f1 = lambda x: sum(xi**2 for xi in x)
if x := de(f1): print(f"1\t{f1(x):.2f}\t{[f'{xi:.2f}' for xi in x]}")

# Rosenbrock: min at (1,1) 
f2 = lambda x: sum(100*(x[i+1]-x[i]**2)**2 + (1-x[i])**2 for i in range(len(x)-1))
if x := de(f2, iters=500): print(f"2\t{f2(x):.2f}\t{[f'{xi:.2f}' for xi in x]}")

# Rastrigin: min at (0,0,0)
f3 = lambda x: 10*len(x) + sum(xi**2 - 10*m.cos(2*m.pi*xi) for xi in x)
if x := de(f3, d=3, n=30, iters=300): print(f"3\t{f3(x):.2f}\t{[f'{xi:.2f}' for xi in x]}")

# Ackley: min at (0,0)
f4 = lambda x: -20*m.exp(-.2*m.sqrt(sum(xi**2 for xi in x)/len(x))) \
               -m.exp(sum(m.cos(2*m.pi*xi) for xi in x)/len(x)) + 20 + m.e
if x := de(f4, iters=200): print(f"4\t{f4(x):.2f}\t{[f'{xi:.2f}' for xi in x]}")

"""
Desired output:
	y	x
1	0.00	['0.00', '0.00']
2	0.00	['1.00', '1.00']
3	0.00	['-0.00', '0.00', '-0.00']
4	0.00	['0.00', '0.00']
"""
