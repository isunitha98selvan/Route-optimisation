import math
import random
import sys
import time

from graph import Graph, Vertex, Edge
from dijkstraAlgo import dijkstraHeap
from backtracking import ibacktracking
from kruskalAlgo import kruskal

def main():

	V = 100
	G = Graph()
	G.createGraph(V)

	srcV = 0
	dstV = V-1

	#Testing Improved backtracking
	start = time.time()
	max_D = ibacktracking(G, srcV, dstV, V)
	end = time.time()
	elapsedTimeD = end-start
	
	print("Time taken by Improved Backtracking algorithm: ", elapsedTimeD)

	#Testing Dijkstra's Algorithm with Heap structure
	start = time.time()
	max_DH = dijkstraHeap(G, srcV, dstV, V)
	end = time.time()
	elapsedTimeDH = end-start
	print("Time taken by Djikstra's algorithm: ", elapsedTimeDH)

	#Testing Kruskal's Algorithm  with Heapsort
	start = time.time()
	max_K = kruskal(G, srcV, dstV)
	end = time.time()
	elapsedTimeK = end-start
	print("Time taken by Kruskal's algorithm: ", elapsedTimeK)

	#Prints Maximum Bandwidth Path for each algorithm
	print("Max bandwidth Improved Backtracking algorithm: ", max_D)
	print("Max bandwidth Dijkstra's Algorithm: ", max_DH)
	print("Max bandwidth Kruskal's algorithm : ", max_K)

if __name__ == "__main__":
	main()