import math
import random
import numpy as np
import matplotlib.pyplot as plt
import pprint

pp = pprint.PrettyPrinter()


def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    dx = x1 - x2
    dy = y1 - y2

    dist = math.sqrt((dx*dx) + (dy*dy))
    return(dist)

def closest_point(all_points, new_point):

    best_point = None
    best_distance = None

    for current_point in all_points:
        current_distance = distance(new_point, current_point)
        
        # Include the possibility that best_distance is none
        if best_distance is None or current_distance < best_distance :
            best_distance = current_distance
            best_point = current_point
    return f'Closest point is: {best_point} with distance: {best_distance}'


all_points = [(random.randint(0, 35), random.randint(0, 35)) for i in range(200)]
# Creating X and Y for plotting
x_axis = [x[0] for x in all_points]
y_axis = [y[1] for y in all_points]
plt.scatter(x_axis, y_axis)
closest_point(all_points, (7,0))

k = 2
def build_kdtree(points, depth=0):
    n = len(points)    
    if n <= 0:
        return None    
    axis = depth % k
    # Sorting points by splitting axis
    sorted_points = sorted(points, key = lambda point: point[axis])  
    
    return {
        'point': sorted_points[n // 2],
        # points before splitting point
        'left' : build_kdtree(sorted_points[:n//2], depth + 1),
        # points after splitting point
        'right' : build_kdtree(sorted_points[n//2 + 1:], depth + 1)
        }

kdtree = build_kdtree(all_points)
pp.pprint(build_kdtree(all_points))

# Nearest Neighbors in k-d Tree
def closer_distance(dot, p1, p2):    
    if p1 is None:
        return p2
    if p2 is None:
        return p1
    d1 = distance(dot, p1)
    d2 = distance(dot, p2)
    
    if d1 < d2:
        return p1
    else:
        return p2
    
def nearest_neighbor_kdtree(root, point, depth = 0):
    if root is None:
        return None
    
    axis = depth % k
    
    next_branch = None
    oposite_branch = None
    
    if point[axis] < root['point'][axis]:
        next_branch = root['left']
        oposite_branch = root['right']
    else:
        next_branch = root['right']
        oposite_branch = root['left']  
        
    # If the current point is closer to the selected point than splitting one
    best = closer_distance(point,
                           nearest_neighbor_kdtree(next_branch,
                                                   point,
                                                   depth + 1),
                           root['point'])
    
    # Checking if better value on the other side
    if distance(point, best) > abs(point[axis] - root['point'][axis]):
        
        best = closer_distance(point,
                               nearest_neighbor_kdtree(oposite_branch,
                                                       point,
                                                       depth + 1),
                               best)
    return best
    

nearest_neighbor_kdtree(kdtree,(30,4))
closest_point(all_points,(30,4))
