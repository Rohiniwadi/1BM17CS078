class graph:
    def  __init__(self,v):
        self.v=v
        self.adj=[[] for i in range(self.v)]
    def Dfs(self,t,v,visited):
        visited[v]=True
        t.append(v)
        for i in self.adj[v]:
            if visited[i]== False:
                t=self.Dfs(t,i,visited)
        return t
    def connectedcomponent(self):
        visited=[]
        c=[]
        for i in range(self.v):
            visited.append(False)
        for i in range(self.v):
            if visited[i]==False:
                t=[]
                c.append(self.Dfs(t,i,visited))
        return c
    def addedge(self,v,w):
        self.adj[v].append(w)
        self.adj[w].append(v)
g=graph(6)
g.addedge(0,1)
g.addedge(2,3)
g.addedge(3,4)
l=g.connectedcomponent()
print(l)
        
