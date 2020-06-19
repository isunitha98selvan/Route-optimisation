from vertex import Vertex
import random
import djikstras
def main():
    nodes = 10
    vertices =[]
    for i in range(nodes):
        v_traffic = random.randint(1,50)
        vertices.append(Vertex(i,v_traffic)) 
main()