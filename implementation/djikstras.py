import heapq

def dijkstra(graph, source, dest, numNodes):
    distances = [float('infinity') for i in range(numNodes)]
    distances[source] = 0

    pq = [(0, source)]
    parent = [-1 for i in range(numNodes)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for i in range(numNodes): #Iterate through neighbours
            if(i == current_vertex or graph[current_vertex][i] == 0.0): continue
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
