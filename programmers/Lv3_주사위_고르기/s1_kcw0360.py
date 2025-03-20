from itertools import combinations, product
from bisect import bisect_left


def solution(dice):
    n = len(dice)
    best_win_rate = -1
    answer = []

    # A가 선택할 수 있는 모든 조합 생성
    for A_comb in combinations(range(n), n // 2):
        B_comb = [j for j in range(n) if j not in A_comb]

        # A와 B의 주사위 조합에서 가능한 모든 합 계산
        A_sums = sorted(sum(roll) for roll in product(*(dice[k] for k in A_comb)))
        B_sums = sorted(sum(roll) for roll in product(*(dice[k] for k in B_comb)))

        # A의 승률 계산
        win_cnt = 0
        total_cases = len(A_sums) * len(B_sums)

        for a_sum in A_sums:
            win_cnt += bisect_left(B_sums, a_sum)  # B보다 작은 경우 찾기

        win_rate = win_cnt / total_cases  # 승률 반환

        # 최적의 조합 찾기 (승률이 같은 경우 사전 순으로 작은 조합 선택)
        if win_rate > best_win_rate:
            best_win_rate = win_rate
            answer = sorted([i + 1 for i in A_comb])
        elif win_rate == best_win_rate:
            answer = min(answer, sorted([i + 1 for i in A_comb]))

    return answer
