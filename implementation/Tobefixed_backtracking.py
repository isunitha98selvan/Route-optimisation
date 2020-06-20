   
# from distances import distances
from temp import distances
   
all_paths = []

def dfs(source,dest,numNodes):
	printAllPaths(source, dest,numNodes)
	
def findPath(source, dest, visited, path): 
  
    # Mark the current node as visited and store in path 
    visited[source]= True
    path.append(source) 

    # If current vertex is same as destination, then print path
    if source == dest: 
        print(path)
        all_paths.append(path)
        print(all_paths)
    else: 
    # If current vertex is not destination Recur for all the vertices adjacent to this vertex 
        for i in range(len(distances[source])): 
            if visited[i]==False and distances[source][i]!=0: 
                findPath(i, dest, visited, path) 
                      
        # Remove current vertex from path[] and mark it as unvisited 
    path.pop() 
    visited[source]= False

def calculatePathDistance(path):
	dist = 0
	for i in range(len(path)-1):
		dist += distances[path[i]][path[i+1]]
	return dist
# Prints all paths from 's' to 'd' 
def printAllPaths(source, dest, numNodes): 
  
    # Mark all the vertices as not visited 
    visited =[False]*(numNodes) 
  
    # Create an array to store paths 
    path = [] 
  
     # Call the recursive helper function to print all paths 
    findPath(source, dest,visited, path) 
   
   
# Create a graph given in the above diagram 

s = 2 ; d = 3
print("Following are all different paths from %d to %d :" %(s, d)) 
(dfs(s, d,4))
