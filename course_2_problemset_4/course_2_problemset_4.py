from Vertex import *
from PriorityQueue import *
from matplotlib import pyplot as plt
from DummyGraphClass import *
from DirectedGraphFromImage import *
import cv2

import math 
def fixPixelValues(px):
    # convert the RGB values into floating point to avoid an overflow that will give me wrong answers
    return [ float(px[0]), float(px[1]), float(px[2]) ]

# This is a useful function that given a list of (x,y) values, 
# draw a series of red lines between each coordinate and next to 
# show the path in the image
def drawPath(img, path, pThick=2):
    v = path[0]
    x0, y0 = v[0], v[1]
    for v in path:
        x, y = v[0], v[1]
        cv2.line(img,(x,y), (x0,y0), (255,0,0),pThick)
        x0, y0 = x,y

# This is a useful function that given a list of (x,y) values, 
# draw a series of red lines between each coordinate and next to 
# show the path in the image
def drawPath(img, path, pThick=2):
    v = path[0]
    x0, y0 = v[0], v[1]
    for v in path:
        x, y = v[0], v[1]
        cv2.line(img,(x,y), (x0,y0), (255,0,0),pThick)
        x0, y0 = x,y



# ---------------------------------------------------------------------------------------------------
import os

directory_path = 'C:\\Users\\fred\\Github\\learn_python\\course_2_problemset_4\\'
# You can read png, jpg and other file types 
img = cv2.imread(directory_path + 'maze.png') # read an image from a file using opencv (cv2) library
# you can annotate images 
cv2.circle(img,(5,220), 3, (255,0,0), -1) # add a circle centered at (5, 220) radius 3, color red (RGB: 255,0,0)
cv2.circle(img, (5,5), 3, (0,0,255), -1) # add a circle centered at (5,5) radius 3, color red (RGB: 0,0,255)
plt.imshow(img) # show the image on the screen 
plt.title('Amazing')
# plt.show()
img = cv2.imread(directory_path + 'maze-solution.png') # read an image from a file using opencv (cv2) library
# you can annotate images 
cv2.circle(img,(5,220), 3, (255,0,0), -1) # add a circle centered at (5, 220) radius 3, color red (RGB: 255,0,0)
cv2.circle(img, (5,5), 3, (0,0,255), -1) # add a circle centered at (5,5) radius 3, color red (RGB: 0,0,255)
plt.imshow(img) # show the image on the screen 
plt.title('Amazing Solution ')
# plt.show()



print('Image size (height, width, num layers) is', img.shape)
px = img[145, 67] # img[y,x] is the color of the pixel of x,y
print(px) 
cv2.circle(img, (80, 18), 3, (198,31,4),-1) # Draw a colored circle centered at (80, 18)
px1 = img[18, 80] # It is important to note that rows of the image are y values and columns are x values.
print(px1)
px2 = img[80, 18] # This is important to note that indexing the img data structure takes y, x values.
# Most opencv functions will require (x,y) coordinates for pixel as is natural.
print(px2)



# Example
img = cv2.imread(directory_path + 'maze.png') # read an image from a file using opencv (cv2) library
drawPath(img, [ (15, 15), (150, 15), (150, 85), (75, 85), (75, 195)])
plt.imshow(img) # show the image on the screen 
plt.title('Illustration of drawPath')
# plt.show()

# =================================================================================================

