import math
nodes = []
file1 = open('nodes.txt', 'r') 
Lines = file1.readlines() 
num_nodes = 75
for i in range(num_nodes):
	node,x,y = Lines[i].strip().split(" ")
	nodes.extend([(node,(float(x),float(y)))])


def calcEuclideanDist(x1,x2,y1,y2):
	distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
	return distance

def generate(nodes, num):
	arr = [[999999 for _ in range(num)] for _ in range(num)]
	for i in range(num):
		for j in range(num):
			if i!=j:
				calc = calcEuclideanDist(nodes[i][1][0],nodes[j][1][0],nodes[i][1][1],nodes[i][1][1])
				arr[i][j] = calc
				arr[j][i] = calc
	return arr

distances = (generate(nodes,num_nodes))
print(distances)