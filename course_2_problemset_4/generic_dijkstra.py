# Python program for Dijkstra's single source shortest path algorithm. The program is for adjacency matrix representation of the graph
class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	def printSolution(self, dist):
		print("Vertex \t Distance from Source")
		for node in range(self.V):
			print(node, "\t\t", dist[node])
		print(f'dist = {dist}')

	# A utility function to find the vertex with minimum distance value, from the set of vertices not yet included in shortest path tree
	def minDistance(self, dist, sptSet):

		# Initialize minimum distance for next node
		min = 1e7

		# Search not nearest vertex not in the shortest path tree
		for index in range(self.V):
			print("-----")
			print('index = {index}')
			print(f'if     dist[{index}] = {dist[index]}')
			print(f'and if sptSet[{index}] = {sptSet[index]}')
			if dist[index] < min and sptSet[index] == False:
				min = dist[index]
				min_index = index
				print(f'min = {dist[index]}')
				print(f'min_index = {min_index}')
				print("")
		print(f'return index {min_index}')
		return min_index

	# Function that implements Dijkstra's single source shortest path algorithm for a graph represented using adjacency matrix representation
	def dijkstra(self, src):

		dist = [1e7] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):

			# Pick the minimum distance vertex from the set of vertices not yet processed.
			# u is always equal to src in first iteration
			u = self.minDistance(dist, sptSet)

			# Put the minimum distance vertex in the shortest path tree
			sptSet[u] = True

			# Update dist value of the adjacent vertices of the picked vertex only if the current distance is greater than new distance and the vertex in not in the shortest path tree
			for v in range(self.V):
				print(f'u = {u}, v = {v}')
				print(f'if     self.graph[{u}][{v}] = {self.graph[u][v]}')
				print(f'and if sptSet[{v}] = {sptSet[v]}')
				print(f'and if dist[{v}] = {dist[v]}')
				print(f'and if self.graph[{u}][{v}] = {self.graph[u][v]}')
				if (self.graph[u][v] > 0 and sptSet[v] == False and	dist[v] > dist[u] + self.graph[u][v]):
					dist[v] = dist[u] + self.graph[u][v]
					print(f'dist[{v}] = dist[{u}] + self.graph[{u}][{v}]  = {dist[u]} + {self.graph[u][v]} = {dist[u] + self.graph[u][v]}')
				print("-----.....")

		self.printSolution(dist)
		return dist

# Driver program
# g = Graph(9)
# g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
# 		[4, 0, 8, 0, 0, 0, 0, 11, 0],
# 		[0, 8, 0, 7, 0, 4, 0, 0, 2],
# 		[0, 0, 7, 0, 9, 14, 0, 0, 0],
# 		[0, 0, 0, 9, 0, 10, 0, 0, 0],
# 		[0, 0, 4, 14, 10, 0, 2, 0, 0],
# 		[0, 0, 0, 0, 0, 2, 0, 1, 6],
# 		[8, 11, 0, 0, 0, 0, 1, 0, 7],
# 		[0, 0, 2, 0, 0, 0, 6, 7, 0]
# 		]

# g.dijkstra(0)

# This code is contributed by Divyanshu Mehta
n_verticies = 8
positive_infinity = float('inf')
sample_graph = [[positive_infinity for column in range(n_verticies)]
					for row in range(n_verticies)]
for index_73 in range(n_verticies):
	sample_graph[index_73][index_73] = 0
# ,(,,)
edges = [(0,1,0.5),(0,4,0.5),(0,2,1),(1,0,0.5),(1,7,3),(2,1,1),(2,3,1.5),(2,4,2),(3,2,1.5),(3,4,1.5),(4,0,0.5),(4,1,0.5),(4,2,2),(4,3,1.5),(5,6,2),(5,7,2),(6,5,2),(7,1,3),(7,5,2)]
for edge in edges:
	sample_graph[edge[0]][edge[1]] = edge[2]

print(f'sample_graph = ' )
for row in sample_graph:
	print(row)

g = Graph(8)
g.graph = sample_graph
list_of_list = []
for i in range(g.V):
    list_of_list.append(g.dijkstra(i))
print(f'list_of_list = {list_of_list}' )