import math
import random
import sys
import time

# from graph import Graph, Vertex, Edge
# from dijkstraAlgo import *
# from backtracking import ibacktracking
from kruskalAlgo import kruskal
# from AntColonyRO import antColony
def main():

	V = 20
	# G = Graph()
	# G.createGraph(V)

	srcV = 0
	dstV = V-1

	# #Testing Improved backtracking
	# start = time.time()
	# max_D = ibacktracking(G, srcV, dstV, V)
	# end = time.time()
	# elapsedTimeD = end-start
	
	# print("Time taken by Improved Backtracking algorithm: ", elapsedTimeD)

	# #Testing Dijkstra's Algorithm with Heap structure
	# start = time.time()
	# max_DH = dijkstraHeap(G, srcV, dstV, V)
	# end = time.time()
	# elapsedTimeDH = end-start
	# print("Time taken by Djikstra's algorithm: ", elapsedTimeDH)


	# #Testing Dijkstra's Algorithm with Node failure
	# start = time.time()
	# max_DF = djikstraNodeFail(G, srcV, dstV, V)
	# end = time.time()
	# elapsedTimeDH = end-start
	# print("Time taken by Djikstra's algorithm: with node failure ", elapsedTimeDH)

	# #Testing Kruskal's Algorithm  with Heapsort
	# start = time.time()
	# antColony(V,G.arr)
	# end = time.time()
	# elapsedTimeK = end-start
	# # print("Time taken by Kruskal's algorithm: ", elapsedTimeK)

	#Testing Kruskal's Algorithm  with Heapsort
	start = time.time()
	max_K = kruskal(srcV, dstV,10)
	end = time.time()
	elapsedTimeK = end-start
	print(max_K)
	print("Time taken by Kruskal's algorithm: ", elapsedTimeK)

	#Prints Maximum Bandwidth Path for each algorithm
	# print("Max bandwidth Improved Backtracking algorithm: ", max_D)
	# print("Max bandwidth Dijkstra's Algorithm: ", max_DH)
	# print("Max bandwidth Dijkstra's Algorithm with node failure: ", max_DF)
	# print("Max bandwidth Kruskal's algorithm : ", max_K)

if __name__ == "__main__":
	main()