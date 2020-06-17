from graph import Graph, Vertex
import heapq

def dijkstraHeap(G, s, t, V):
	distances = { i: float("inf") for i in range(V)}
	distances[s] = 0
	min_heap = [(0,s)]
	visited = set()

	while min_heap:
		
		cur_dist, cur = heapq.heappop(min_heap)
		if cur in visited: continue
		visited.add(cur) 
		n = G.graph[cur]   
		for i in range(len(n)):
			if n[i].dst in visited: continue
			this_dist = cur_dist + n[i].w
			if this_dist  < distances[n[i].dst]:
				distances[n[i].dst] = this_dist
				heapq.heappush(min_heap, (this_dist, n[i].dst))
	return distances[t]