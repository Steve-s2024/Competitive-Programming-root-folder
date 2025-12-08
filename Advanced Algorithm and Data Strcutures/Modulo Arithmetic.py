# the space for modulo arithmetic operation and tricks

# an identity of modulo operation
# if A % mod = B % mod, then A/k % (mod/gcd(mod, k)) = B/k % (mod/gcd(mod, k))


# 0. define division modulo operation with Fermat's little theorem.
# the theorem give such relation: pow(a, m-2) % m = pow(a, -1) % m, where m is co-prime with a and m is prime itself

# 1. to get the modulo equivalent of expression (a + b/c) % mod, where a, b, c are int and mod is co-prime with a and
# mod is prime itself
mod = 998244353
arr = [[1,18], [2,9]] # arr[i] represent a fraction of the form arr[i][0]/arr[i][1]
res = 0
for p, q in arr:
    # res => a, p => b, q => c
    res = (res*q + p) * pow(q, mod-2, mod)
    res %= mod
print(res)
