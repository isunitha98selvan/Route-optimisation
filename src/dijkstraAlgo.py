from graph import Graph, Vertex
import heapq
import random


def dijkstraHeap(G, s, t, V):
	distances = { i: float("inf") for i in range(V)}
	distances[s] = 0
	min_heap = [(0,s)]
	visited = set()
	parents = [0 for i in range(V)]

	while min_heap:
		
		cur_dist, cur = heapq.heappop(min_heap)
		if cur in visited: continue
		visited.add(cur) 
		n = G.graph[cur]   
		for i in range(len(n)):
			if n[i].dst in visited or n[i].dst in G.failed: continue
			this_dist = cur_dist + n[i].w
			if this_dist  < distances[n[i].dst]:
				distances[n[i].dst] = this_dist
				heapq.heappush(min_heap, (this_dist, n[i].dst))
				parents[n[i].dst] = cur
	path = []
	node = t
	while node is not s:
		path.append(node)
		node = parents[node]
	path.append(s)
	reversed(path)
	print("Path taken is")
	print(path)
	print("-------------------------")

	return distances[t]

def djikstraNodeFail(G,s,t,V):
	num = V//2
	failed = []
	for _ in range(num):
		val = random.randint(1,V-2)
		if not val in failed:
			G.failed.append(val)
		else:
			while val in failed:
				val = random.randint(1,V-2)
			G.failed.append(val)
	G.failed.append(2)
	G.failed.append(39)
	print(G.failed)
	
	return dijkstraHeap(G,s,t,V)
	





