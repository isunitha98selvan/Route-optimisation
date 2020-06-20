from vertex import Vertex
import random
import djikstras
from distances import distances

def generate_weights(n):
    weights = [[random.randint(1,100) for i in range(n)] for j in range(n)]
    return weights

def main():
    nodes = 70
    vertices =[]
    for i in range(nodes):
        v_traffic = random.randint(1,500)
        vertices.append(Vertex(i,v_traffic)) 
    weights = generate_weights(nodes)
    graph = distances
    graph[0][9] = 99999999
    dist = djikstras.dijkstra(graph,0,nodes-1,nodes, vertices)
    print(dist)
    dist2 = djikstras.nodeFailureDjikstras(graph,0,nodes-1,nodes, vertices)
    print(dist2)
    dist3 = djikstras.dijkstraPacketTraffic(graph,0,nodes-1,nodes, vertices)
    print(dist3)

main()

    

