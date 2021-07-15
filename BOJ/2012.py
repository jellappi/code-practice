# https://www.acmicpc.net/problem/2012

from sys import stdin
input = stdin.readline

n = int(input())
nums = list(int(input()) for _ in range(n))
nums.sort()

unhappy = 0
for i in range(n):
    unhappy += abs((i+1) - nums[i])
    
print(unhappy)
