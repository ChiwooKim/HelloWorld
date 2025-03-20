def solution(players, m, k):
    answer = 0
    servers = [0] * 24

    for i in range(24):
        tmp = (players[i] // m) - servers[i]
        if tmp <= 0:
            tmp = 0
        else:
            answer += tmp

        check = i
        while check < 24 and check < i + k:
            servers[check] += tmp
            check += 1

    return answer
