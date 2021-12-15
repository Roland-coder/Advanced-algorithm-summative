from heapq import heappush, heappop
import heapq

def shortestReach(n,edges,s):
    graph = [[] for _ in range(n)]
    for i in range(n):
        x,y,r = edges[i][0],edges[i][1],edges[i][2]
        x,y = x-1,y-1
        graph[x].append((r,y))
        graph[y].append((r,x))
        
    S = s - 1
    paths = [-1]*n
    visited = [False]*n
    visited[S] = True
    cd = 0
    q = [(cd,S)]
    while q:
        d,c = heappop(q)
        for r,num in graph[c]:
            nd = d+r
            if not visited[num]:
                visited[num] = True
                heappush(q, (nd,num))
                paths[num] = nd
            else:
                if paths[num] > nd:
                    index = q.index((paths[num],num))
                    q[index] = (nd,num)
                    heapq._siftdown(q, 0, index)
                    paths[num] = nd
                    
                    
    paths = paths[:S] + paths[S+1:]
    print(" ".join(map(str, paths)))
n = 4
edges = [[1,2,24],[1,4,20],[1,3,3],[3,4,12]]
s = 4
shortestReach(n,edges,s)
