from vertex import Vertex
import random
import djikstras
from distances import distances
import time
from kruskals import kruskal
from aco import aco
def generate_weights(n):
    weights = [[random.randint(1,100) for i in range(n)] for j in range(n)]
    return weights

def main():
    nodes = 75
    vertices =[]
    for i in range(nodes):
        v_traffic = random.randint(1,800)
        vertices.append(Vertex(i,v_traffic)) 
    weights = generate_weights(nodes)
    graph = distances
    graph[0][9] = 99999999
    start = time.time()
    dist = djikstras.dijkstra(graph,0,nodes-1,nodes, vertices)
    end = time.time()
    print(dist[nodes-1])
    print("Time taken is ", end-start)
    print("--------------------------------")
    start = time.time()
    dist2 = djikstras.nodeFailureDjikstras(graph,0,nodes-1,nodes, vertices)
    end = time.time()
    print(dist2[nodes-1])
    print("Time taken is ", end-start)
    print("--------------------------------")
    start = time.time()
    dist3 = djikstras.dijkstraPacketTraffic(graph,0,nodes-1,nodes, vertices)
    end = time.time()
    print(dist3[nodes-1])
    print("Time taken is ", end-start)
    print("--------------------------------")
    start = time.time()
    kruskal(nodes,0,nodes-1,graph)
    end = time.time()
    print("Time taken is ", end-start)
    print("--------------------------------")
    start = time.time()
    aco(nodes)
    end = time.time()
    print("Time taken is ", end-start)


main()

    

