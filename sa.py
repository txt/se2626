# vim: set ts=2 sw=2 et ai si:
import random  as r
import math as m

r.seed(1)

def sa(f, x=1, T=100, cool=1, iters=1000, step=1, bounds=None):
  best = x
  eps = T / iters
  for _ in range(iters):
    xnew = x + r.uniform(-step, step)
    if bounds: xnew = max(bounds[0], min(bounds[1], xnew))  # clip
    if f(xnew) < f(x) or r.random() < m.exp((f(x)-f(xnew))/T):
      x = xnew
    if f(x) < f(best): best = x
    T -= cool * eps
  return best

print("\ty\tx")
### Eg 1. Rastrigin (many local minima)**

f1 = lambda x: 10 + x**2 - 10*m.cos(2*m.pi*x)  # global min at x=0
if x := sa(f1, 5): print(f"f1\t{f1(x):.2f}\t{x:.2f}")

### Eg 2. Needle in haystack**

f2 = lambda x: 0 if abs(x-7.1) < .1 else 100 + abs(x-7.3)  # sharp global min
if x := sa(f2, 0, T=200, iters=2000): print(f"f2\t{f2(x):.2f}\t{x:.2f}")

### Eg 3. Deceptive gradient**

f3 = lambda x: -abs(x) if x < 0 else x**2  # gradient points wrong way
if x := sa(f3, 5, T=10, step=5, bounds=(-10, 10)): 
  print(f"f3\t{f3(x):.2f}\t{x:.2f}")  # Start at x=5 (positive side)

### Eg 4. Schwefel (tricky landscape)**

f4 = lambda x: 418.9829 - x*m.sin(m.sqrt(abs(x)))  # min near x=420.97
if x := sa(f4, 400, T=500, iters=5000, step=10): 
  print(f"4\t{f4(x):.2f}\t{x:.2f}")  # Start closer

### Eg 5. Noisy quadratic**

f5 = lambda x: (x-3)**2 + r.gauss(0, 0.5)  # noise hides gradient
if x := sa(f5, 1, T=10, cool=1): print(f"f5\t{f5(x):.2f}\t{x:.2f}")
