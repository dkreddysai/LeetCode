graph = {
  '5' : ['3','7'],
  '3' : ['4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : ['2']
}

visited = []
queue = []

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    m = queue.pop(0)
    print(m,end=" ")

    for k in graph[m]:
      if k not in visited:
        visited.append(k)
        queue.append(k)


print("Following is the Breadth-First Search")
bfs(visited, graph, '5')