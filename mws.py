# vim: set ts=2 sw=2 et ai si:
import random as r
import math as m
r.seed(1)

def maxwalk(f, d=2, iters=100, lo=-5, hi=5, p=0.3, step=0.5):
  x = [r.uniform(lo,hi) for _ in range(d)]
  best = x[:]
  for _ in range(iters):
    i = r.randrange(d)
    old = x[i]
    if r.random() < p:  # random restart
      x[i] = r.uniform(lo, hi)
    else:  # greedy local search - try both directions
      x[i] = old + r.uniform(-step, step) * (hi - lo)
      x[i] = max(lo, min(hi, x[i]))
    if f(x) < f(best): 
      best = x[:]
    else:
      x[i] = old  # revert if not better (greedy!)
  return best

print("\ty\tx")

# Sphere: min at (0,0)
f1 = lambda x: sum(xi**2 for xi in x)
if x := maxwalk(f1, iters=5000): print(f"1\t{f1(x):.2f}\t{[f'{xi:.2f}' for xi in x]}")

# Rosenbrock: min at (1,1) 
f2 = lambda x: sum(100*(x[i+1]-x[i]**2)**2 + (1-x[i])**2 for i in range(len(x)-1))
if x := maxwalk(f2, iters=10000, p=0.2, step=0.3): 
  print(f"2\t{f2(x):.2f}\t{[f'{xi:.2f}' for xi in x]}")

# Rastrigin: min at (0,0,0)
f3 = lambda x: 10*len(x) + sum(xi**2 - 10*m.cos(2*m.pi*xi) for xi in x)
if x := maxwalk(f3, d=3, iters=10000, p=0.4): 
  print(f"3\t{f3(x):.2f}\t{[f'{xi:.2f}' for xi in x]}")

# Ackley: min at (0,0)
f4 = lambda x: -20*m.exp(-.2*m.sqrt(sum(xi**2 for xi in x)/len(x))) \
               -m.exp(sum(m.cos(2*m.pi*xi) for xi in x)/len(x)) + 20 + m.e
if x := maxwalk(f4, iters=5000, p=0.3): 
  print(f"4\t{f4(x):.2f}\t{[f'{xi:.2f}' for xi in x]}")

"""
Desired output:
	y	x
1	0.00	['0.00', '0.00']
2	0.00	['1.00', '1.00']
3	0.00	['-0.00', '0.00', '-0.00']
4	0.00	['0.00', '0.00']
"""
