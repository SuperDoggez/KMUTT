graph = {}
many = int(input("How many point do you want: "))
for l in range(many): 
    key = input("Enter a point: ")
    values = [i for i in input("Enter a path: ").split()]
    graph[key] = values

start = input("Start: ")
stop = input("Stop: ")
n = 0

def dfs_search(start,stop,graph, times = start, path = start):
    global n
    if path.count(times) > 1:
        return
    if times == stop:
        final = [i for i in path]
        if len(final) == len(list(graph.keys())):
            n += 1
            print("Answer",n,":",[i for i in path])
            return
        else:
            return
    for j in graph[times]:
        dfs_search(start,stop,graph,j,path+j)

dfs_search(start,stop,graph)
print("Finished")


