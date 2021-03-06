# 효율적인 해킹
"""
해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 이 회사는 N개의 컴퓨터로 이루어져 있다. 김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.

이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.

이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.

10000개의 컴퓨터, 100000개의 관계
"""
import sys 
from collections import deque

N, M = list(map(int, sys.stdin.readline().strip().split()))
numlist = [[] for i in range(N+1)]
result = []
value = 0
# result_bool = [True]*(N+1)

for i in range(M):
    A, B = list(map(int, sys.stdin.readline().strip().split()))
    numlist[B].append(A)
    # result_bool[A]=False

# res_list = [i for i, value in enumerate(result_bool) if value == True]

def bfs(idx, deq, cnt):
    if len(numlist[idx]) > 0:
        cnt +=1
        deq.extend(numlist[idx])
        while deq:
            new_idx = deq.popleft()
            bfs(new_idx, deque(), cnt)
    else:
        num_list.append(cnt)
        return cnt        
# def dfs(idx):


for i in range(1, N):
    # node = num_list[i]
    num_list = []
    bfs(i, deque(), 0)
    if value==max(num_list):
        result.append(i)
    elif value<max(num_list):
        value = max(num_list)
        result = [i]
print(' '.join(map(str,result)))