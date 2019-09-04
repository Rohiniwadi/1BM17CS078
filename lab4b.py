def dfs(m,i,j):
    global visited
    visited[i][j]=True
    r=[-1,-1,-1,0,0,1,1,1]
    c=[-1,0,1,-1,1,-1,0,-1]
    for p in range(8):
        if issafe(m,i+r[p],j+c[p]):
            dfs(m,i+r[p],j+c[p])
    print(visited)
def issafe(m,row,col):
    global visited
    return (row>=0 and col>=0 and row<R and col<C and  not visited[row][col] and m[row][col])
def c_island(m):
    global visited
    count=0
    for i in range(R):
        for j in range(C):
            if visited[i][j]==False and m[i][j]==1:
                dfs(m,i,j)
                count+=1
    return count
matrice=[[1,1,0,0],
         [0,1,1,0],
         [1,0,0,0],
         [1,1,1,1]]
R=len(matrice)
C=len(matrice[0])
visited=[[False for i in range(C)] for j in range(R)]
print(c_island(matrice))
         