def computeShortestPath( graph, source_coordinates, dest_coordinates):
    # your code here
    # --------------------------------------------------
    # 1. Initialize an empty priority queue `q` (use `PriorityQueue` class)
    temp_PriorityQueue = PriorityQueue()
    loop_bool = True
    min_vertex_object = None

    # 2. Get the source vertex (`source`) using the function `graph.get_vertex_from_coords(i,j)`.
    source_vertex = graph.get_vertex_from_coords(source_coordinates[0],source_coordinates[1])

    # 3. Set the `source.d` field to 0 to indicate that distance of source from source is 0.
    source_vertex.d = 0
    
    # print(f'debug - type source_vertex = {type(source_vertex)}')
    # print(f'debug - source_vertex.x = {source_vertex.x}')
    # print(f'debug - source_vertex.y = {source_vertex.y}')
    # print(f'debug - source_vertex.d = {source_vertex.d}')

    # 4. Add the source vertex to the priority queue (use `insert` method).
    # print(f'debug - len(temp_PriorityQueue.q) = {len(temp_PriorityQueue.q)}')
    temp_PriorityQueue.insert(source_vertex)
    # print(f'debug - len(temp_PriorityQueue.q) = {len(temp_PriorityQueue.q)}')
    
    
    # print(f'debug - temp_PriorityQueue.q return {temp_PriorityQueue.q}')
    # for element in temp_PriorityQueue.q:
    #     print(f'debug - type(element) = {type(element)}')
    #     if element is not None:
    #         print(f'debug - {element.x}, {element.y}, {element.d}')
    
    # print(f'debug --------what is in the graph object------------------- ')
    # # print(f'debug - graph.adj_list = {graph.adj_list}')
    # for element in graph.verts:
    #     print (f'graph.verts - {type(element)},{element}')
    # print("debug ----")
    # for element in graph.adj_list:
    #     print (f'graph.adj_list {type(element)},{element}')
    # print(f'debug - graph.verts = {graph.verts}')
    # print(f'debug --------what is in the graph object------------------- ')

    # 5. While the priority queue is not empty.
    while( len(temp_PriorityQueue.q) > 1 and loop_bool):
        # print(f'debug -----------------------------------------------')
        #   5.1 Get the vertex with minimum value of d and delete it (use `get_and_delete_min` function). Let's call this vertex `u`.
        min_vertex_object = temp_PriorityQueue.get_and_delete_min()
        
        # print(f'debug - min_verticy = ({min_vertex_object.x}, {min_vertex_object.y}), distance = {min_vertex_object.d},{min_vertex_object.processed}, parent = {min_vertex_object.pi}')
        
        # print(f'debug - len(temp_PriorityQueue.q) = {len(temp_PriorityQueue.q)}')
        # print(f'debug - temp_PriorityQueue.q return {temp_PriorityQueue.q}')
        # for element in temp_PriorityQueue.q:
        #     print(f'debug - type(element) = {type(element)}')
        #     if element is not None:
        #         print(f'debug - {element.x}, {element.y}, {element.d}')
        # print("")

        #   5.2 Set the processed field of `u` to True.
        min_vertex_object.processed = True
        temp_each_adjacent_node_in_grap = graph.get_vertex_from_coords(min_vertex_object.x,min_vertex_object.y)
        temp_each_adjacent_node_in_grap.processed = True
        

        #   5.3 If `u` has the same coordinates as destination (use `u.x` and `u.y`) then 
        if min_vertex_object.x == dest_coordinates[0] and min_vertex_object.y == dest_coordinates[1]:
            #   5.3.1 shortest path distance is `u.d` and break from the loop.
            loop_bool = False
        else:
            
            # print(f'debug ====================================================')
            # print(f'type of graph.adj_list = {type(graph.adj_list)}')
            # print(graph.adj_list.keys())
            # for key in graph.adj_list.keys():
            #     temp_list = graph.adj_list.get(key)
            #     print(f'\n--type of temp = {type(temp_list)}')
            #     print(f'--len of temp_list is {len(temp_list)}')
            #     print(f'--key = {key}')

            #     for tuple in temp_list:
            #         print(f'------type = {type(element)}')
            #         print(f'------tuple[0].x = {tuple[0].x}')
            #         print(f'------tuple[0].y = {tuple[0].y}')
            #         print(f'------tuple[0].d = {tuple[0].d}')
            #         print(f'------tuple[0].processed = {tuple[0].processed}')
            #         print(f'------tuple[0].idx_in_priority_queue = {tuple[0].idx_in_priority_queue}')
            #         print(f'------tuple[0].pi (parent) = {tuple[0].pi}')
            #         print(f'------tuple[1] (weight) = {tuple[1]}')
            #         print(f'------')
            # print(f'debug ====================================================')


        #   5.4 For each outgoing edge from `u` to `v` with weight `w`
            temp_graph_adj_list_per_key = graph.get_list_of_neighbors(min_vertex_object)
            if temp_graph_adj_list_per_key != None:
                for each_adjacent_node in temp_graph_adj_list_per_key:
                    #   5.4.1 If `v` is not already processed and `v.d > u.d + w` then 

                    if each_adjacent_node[0].processed == False:
                        # each_adjacent_node[0].d > min_vertex_object.d + each_adjacent_node[1]:
                        # print(f'debug, before update, tuple[0].x = ({each_adjacent_node[0].x}, {each_adjacent_node[0].y}), distance = {each_adjacent_node[0].d}, parent = {each_adjacent_node[0].pi}')
                        #   5.4.1.1 update `v.d` to `u.d + w`. Set `v.pi` to `u`
                        each_adjacent_node[0].d = min_vertex_object.d + each_adjacent_node[1]
                        each_adjacent_node[0].pi = (min_vertex_object.x, min_vertex_object.y)
                        temp_each_adjacent_node_in_grap = graph.get_vertex_from_coords(each_adjacent_node[0].x,each_adjacent_node[0].y)
                        temp_each_adjacent_node_in_grap.d = each_adjacent_node[0].d
                        temp_each_adjacent_node_in_grap.pi = each_adjacent_node[0].pi
                        # print(f'debug, after update, tuple[0].x = ({each_adjacent_node[0].x}, {each_adjacent_node[0].y}), distance = {each_adjacent_node[0].d}, parent = {each_adjacent_node[0].pi}')
                        # print(f'debug ----')
                
                    #   5.4.1.2 If `v` is already not in the priority queue, insert it into the queue
                    # if each_adjacent_node[0].processed == False and ((each_adjacent_node[0].x, each_adjacent_node[0].y)) in processed_node == False:
                    
                    if temp_each_adjacent_node_in_grap.processed == False:
                        # add to PriorityQueue
                        temp_PriorityQueue.insert(temp_each_adjacent_node_in_grap)

                    #   5.4.1.3 Else, use the `update_vertex_weight` method of priority queue with `v` as the argument to make sure that `v` is moved to the appropriate place in the priority queue.
                        temp_PriorityQueue.update_vertex_weight(temp_each_adjacent_node_in_grap)
            
            # print(f'debug - processed_node = {list_processed_node}')
    
    #   6. To get the path, start from the destination vertex and keep taking the parent pointer until we reach the source. Store the sequence of vertices in a path.
    result_path = []
    
    # print(f'debug ====================================================')
    # print(f'type of graph.adj_list = {type(graph.adj_list)}')
    # print(graph.adj_list.keys())
    # for key in graph.adj_list.keys():
    #     temp_list = graph.adj_list.get(key)
    #     print(f'\n--type of temp = {type(temp_list)}')
    #     print(f'--len of temp_list is {len(temp_list)}')
    #     print(f'--key = {key}')

    #     for tuple in temp_list:
    #         print(f'------tuple[0].x = {tuple[0].x}')
    #         print(f'------tuple[0].y = {tuple[0].y}')
    #         print(f'------tuple[0].d = {tuple[0].d}')
    #         print(f'------tuple[0].processed = {tuple[0].processed}')
    #         print(f'------tuple[0].idx_in_priority_queue = {tuple[0].idx_in_priority_queue}')
    #         print(f'------tuple[0].pi (parent) = {tuple[0].pi}')
    #         print(f'------tuple[1] (weight) = {tuple[1]}')
    #         print(f'------')
    # print(f'debug ====================================================')
    # print(f'debug - min_verticy = ({min_vertex_object.x}, {min_vertex_object.y}), distance = {min_vertex_object.d},{min_vertex_object.processed}, parent = {min_vertex_object.pi}')
    
    loop_bool = True
    current_key_x = min_vertex_object.x
    current_key_y = min_vertex_object.y
    result_path = result_path
    while(loop_bool):
        temp_vertex = graph.get_vertex_from_coords(current_key_x,current_key_y)
        result_path = [(current_key_x, current_key_y)] + result_path
        if temp_vertex.pi == None:
            loop_bool = False
        else:
            current_key_x = temp_vertex.pi[0]
            current_key_y = temp_vertex.pi[1]

    #   7. Return the (path, shortest path distance)
    return (result_path,min_vertex_object.d)

