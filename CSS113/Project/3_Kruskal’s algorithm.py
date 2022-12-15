def kruskal(g):
  mst = []
  edges = sorted(g['edges'], key=lambda x: x[2])


  connected_components = []
  for node in g['nodes']:
    connected_components.append({node})


  for edge in edges:

    a = None
    b = None
    for component in connected_components:
      if edge[0] in component:
        a = component
      if edge[1] in component:
        b = component

    if a != b:
      mst.append(edge)
      connected_components.remove(a)
      connected_components.remove(b)
      connected_components.append(a.union(b))

  return mst

g = {}

edgeslist = []
input_nodes = [i for i in input("Name node is: ").split()]
while True:
    edges = tuple(input("Enter a edges (or press Enter to stop): "))
    if edges  == ():
        break
    edgeslist.append(edges)

g["nodes"] = input_nodes
g["edges"] = edgeslist

mst = kruskal(g)

ans = 0
preans = []
for j in mst:
    preans.append(j[2])
for k in preans:
    ans += int(k)

print(mst)
print("minimum spanning tree: ",ans)

