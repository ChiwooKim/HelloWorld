from collections import Counter


def solution(points, routes):
    answer = 0
    result = []

    for route in routes:
        cnt = 0
        for i in range(1, len(route)):
            sy, sx = points[route[i - 1] - 1]
            ey, ex = points[route[i] - 1]
            diff = ey - sy
            if diff != 0:
                move = diff // abs(diff)
                while sy != ey:
                    temp = (sy, sx, cnt)
                    result.append(temp)
                    sy += move
                    cnt += 1

            diff = ex - sx
            if diff != 0:
                move = diff // abs(diff)
                while sx != ex:
                    temp = (sy, sx, cnt)
                    result.append(temp)
                    sx += move
                    cnt += 1

            if i == len(route) - 1:
                result.append((sy, sx, cnt))

    for val in Counter(result).values():
        if val > 1:
            answer += 1

    return answer
