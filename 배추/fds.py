'''
1
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
'''

def dfs(i,j):
    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0<= ni <N and 0<= nj < N:
            arr[ni][nj] == 1 and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            dfs(ni,nj)


T = int(input())
M,N,K =  map(int, input().split())


arr = [[0 for i in range(M)] for j in range(N)]

for x,y in range(K):
    arr[x][y] = 1

visited = [[0 for i in range(M)] for j in range(N)]
cnt = 0



#1. 위치 이동하면서 
for i in range(M):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            cnt +=1
            dfs(i,j)


print(cnt)


