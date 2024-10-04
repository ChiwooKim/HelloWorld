def solution(n, tops):
    mod = 10007
    dp = [[0, 0] for _ in range(n + 1)]
    dp[0][1] = 1

    for i in range(n):
        dp[i + 1][0] = (dp[i][0] + dp[i][1]) % mod
        if tops[i]:
            dp[i + 1][1] = (dp[i][0] * 2 + dp[i][1] * 3) % mod
        else:
            dp[i + 1][1] = (dp[i][0] + dp[i][1] * 2) % mod

    return (dp[n][0] + dp[n][1]) % mod
