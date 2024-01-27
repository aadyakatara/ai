from queue import PriorityQueue
v = int(input("Enter Number of vertices: "))  # Ask for the number of vertices
graph = [[] for i in range(v)]

def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))

def bestFirstSearch(source, target, n):
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, source))
    visited[source] = True
    while not pq.empty():
        u = pq.get()[1]
        print(u, end="")
        if u == target:
            print(" ")
            break
        for v, c in graph[u]:
            if not visited[v]:
                visited[v] = True
                pq.put((c, v))
        print()
   # Input edges
for i in range(v - 1):  # You need v - 1 edges to create a connected graph
    v1, v2, cost = map(int, input().split())
    addedge(v1, v2, cost)

print("Order of vertices included..")
source = int(input("Enter source: "))
target = int(input("Enter target: "))
bestFirstSearch(source, target, v)