print(f'----------------test 1-------------------------------------')
# # Test 1
verts = {(i,j): Vertex(i,j) for i in range(3) for j in range(3)}
adj_list= {}
def connect_nodes(src, dest, weight):
    v1 = src
    v2 = verts[dest]
    if v1 in adj_list:
        adj_list[v1].append((v2, weight))
    else:
        adj_list[v1] = [(v2, weight)]
# Let's build a graph
connect_nodes((0,0),(0,1),1.0)
connect_nodes((0,0),(1,0),0.5)
connect_nodes((1,0),(0,1), 0.5)
connect_nodes((0,1),(0,0), 0.5)
connect_nodes((1,0),(1,1), 0.5)
connect_nodes((1,1), (2,2), 0.25)
connect_nodes((1,1),(1,2), 0.5)
connect_nodes((1,1),(2,1), 1.2)
connect_nodes((2,1), (2,2), 0.25)
connect_nodes((1,2), (2,2), 0.25)
graph = DummyGraphClass(adj_list, verts)

path, dist = computeShortestPath(graph, (0,0), (2,2))
print(path)

assert(dist == 1.25) , ' shortest path distance from (0,0) to (2,2) must be 1.25'
assert (path == [(0,0), (1,0), (1,1), (2,2)])

for (_,v) in verts.items():
    v.reset()

