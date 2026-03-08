import math

def recursive_pi(n):
    term = (1 / 16**n) * (4/(8*n + 1) - 2/(8*n + 4) - 1/(8*n + 5) - 1/(8*n + 6))
    print(n, " ", term)
    if n == 0:
        return term
    return term + recursive_pi(n - 1)

if __name__ == "__main__":
    print("k", " ", "Contribution to the value of", "\u03C0")
    result = recursive_pi(10)
    print()
    print("The BBP value of \u03C0 =", result)
    print("The Math module value of \u03C0 =", math.pi)

