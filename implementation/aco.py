import random
import math
import sys
import argparse
import time

class Graph(object):
    def __init__(self, adj_matrix, rank):
        self.matrix = adj_matrix
        self.rank = rank
        self.pheromone = [[1 / (rank * rank) for j in range(rank)]
                          for i in range(rank)]  # m x m


class ACO(object):
    def __init__(self, cont_ant, generations, alfa, beta, ro, Q=0.0):

        self.Q = Q
        self.ro = ro
        self.beta = beta
        self.alfa = alfa
        self.cont_ant = cont_ant
        self.generations = generations

    def _update_pheromone(self, graph, ants):
        for i, line in enumerate(graph.pheromone):
            for j, column in enumerate(line):
                graph.pheromone[i][j] *= self.ro  
                for ant in ants: 
                    graph.pheromone[i][j] += ant.pheromone_delta[i][j]

    def resolve(self, graph):
        best_cost = float('inf')
        best_solution = []
        for gen in range(self.generations):
            ants = [_Ant(self, graph) for i in range(self.cont_ant)
            ]
            for ant in ants:
                for i in range(graph.rank - 1):
                    ant._selection_proximity()
                ant.total_cost += graph.matrix[ant.path[-1]][ant.path[0]]
                if ant.total_cost< best_cost:
                    best_cost = ant.total_cost
                    best_solution = [] + ant.path
                ant._update_pheromone_delta()  
            self._update_pheromone(graph, ants)
        return best_solution, best_cost


class _Ant(object):
    def __init__(self, aco, graph):
        self.colonies = aco
        self.graph = graph
        self.total_cost = 0.0 
        self.path = [] 
        self.pheromone_delta = []  
        self.allowed = [i for i in range(graph.rank)]
        self.eta = [[ 0 if i == j else 1 / graph.matrix[i][j] for j in range(graph.rank)] for i in range(graph.rank)]
        start = random.randint(0, graph.rank - 1) 
        self.path.append(start)
        self.current = start
        self.allowed.remove(start)

    def _selection_proximity(self):
        denominator = 0
        for j in self.allowed:
            denominator += self.graph.pheromone[self.current][j]**self.colonies.alfa * self.eta[self.current][j]**self.colonies.beta
        probabilities = [0 for i in range(self.graph.rank)]  
        for i in range(self.graph.rank):
            try:
                self.allowed.index(i)
                probabilities[i] = self.graph.pheromone[self.current][i] ** self.colonies.alfa * \
                    self.eta[self.current][i] ** self.colonies.beta / denominator
            except ValueError:
                pass   

        selection = 0
        rand = random.random()
        for i, probability in enumerate(probabilities):
            rand -= probability
            if rand <= 0:
                selection = i
                break
        self.allowed.remove(selection)
        self.path.append(selection)
        self.total_cost += self.graph.matrix[self.current][selection]
        self.current = selection

    def _update_pheromone_delta(self):
        self.pheromone_delta = [[0 for j in range(self.graph.rank)] for i in range(self.graph.rank)]
        for _ in range(1, len(self.path)):
            i = self.path[_ - 1]
            j = self.path[_]
            self.pheromone_delta[i][j] = self.colonies.Q / self.total_cost

def calc_distance(site1, site2):
    return math.sqrt((site1['x'] - site2['x'])**2 +
                     (site1['y'] - site2['y'])**2)

def aco(rank,distances):
    for i in range(rank): 
        for j in range(rank):
            if distances[i][j]==0:
                distances[i][j]=1
    aco = ACO(cont_ant=10, generations=10, alfa=1.0, beta=10.0, ro=0.5, Q=10)
    graph = Graph(distances, rank)
    path, cost = aco.resolve(graph)
    print( "Best trail found: ", path)

