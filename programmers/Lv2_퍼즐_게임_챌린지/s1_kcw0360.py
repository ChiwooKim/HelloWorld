def solution(diffs, times, limit):
    min_lev, max_lev = 1, max(diffs)
    n = len(diffs)

    while min_lev < max_lev:
        now_lev = (min_lev + max_lev) // 2
        temp = times[0]
        for i in range(1, n):
            val = diffs[i] - now_lev
            if val <= 0:
                temp += times[i]
            else:
                temp += val * (times[i - 1] + times[i]) + times[i]

        if temp <= limit:
            max_lev = now_lev
        else:
            min_lev = now_lev + 1

    return min_lev
