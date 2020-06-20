from vertex import Vertex
import random
import djikstras
from data.distances75 import distances
import time
from kruskals import kruskal
from aco import aco

def generate_weights(n):
    #can be used to generate additional parameters if required 
    weights = [[random.randint(1,100) for i in range(n)] for j in range(n)]
    return weights

def main():
    nodes = 75
    vertices =[]
    source = 0
    destination = nodes-1
    for i in range(nodes):
        v_traffic = random.randint(1,800)
        vertices.append(Vertex(i,v_traffic)) 
    graph = distances
    graph[0][nodes-1] = 99999999
    start = time.time()
    dist = djikstras.dijkstra(graph,source,destination,nodes, vertices)
    end = time.time()
    print(dist[nodes-1])
    print("Time taken is ", end-start)
    print("--------------------------------")
    start = time.time()
    dist2 = djikstras.nodeFailureDjikstras(graph,source,destination,nodes, vertices)
    end = time.time()
    print(dist2[nodes-1])
    print("Time taken is ", end-start)
    print("--------------------------------")
    start = time.time()
    dist3 = djikstras.dijkstraPacketTraffic(graph,source,destination,nodes, vertices)
    end = time.time()
    print(dist3[nodes-1])
    print("Time taken is ", end-start)
    print("--------------------------------")
    start = time.time()
    kruskal(nodes,source,destination,distances)
    end = time.time()
    print("Time taken is ", end-start)
    print("--------------------------------")
    start = time.time()
    aco(nodes,distances)
    end = time.time()
    print("Time taken is ", end-start)
    print("--------------------------------")
   
if __name__=='__main__':
    main()

    

