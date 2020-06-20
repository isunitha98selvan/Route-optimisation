from distances import distances

class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.edges=[]

    def addEdge(self,u,v,w):
        self.edges.append([u,v,w])

    def find(self, parent, i): 
        if parent[i] == i: 
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
  
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1

    def kruskal(self,src):
        path = []
        e = 0
        
        source_edges = []
        self.edges =  sorted(self.edges,key=lambda item: item[2])
        for i in range(len(self.edges)):
            u,v,w = self.edges[i]
            if u==src:
                source_edges.append([i,w])
        source_edges = sorted(self.edges,key=lambda item:item[2])
        first_edge = source_edges[0][0]
        self.edges[0],self.edges[first_edge] = self.edges[first_edge],self.edges[0]
        i = 0
        parent = []
        rank = [] 
        for node in range(self.vertices): 
            parent.append(node) 
            rank.append(0)
        while e < self.vertices -1 : 
            u,v,w =  self.edges[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 
            if x != y: 
                e = e + 1     
                path.append([u,v,w]) 
                self.union(parent, rank, x, y)       
        return path
    
def formShortestPath(path,src,dest):
    minWeight = 99999999
    nextNode = -1
    flag = 0
    print("Path: ",src)
    if src!=dest:
        for u,v,w in path:
            if u == src or v==src:
                if w<minWeight:
                    minWeight = w
                    if u==src:
                        nextNode =v
                        flag = 1
                    else:
                        nextNode = u
                        flag = -1
        
        if flag==1:
            # print([src,nextNode,minWeight])
            path.remove([src,nextNode,minWeight])
        else:
            # print([nextNode,src,minWeight])
            path.remove([nextNode,src,minWeight])
        formShortestPath(path,nextNode,dest)

def kruskal(nodes,src,dest, distances):
    G = Graph(nodes)
    for i in range(nodes):
        for j in range(nodes):
            if distances[i][j] !=0.0:
                G.addEdge(i,j,distances[i][j])
    
    path = G.kruskal(src)
    print("Minimum Spanning Tree")
    for u,v,w in path:
        print(u,v,"weight: ",w)
    print("Shortest path from source to destination")
    formShortestPath(path,src,dest)

