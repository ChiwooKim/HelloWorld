def solution(n):
    answer = []

    def tower(x, start, sub, end):
        if x == 1:
            answer.append([start, end])
            return

        tower(x - 1, start, end, sub)
        answer.append([start, end])
        tower(x - 1, sub, start, end)

    tower(n, 1, 2, 3)

    return answer
