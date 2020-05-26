numNodes = 11
numAnts = 100
maxTime = 100
infinity = 9999


alpha = 3 # influence of pheromone in direction
beta = 2 # influence of adjacent node distance
rho = 0.01 # pheromone decrease factor
Q = 2.0 # pheromone increase factor

def Graph(self, dist): #[numNodes][numNodes]
    random.seed(42)
    for i in range(numNodes):
        for j in range(numNodes):
            if j == i:
                dist[i][j] = infinity
            else:
                d = randint(0,32767) % 10 + 1
                dist[i][j] = d
                dist[j][i] = d

def printants(self, ants):
    for i in range(numAnts):#(i = 0; i < numAnts; i++)
        temp =[]
        for j in range(len(ants[i])):#(j = 0; j < ants[i].size(); j++)
            temp.append(str(ants[i][j]))
        print(" ".join(temp))

def printpheromones(self, pheromones):
    for i in range(numNodes):
        temp =[]
        for j in range(numNodes):
            temp.append(str(pheromones[i][j]))
        print(" ".join(temp))

def InitPheromones(self, pheromones):
    for i in range(numNodes):
        for j in range(numNodes):
            pheromones[i][j] = 0.01

def InitAnts(self, ants):
    for i in range(numAnts):
        start = 0
        vis = [0 for _ in range(numNodes)]
        trail = []
        trail.append(start)
        vis[start] = 1

        for j in range(numNodes):

            r = randint(0,32767) % numNodes
            r+=1

            if vis[r] == 0:
                vis[r] = 1
                trail.append(r)
            else:
                j-=1
            if r == 10:
                break

        index = 0
        for j in range(len(trail)):
            ants[i].append(trail[j])

def Length(self, x, dist):
    ans = 0.0
    for i in range(len(x)-1):
        ans += dist[x[i]][x[i + 1]]
    return ans

def ShowLength(ants,dist):
    for i in range(numAnts):
        temp = [str(i) + ": [ "]
        for j in range(len(ants[i])):
            temp.append(str(ants[i][j]) + " ")
        temp.append("] len = ")
        leng = Length(ants[i], dist);
        temp.append(leng)
        print(''.join(temp))
