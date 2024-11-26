import sys

input = sys.stdin.readline

N = int(input())
buildings = [int(input()) for _ in range(N)]

stack = []
answer = 0

for building in buildings:
    while stack and stack[-1] <= building:
        stack.pop()
    answer += len(stack)
    stack.append(building)

print(answer)
