"""
Bisection method for finding roots of a continuous function.

Given a bracketing interval [a, b] where f(a) * f(b) < 0, this
implements the classic bisection algorithm recursively.
"""


def bisection(f, a, b, tol=1e-10, max_iter=100):
    """
    Find a root of f in [a, b] via recursive bisection.

    Parameters
    ----------
    f : callable
    a, b : float
        Endpoints with f(a) * f(b) < 0.
    tol : float
        Stop when the interval width is below this.
    max_iter : int
        Safety cap on recursion depth.

    Returns
    -------
    root : float
    iterations : int
    errors : list of float
    """
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    def recurse(a, b, iters_left, errors):
        if b - a <= tol or iters_left <= 0:
            return (a + b) / 2, len(errors), errors

        c = (a + b) / 2
        errors.append(abs(b - a) / 2)

        if f(a) * f(c) < 0:
            return recurse(a, c, iters_left - 1, errors)
        else:
            return recurse(c, b, iters_left - 1, errors)

    return recurse(a, b, max_iter, [])


if __name__ == "__main__":
    # Example: find the root of f(x) = x^2 - 4 in [0, 3]
    def f(x):
        return x**2 - 4

    root, iters, errors = bisection(f, 0, 3)
    print(f"Root: {root}")
    print(f"Iterations: {iters}")
    print(f"Final error estimate: {errors[-1]}")
