
graph = {
'0' : set(['1','2']),
'1' : set(['0','3','4']),
'2' : set(['0']),
'3' : set(['1']),
'4' : set(['2','3'])}

graph1 = {
'1' : set(['2','3']),
'2' : set(['1','4','5']),
'3' : set(['6','7']),
'4' : set(['2']),
'5' : set(['2']),
'6' : set(['3']),
'7' : set(['3','8','9']),
'8' : set(['7']),
'9' : set(['7'])
}

# Обход графа в глубину
def dfs(graph,start,visited = []):
 	visited.append(start)

 	print(graph[start])

 	for v in graph[start]:
 		if v not in visited:
 			visited = dfs(graph,v,visited)
 	return visited

# Обход графа в ширину
def bfs(graph,start,queue = [],visited = []):

	visited.append(start)
	queue.append(start)

	while queue: # Очередь для просмотра вершин следующего уровня
		#print(queue)
		s = queue.pop(0)

		for i in graph[s]:
			if i not in visited:
				visited.append(i)
				queue.append(i) # добавляем узлы в очередь для просотра (следующий уровень обхода)

	return visited

print(bfs(graph1,'1'))

# Вывод программы
# ['1', '2', '3', '4', '5', '7', '6', '8', '9']

	
