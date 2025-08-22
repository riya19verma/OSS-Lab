def fib(n, dp):
    if n<=1:
        dp[n] = n
        return dp[n]
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib(n-1, dp) + fib(n-2, dp)
    return dp[n]

n = int(input("Enter the value of n: "))
dp = [-1] * (n+1)
num = fib(n, dp)
print(dp[:6])