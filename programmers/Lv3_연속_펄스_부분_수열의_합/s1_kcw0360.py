def solution(sequence):
    n = len(sequence)
    seq1, seq2 = [], []
    w = 1
    for i in range(n):
        seq1.append(sequence[i] * w)
        seq2.append(sequence[i] * -w)
        w *= -1

    res1, res2 = [seq1[0]], [seq2[0]]
    for i in range(1, n):
        res1.append(max(res1[i - 1] + seq1[i], seq1[i]))
        res2.append(max(res2[i - 1] + seq2[i], seq2[i]))

    return max(max(res1), max(res2))
