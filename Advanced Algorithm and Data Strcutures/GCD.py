# this is a GCD algorithm that runs in log(max(a,b)) time, which is significantly faster than prime factorization plus
# intersecting the factors -O(sqrt(max(a, b)). the method is called Euclidean Algorithm
def gcd(a, b):
    while a and b:
        if a >= b: a %= b
        else: b %= a
    if a: return a
    return b


print(gcd(10, 5))
print(gcd(10, 237))
print(gcd(11, 55))
print(gcd(30, 42))
