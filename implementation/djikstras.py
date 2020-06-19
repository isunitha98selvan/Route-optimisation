import heapq
import random

def dijkstra(graph, source, dest, numNodes, vertices):
    distances = [float('infinity') for i in range(numNodes)]
    distances[source] = 0

    pq = [(0, source)]
    parent = [-1 for i in range(numNodes)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for i in range(numNodes): #Iterate through neighbours
            if(i == current_vertex or graph[current_vertex][i] == 0.0 or vertices[i].alive == False): continue
            distance = current_distance + graph[current_vertex][i]
            if distance < distances[i]:
                distances[i] = distance
                heapq.heappush(pq, (distance, i))
                parent[i] = current_vertex
    path = []
    node = dest
    while node != source:
        path.append(node)
        node = parent[node]
    path.append(source)
   
    print(path)

    return distances


def nodeFailureDjikstras(graph, source, dest, numNodes, vertices):
    num = numNodes//2
    for _ in range(num):
        val = random.randint(1,numNodes-2)
        if not vertices[val].alive == True:
            vertices[val].alive = False
        else:
            while vertices[val].alive == False:
                val = random.randint(1,numNodes-2)
            vertices[val].alive = False

    return dijkstra(graph, source, dest, numNodes, vertices)

