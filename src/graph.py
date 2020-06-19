import random
from collections import defaultdict
from graphValue import graph
import generate_graph
class Edge:
	def __init__(self, src, dst, w):
		self.src = src
		self.dst = dst
		self.w = w

class Vertex:
	def __init__(self, dst = 0, w = 0):
		self.dst = dst
		self.w = w

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
		self.arr = None
		self.failed = []

	def findNeighbor(self, u):
		return self.graph[u]

	def addEdge(self, u, v, w):
		self.graph[u].append(Vertex(v, w))

	def exists(self, x, y):
		vertices = self.graph[x]
		for v in vertices:
			if v.dst == y:
				return True
		return False
	

	def createGraph(self, V):
		g = generate_graph.generate(V)
		self.arr = g
		for i in range(V):
			for j in range(V):
				if i != j:
					self.graph[i].append(Vertex(j, g[i][j]))
					self.graph[j].append(Vertex(i, g[j][i]))




