#https://www.acmicpc.net/problem/1449
'''
정렬 + 그리디 알고리즘
'''

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
re = 0
sticker = arr[0]-0.5 # 스티커 시작 위치
for i in range(len(arr)):
    #print( sticker , arr[i]+0.5)
    if sticker < arr[i]-0.5:
        sticker = arr[i]-0.5
    while sticker < arr[i]+0.5:  #위치보다 0.5이상 필요
        sticker += L
        re += 1
print(re)