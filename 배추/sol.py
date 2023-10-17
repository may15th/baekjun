
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



T = int(input())
for i in range(T):
    M,N,K =  map(int, input().split())
    graph = [[0 for i in range(M)] for j in range(N)]
    visited = [[0 for i in range(M)] for j in range(N)]

    dirR = [-1,1,0,0]
    dirc = [0,0,-1,1]


    def dfs(x,y):
        global visited
        visited[y][x] = True
        for dirIdx in range(4):
            newY = y + dirR[dirIdx]
            newX = x + dirc[dirIdx]
            if graph[newY][newX] and not visited[newY][newX]:
                dfs(newY,newX)
    
    #1. 그래프 정보 입력:
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y+1][x+1] = True

    #2.방문하지 않은 지점 부터 dfs
    answer = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] and not visited[i][j]:
                dfs(i,j)
                answer += 1
    print(answer)