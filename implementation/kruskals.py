from distances import distances
import sys
from collections import defaultdict

class Graph:
	def __init__(self,vertices):
		self.vertices = vertices
		self.edges=[]
		self.adj = defaultdict(list)

	def addEdge(self,u,v,w):
		self.edges.append([u,v,w])
		self.adj[u].append([v,w])

	def findNeighbor(self, u):
		return self.adj[u]

	def find(self, parent, i): 
		if parent[i] == i: 
			return i
		return self.find(parent, parent[i])

	def union(self, parent, rank, x, y): 
		xroot = self.find(parent, x) 
		yroot = self.find(parent, y) 
  
		if rank[xroot] < rank[yroot]: 
			parent[xroot] = yroot 
		elif rank[xroot] > rank[yroot]: 
			parent[yroot] = xroot 
		else : 
			parent[yroot] = xroot 
			rank[xroot] += 1

	def kruskal(self,src):
		path = []
		e = 0
		
		source_edges = []
		self.edges =  sorted(self.edges,key=lambda item: item[2])
		for i in range(len(self.edges)):
			u,v,w = self.edges[i]
			if u==src:
				source_edges.append([i,w])
		source_edges = sorted(self.edges,key=lambda item:item[2])
		first_edge = source_edges[0][0]
		self.edges[0],self.edges[first_edge] = self.edges[first_edge],self.edges[0]
		i = 0
		parent = []
		rank = [] 
		for node in range(self.vertices): 
			parent.append(node) 
			rank.append(0)
		while e < self.vertices -1 : 
			u,v,w =  self.edges[i] 
			i = i + 1
			x = self.find(parent, u) 
			y = self.find(parent ,v) 
			if x != y: 
				e = e + 1     
				path.append([u,v,w]) 
				self.union(parent, rank, x, y)       
		return path
	
# def formShortestPath(path,src,dest):
# 	minWeight = 99999999
# 	nextNode = -1
# 	flag = 0
# 	print("Path: ",src)
# 	if src!=dest:
# 		for u,v,w in path:
# 			if u == src or v==src:
# 				if w<minWeight:
# 					minWeight = w
# 					if u==src:
# 						nextNode =v
# 						flag = 1
# 					else:
# 						nextNode = u
# 						flag = -1
		
# 		if flag==1:
# 			# print([src,nextNode,minWeight])
# 			path.remove([src,nextNode,minWeight])
# 		elif flag == -1:
# 			# print([nextNode,src,minWeight])
# 			path.remove([nextNode,src,minWeight])
# 		else:
# 			print("It is not part of MST")
# 			return
# 		formShortestPath(path,nextNode,dest)

def DFS(G,MST, s, t, status, parent, w):
	if s == t:
		return
	status[s] = 1
	for v in G.findNeighbor(s):
		# print("Printing neighbours of ",s)
		# print([s,v[0],v[1]])
		if [s,v[0],v[1]] in MST or [v[0],s,v[1]] in MST:			
			if status[v[0]]==2:
				# print("Going from", s,v[0])
				# w[v[0]]=min(w[s],v[1])
				parent[v[0]]=s
				DFS(G,MST,v[0],t,status,parent,w)
	status[s] = 0
	return

def path(G,MST, s, t,nodes):
	status = [2]*nodes
	parent = [-1]*nodes
	w = [0]*nodes
	w[s] = sys.maxsize
	maxw = sys.maxsize

	DFS(G,MST, s, t, status, parent, w)
	pathTrace = [0]*nodes
	# print(len(parent))
	# for i in range(len(parent)):
	# 	print(i,parent[i])
	i = 0
	while t != s:
		maxw = min(maxw, w[t])
		pathTrace[i] = t
		t = parent[t]
		i += 1
	pathTrace[i] = s
	n = i
	cost =0
	print("Path taken is ")
	for j in range(n+1):
		print(pathTrace[j], end=" ")
		if j!=n:
			cost+=distances[pathTrace[j]][pathTrace[j+1]]
			# print("cost:",cost)
	print("\n")
	print("cost: ",cost)
	return maxw

def kruskal(nodes,src,dest, distances):
	print("Source: ",src)
	print("Destination: ",dest)
	G = Graph(nodes)
	for i in range(nodes):
		for j in range(nodes):
			if distances[i][j] !=0.0:
				G.addEdge(i,j,distances[i][j])	
	MST = G.kruskal(src)
	# print("Minimum Spanning Tree")
	# for u,v,w in MST:
	# 	print(u,v,"weight: ",w)
	# print("Shortest path from source to destination")
	# formShortestPath(path,src,dest)
	path(G,MST,src,dest,nodes)

# kruskal(10,0,9,distances)