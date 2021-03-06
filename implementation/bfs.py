import pytholog as pl
from data.distances75 import distances
from vertex import Vertex
import time
import heapq
import random

numNodes = 50
distances[0][numNodes-1] = 0.0
start = time.time()
graph_kb = pl.KnowledgeBase("Shortest path in a network")
arr = []
for i in range(numNodes):
    for j in range(50):
        if distances[i][j] != 0.0 and i!=j:
            route =  "route(p" + str(i) + ",p" + str(j) + "," + str(distances[i][j]) + ")"
            arr.append(route)
    

arr.append("path(X, Y, P) :- route(X, Y, P)")
arr.append("path(X, Y, P) :- route(X, Z, P2), path(Z, Y, P3), P is P2 + P3")
# arr.append("path(X, Y, P) :- route(Y, Z, P2), path(Z, X, P3), P is P2 + P3")
graph_kb(arr)

x, y = graph_kb.query(pl.Expr("path(p0,p49, Weight)"), cut = True, show_path = True)
nodes = [x for x in y if str(x) > "Z"] ## remove weights in the visited nodes
traversed = []
for i in nodes:
    traversed.append(int(i[1:]))
traversed.append(0)
traversed.append(numNodes-1)
source = 0


dist = [float('infinity') for i in range(numNodes)]
dist[source] = 0

pq = [(0, source)]
parent = [-1 for i in range(numNodes)]
while len(pq) > 0:
    current_distance, current_vertex = heapq.heappop(pq)

    if current_distance > dist[current_vertex]:
        continue

    for i in range(numNodes): #Iterate through neighbours
        if i == current_vertex or distances[current_vertex][i] == 0.0: continue
        if not i in traversed: continue
        distance = current_distance + distances[current_vertex][i]
        if distance < dist[i]:
            dist[i] = distance
            heapq.heappush(pq, (distance, i))
            parent[i] = current_vertex
path = []
node = numNodes -1
while node != source:
    path.append(node)
    node = parent[node]
path.append(source)
print(dist[numNodes-1])
print("Path taken")
print(path)

end = time.time()
print(end-start)