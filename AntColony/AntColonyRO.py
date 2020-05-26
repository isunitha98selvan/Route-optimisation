import sys
import random

numNodes = 11
numAnts = 100
maxTime = 100
infinity = 9999


alpha = 3 # influence of pheromone in direction
beta = 2 # influence of adjacent node distance
rho = 0.01 # pheromone decrease factor
Q = 2.0 # pheromone increase factor

def Graph(dist): #[numNodes][numNodes]
    random.seed(42)
    for i in range(numNodes):
        for j in range(numNodes):
            if j == i:
                dist[i][j] = infinity
            else:
                d = randint(0,32767) % 10 + 1
                dist[i][j] = d
                dist[j][i] = d

def printants(ants):
    for i in range(numAnts):#(i = 0; i < numAnts; i++)
        temp =[]
        for j in range(len(ants[i])):#(j = 0; j < ants[i].size(); j++)
            temp.append(str(ants[i][j]))
        print(" ".join(temp))

def printpheromones(pheromones):
    for i in range(numNodes):
        temp =[]
        for j in range(numNodes):
            temp.append(str(pheromones[i][j]))
        print(" ".join(temp))

def InitPheromones(pheromones):
    for i in range(numNodes):
        for j in range(numNodes):
            pheromones[i][j] = 0.01

def InitAnts(ants):
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

def Length(x, dist):
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

def BestTrail(ants,dist,bestTrail):
    bestLength = Length(ants[0],dist)
    index = 0
    for i in range(1,numAnts):
        length = Length(ants[i],dist)
        if length<bestLength:
            bestLength = length
            index=i

    for i in range(len(ants[index])):
        bestTrail.append(ants[index][i])

def Probability(k,nodeX,visited,pheromones,dist,probs):
    tau = [0]*numNodes
    sum = 0.0
    for i in range(numNodes):
        if i==nodeX:
            tau[i]=0.0
        elif visited[i]==True:
            tau[i]=0.0
        else:
            tau[i]= (pow(pheromones[nodeX][i],alpha*1.0)) * (pow((1.0/dist[nodeX][i]*1.0), beta*1.0))
            if tau[i]<0.0001:
                tau[i]=0.0001
            elif tau[i] > sys.float_info.max / numNodes*100:
                tau[i] = sys.float_info.max /numNodes * 100
        sum+=tau[i]
        for i in range(numNodes):
            probs[i] = tau[i] / sum

def NextNode(k,nodeX,visited, pheromones,dist):
    probs = [0]*numNodes
    Probability(k,nodeX,visited,pheromones,dist,probs)
    cum = [0]*(numNodes+1)
    cum[0] = 0.0
    for i in range(numNodes):
        cum[i+1] = cum[i]+probs[i]
    p = random.uniform(0,1)
    for i in range(numNodes):
        if p>=cum[i] and p<cum[i+1]:
            return i

    print("Failure")

def BuildTrail(k,start,pheromones,dist,newTrail):
    visited = [0]*numNodes
    trail = []
    for i in range(numNodes):
        visited[i]=False
    trail.append(start)
    visited[start]=True
    for i in range(numNodes-1):
        nodeX = trail[i]
        next = NextNode(k,nodeX,visited,pheromones,dist)
        trail.append(next)
        visited[next]=True

        if next == 10:
            break
    
    for i in range(len(trail)):
        newTrail.append(trail[i])

def UpdateAnts(ants,pheromones,dist):
    for i in range(numAnts):
        ants[i] = 0
        start = 0
        newTrail = []
        BuildTrail(i,start,pheromones,dist,newTrail)
        for j in range(len(newTrail)):
            ants[i].append(newTrail[j])
                                                          