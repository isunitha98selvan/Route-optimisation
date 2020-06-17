import math
from graph import Graph, Vertex

def maxWeightVertex(w, visited, V):
	maxW = -99999
	vertex = 0
	for i in range(V):
		if visited[i] == 1 and maxW < w[i]:
			maxW = w[i]
			vertex = i

	return vertex

def ibacktracking(G, s, t, V):
	w = [0]*V
	parent = [-1]*V
	visited = [2]*V
	
	visited[s] = 0
	w[s] = 99999999
	for v in G.graph[s]:
		w[v.dst] = v.w
		parent[v.dst] = s
		visited[v.dst] = 1

	while visited[t] != 0:
		v = maxWeightVertex(w, visited, V)
		visited[v] = 0
		n = G.graph[v]
		for i in range(len(n)):
			end = n[i].dst
			if (visited[end] == 2):
				w[end] = min(w[v], n[i].w)
				parent[end] = v
				visited[end] = 1
			elif (visited[end] == 1 and w[end] < min(w[v], n[i].w)):
				w[end] = min(w[v], n[i].w)
				parent[end] = v
	return w[t]



