import math
import sys
import heapq 
from graph import Graph, Vertex, Edge
from MakeUnionFind import MakeUnionFind
V = 5000

# Algorithm status codes:
# In-Tree = 0
# Fringe = 1
# Unseen = 2

def heapify(E, i, n):
	maxVal = i
	left = 2*i+1
	right = 2*i+2

	if (left < n and E[left].w > E[maxVal].w):
		maxVal = left
	if (right < n and E[right].w > E[maxVal].w):
		maxVal = right
	if (maxVal != i):
		E[maxVal], E[i] = E[i], E[maxVal]
		heapify(E, maxVal, n)


def heapSort(G, E):
	for v in range(0, V):
		for n in G.findNeighbor(v):
			if (n.dst >= v):
				E.append(Edge(v, n.dst, n.w))

	n_val = len(E)
	for i in range(int(n_val/2)-1, -1, -1):
		heapify(E, i, n_val)

	for i in range(n_val-1, -1, -1):
		E[0], E[i] = E[i], E[0]
		heapify(E, 0, i)

def DFS(G, s, t, status, parent, w):
	if s == t:
		return
	status[s] = 1
	for v in G.findNeighbor(s):
		if status[v.dst] == 2:
			w[v.dst] = min(w[s], v.w)
			parent[v.dst] = s
			DFS(G, v.dst, t, status, parent, w)
	status[s] = 0
	return

def path(G, s, t):
	status = [2]*V
	parent = [-1]*V
	w = [0]*V
	w[s] = sys.maxsize
	maxw = sys.maxsize

	DFS(G, s, t, status, parent, w)
	pathTrace = [0]*V
	i = 0
	while t != s:
		maxw = min(maxw, w[t])
		pathTrace[i] = t
		t = parent[t]
		i += 1
	pathTrace[i] = s

	return maxw


def kruskal(G, s, t):
	edges = list()
	heapSort(G, edges)
	muf = MakeUnionFind(V)
	newG = Graph()
	for i in range(len(edges)-1, -1, -1):
		e = edges[i]
		source = muf.Find(e.src)
		destiny = muf.Find(e.dst)
		if source != destiny:
			newG.addEdge(e.src, e.dst, e.w)
			newG.addEdge(e.dst, e.src, e.w)
			muf.Union(source, destiny)

	return path(newG, s, t)
