
from sys import maxsize 
import numpy as np
from distances75 import distances

Inf = 999999.0

def BellmanFord(graph, V,src,dest): 
    
    dis = [maxsize] * V 
    dis[src] = 0
  
    for i in range(V):
        for j in range(V): 
                if i!=j and graph[i][j]!= 0:
                    if dis[i]!=maxsize and dis[i] + graph[i][j] < dis[j]:
                        dis[j] = dis[i] + graph[i][j]
  
    print("Minimum Distance from Source: " + str(src) + " to destination " + str(dest) + " is:") 
    print(dis[dest])
    return dis[dest]
if __name__ == "__main__": 
    V = 75 # Number of vertices in graph 
   
    arr = np.array(distances)
    graph=arr.astype(int)
    print(len(graph))
    BellmanFord(graph, V, 0,74)