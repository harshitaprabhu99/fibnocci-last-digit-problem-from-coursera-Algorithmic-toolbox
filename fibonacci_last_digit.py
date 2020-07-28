# Uses python3
def fib_last(n):
    f=[0,1]
    for i in range(2,n+1):
        f.append((f[i-1]+f[i-2])%10)
    return f[n] 
n=int(input())
print(fib_last(n))
