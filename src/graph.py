import random
from collections import defaultdict
from graphValue import graph
from graph200 import graph200
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
	
		for i in range(V):
			for j in range(V):
				self.graph[i].append(Vertex(j, graph200[i][j]))
				self.graph[j].append(Vertex(i, graph200[j][i]))




