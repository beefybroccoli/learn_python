from Vertex import *
from PriorityQueue import *
from matplotlib import pyplot as plt
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

def computeShortestPath( graph, source_coordinates, dest_coordinates):
    # your code here
    # --------------------------------------------------
    # 1. Initialize an empty priority queue `q` (use `PriorityQueue` class)
    # 2. Get the source vertex (`source`) using the function `graph.get_vertex_from_coords(i,j)`.
    # 3. Set the `source.d` field to 0 to indicate that distance of source from source is 0.
    # 4. Add the source vertex to the priority queue (use `insert` method).
    # 5. While the priority queue is not empty.
    #   5.1 Get the vertex with minimum value of d and delete it (use `get_and_delete_min` function). Let's call this vertex `u`.
    #   5.2 Set the processed field of `u` to True.
    #   5.3 If `u` has the same coordinates as destination (use `u.x` and `u.y`) then 
    #   5.3.1 shortest path distance is `u.d` and break from the loop.
    #   5.4 For each outgoing edge from `u` to `v` with weight `w`
    #       5.4.1 If `v` is not already processed and `v.d > u.d + w` then 
    #       5.4.1.1 update `v.d` to `u.d + w`. Set `v.pi` to `u`.
    #       5.4.1.2 If `v` is already not in the priority queue, insert it into the queue
    #       5.4.1.3 Else, use the `update_vertex_weight` method of priority queue with `v` as the argument to make sure that `v` is moved to the appropriate place in the priority queue.
    #   6. To get the path, start from the destination vertex and keep taking the parent pointer until we reach the source. Store the sequence of vertices in a path.
    #   7. Return the (path, shortest path distance)
    pass

sample_Vertex = Vertex(0,1)
print(sample_Vertex.x)

sample_priorityqueue = PriorityQueue()
sample_priorityqueue.insert(sample_Vertex)
print(sample_priorityqueue.q)

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