def solution(A, B):
    answer = 0
    n = len(A)
    A.sort(reverse=True)
    B.sort(reverse=True)

    an, bn = 0, 0
    while an < n and bn < n:
        if A[an] < B[bn]:
            answer += 1
            an += 1
            bn += 1
        else:
            an += 1

    return answer
