# Bisection Method

A pure-Python implementation of the **bisection method** for finding roots
of a continuous function.

## The Math

If `f` is continuous on `[a, b]` and `f(a) · f(b) < 0`, then by the
**Intermediate Value Theorem**, there exists at least one root `x*` in `(a, b)`.

The bisection method repeatedly halves the interval, keeping the half where
the sign change occurs. At each step, the midpoint is computed as:

$$c_n = \frac{a_n + b_n}{2}$$

After `n` iterations, the error is bounded by:

$$|x_n - x^*| \leq \frac{b_0 - a_0}{2^{n+1}}$$

**Convergence is linear**: the error is halved at each iteration.

## Usage

```python
from bisection import bisection

def f(x):
    return x**2 - 4

root, iters, errors = bisection(f, 0, 3)
print(root)     # ~2.0
print(iters)    # ~34
