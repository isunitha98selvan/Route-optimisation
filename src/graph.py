import random
from collections import defaultdict
from graphValue import graph
from graph200 import graph200
class Edge:
	def __init__(self, src, dst, bw):
		self.src = src
		self.dst = dst
		self.bw = bw

class Vertex:
	def __init__(self, dst = 0, bw = 0):
		self.dst = dst
		self.bw = bw

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def findNeighbor(self, u):
		return self.graph[u]

	def addEdge(self, u, v, bw):
		self.graph[u].append(Vertex(v, bw))

	def exists(self, x, y):
		vertices = self.graph[x]
		for v in vertices:
			if v.dst == y:
				return True
		return False

	def createSparseG(self):
		V = 100
		for i in range(V):
			for j in range(V):
					self.addEdge(i, j, graph200[i][j])
					self.addEdge(j, i, graph200[j][i])

	def createDenseG(self):
		V = 5000
		deg = 0.2*V

		for i in range(int(V/2)):
			while len(self.graph[i]) < deg:
				v_rand = random.randint(0, V-1)
				if (v_rand != i) and self.exists(i, v_rand) == False and len(self.graph[v_rand]) < deg:
					w = random.randint(1, 1000)
					self.addEdge(i, v_rand, w)
					self.addEdge(v_rand, i, w)



