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
	def minDistance(self, accumulated_distance, bool_list):

		# Initialize minimum distance for next node
		min = 1e7

		# Search not nearest vertex not in the shortest path tree
		for index in range(self.V):
			print("----------")
			print(f'index = {index}')
			print(f'if     accumulated_distance[{index}] {accumulated_distance[index]} < {min}')
			print(f'and if bool_list[{index}] {bool_list[index]} == False')
			if accumulated_distance[index] < min and bool_list[index] == False:
				min = accumulated_distance[index]
				min_index = index
				print(f'min = {accumulated_distance[index]}')
				print(f'min_index = {min_index}')
				print("")
		print(f'\nreturn index {min_index}')
		return min_index

	# Function that implements Dijkstra's single source shortest path algorithm for a graph represented using adjacency matrix representation
	def dijkstra(self, src):

		accumulated_distance = [1e7] * self.V
		accumulated_distance[src] = 0
		bool_list = [False] * self.V

		for cout in range(self.V):

			# Pick the minimum distance vertex from the set of vertices not yet processed.
			# u is always equal to src in first iteration
			u = self.minDistance(accumulated_distance, bool_list)

			# Put the minimum distance vertex in the shortest path tree
			bool_list[u] = True

			# Update dist value of the adjacent vertices of the picked vertex only if the current distance is greater than new distance and the vertex in not in the shortest path tree
			for v in range(self.V):
				print("-----.....")
				print(f'u = {u}, v = {v}')
				print(f'if     self.graph[{u}][{v}] {self.graph[u][v]} > 0')
				print(f'and if bool_list[{v}] {bool_list[v]} == False')
				print(f'and if accumulated_distance[{v}] {accumulated_distance[v]} > self.graph[{u}][{v}] {self.graph[u][v]}')
				if (self.graph[u][v] > 0 and bool_list[v] == False and	accumulated_distance[v] > accumulated_distance[u] + self.graph[u][v]):
					accumulated_distance[v] = accumulated_distance[u] + self.graph[u][v]
					print(f'accumulated_distance[{v}] {accumulated_distance[v]} = accumulated_distance[{u}] + self.graph[{u}][{v}]  = {accumulated_distance[u]} + {self.graph[u][v]} = {accumulated_distance[u] + self.graph[u][v]}')
				

		self.printSolution(accumulated_distance)
		return accumulated_distance

"""
 Here is an outline of Dijkstra's algorithm with modifications that may be useful.
 
 ~~~
 1. Initialize an empty priority queue `q` (use `PriorityQueue` class)
 2. Get the source vertex (`source`) using the function `graph.get_vertex_from_coords(i,j)`.
 3. Set the `source.d` field to 0 to indicate that distance of source from source is 0.
 4. Add the source vertex to the priority queue (use `insert` method).
 5. While the priority queue is not empty.
    5.1 Get the vertex with minimum value of d and delete it (use `get_and_delete_min` function). Let's call this vertex `u`.
    5.2 Set the processed field of `u` to True.
    5.3 If `u` has the same coordinates as destination (use `u.x` and `u.y`) then 
        5.3.1 shortest path distance is `u.d` and break from the loop.
    5.4 For each outgoing edge from `u` to `v` with weight `w`
        5.4.1 If `v` is not already processed and `v.d > u.d + w` then 
              5.4.1.1 update `v.d` to `u.d + w`. Set `v.pi` to `u`.
              5.4.1.2 If `v` is already not in the priority queue, insert it into the queue
              5.4.1.3 Else, use the `update_vertex_weight` method of priority queue with `v` as the argument to make sure that `v` is moved to the appropriate place in the priority queue.
 6. To get the path, start from the destination vertex and keep taking the parent pointer until we reach the source. Store the sequence of vertices in a path.
 7. Return the (path, shortest path distance)
"""

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