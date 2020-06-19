from vertex import Vertex
import random

def generate_weights(n):
    weights = [[random.randint(1,100) for i in range(n)] for j in range(n)]
    return weights

def main():
    nodes = 10
    vertices =[]
    for i in range(nodes):
        v_traffic = random.randint(1,50)
        vertices.append(Vertex(i,v_traffic)) 
    weights = generate_weights(nodes)
