import pytholog as pl
from distances import distances


graph_kb = pl.KnowledgeBase("Shortest path in a network")
arr = []
for i in range(len(distances[0])):
    for j in range(len(distances[0])):
        if distances[i][j] != 0.0 and i!=j:
            route =  "route(" + str(i) + "," + str(j) + "," + str(distances[i][j]) + ")"
            arr.append(route)

arr.append("path(X, Y, P) :- route(X, Y, P)")
arr.append("path(X, Y, P) :- route(X, Z, P2), path(Z, Y, P3), P is P2 + P3")
arr.append("path(X, Y, P) :- route(Y, Z, P2), path(Z, X, P3), P is P2 + P3")
graph_kb(arr)
v1 = str(0)
v2 = str(74)
x, y = graph_kb.query(pl.Expr("path("+v1+"," +v2+", Weight)"), cut = True, show_path = True) ## cut argument to stop searching when a path is found
print(x)
print([x for x in y if str(x) > "Z"]) ## remove weights in the visited nodes