graph2 = DummyGraphClass(adj_list, verts)
(path2, dist2) = computeShortestPath(graph2, (0,0),(1,2))
print(path2)
assert dist2 == 1.5, ' shortest path distance from (0,0) to (1,2) must be 1.5'
assert path2[0] == (0,0)
assert path2[-1] == (1,2)

for (_,v) in verts.items():
    v.reset()

connect_nodes((2,2), (2,1), 0.5)
connect_nodes((2,1), (1,1), 1.0)
connect_nodes((1,1),(0,1), 0.5)


graph3 = DummyGraphClass(adj_list, verts)
(path3, dist3) = computeShortestPath(graph3, (2,2),(0,0))
print(path3)
assert(dist3 == 2.5)
assert(path3[0]== (2,2))
assert(path3[-1] == (0,0))

print('All tests passed: 15 points!')

print(f'----------------test 2-------------------------------------')

img = cv2.imread(directory_path + 'maze.png') # read an image from a file using opencv (cv2) library
# you can annotate images 
cv2.circle(img,(5,220), 3, (255,0,0), -1) # add a circle centered at (5, 220) radius 3, color red (RGB: 255,0,0)
cv2.circle(img, (5,5), 3, (0,0,255), -1) # add a circle centered at (5,5) radius 3, color red (RGB: 0,0,255)
plt.imshow(img) # show the image on the screen 
plt.title('Amazing')
# plt.show()

img = cv2.imread(directory_path + 'maze.png') # read an image from a file using opencv (cv2) library
graph = DirectedGraphFromImage(img)
p,dist = computeShortestPath(graph, (5,220), (5,5))
assert dist <= 78.1, 'Expected shortest path distance must be 78.1'
assert p[0] == (5,220)
assert p[-1] == (5,5)
print('Passed: 10 points!')

drawPath(img, p, 2)
plt.imshow(img) # show the image on the screen 
plt.title('Amazing')
# plt.show()
cv2.imwrite(directory_path + 'maze-solution.png', img)

print(f'----------------test 3-------------------------------------')


# img = cv2.imread(directory_path + 'maze2.JPG') # read an image from a file using opencv (cv2) library
# cv2.circle(img,(250,470), 10, (255,0,0), -1) # add a circle centered at (600, 70) radius 10, color red (RGB: 255,0,0)
# cv2.circle(img, (20,100), 10, (255,0,0), -1) # add a circle centered at (790,200) radius 10, color red (RGB: 255,0,0)
# plt.imshow(img) # show the image on the screen 
# plt.title('Amazing 2')
# # plt.show()

# img = cv2.imread(directory_path + 'maze2.JPG') # read an image from a file using opencv (cv2) library
# p, dist = computeShortestPath(DirectedGraphFromImage(img), (250,470), (20,100))
# assert dist <= 120.0
# assert p[0] == (250, 470)
# assert p[-1] == (20,100)
# print('Passed: 10 points!')

# drawPath(img,p)
# plt.imshow(img) # show the image on the screen 
# plt.title('Amazing2')
# plt.show()

# img = cv2.imread(directory_path + 'maze3.JPG')
# cv2.circle(img,(70,1750), 15, (255,0,0), -1) # add a circle centered at (600, 70) radius 10, color red (RGB: 255,0,0)
# cv2.circle(img, (900,500), 15, (0,255,255), -1) # add a circle centered at (790,200) radius 10, color red (RGB: 255,0,0)
# plt.imshow(img) # show the image on the screen 
# plt.title('Amazing 3')
# plt.show()

