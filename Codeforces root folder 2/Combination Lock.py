# I kind of gambled with this solution and 
# it worked.

# although I finally understand why it work when input is odd, but
# still don't know why it is guaranteed to have no permutation when 
# the size of the combination is even number. 
t = int(input())
for x in range(t):
    n = int(input())
    if n % 2 == 1:
        odd = []
        even = []
        for num in range(1, n+1):
            if num % 2:
                odd.append(str(num))
            else:
                even.append(str(num))
        print(' '.join(odd + even))
    else:
        print('-1')