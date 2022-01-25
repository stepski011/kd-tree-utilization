# k-d Tree Utilization

The script provides functions for implementing k-d tree algorithm. The fundamental idea of algorithm is building a tree structured data by secting the space in two regions, containing half of the points of parent region, while splitting axis is alternating by each itteration, building sub parts of the tree.
Depth of the tree is equal to number of times that region was splitted (d%k).

## Functions
Elementary function is computing the closest distance between two nodes, and I've provided a brute force search function for the closest point. Next, building function making k d tree data structure, which is represented with Prettyprint package. The nearest neighbor is recursively finding the optimal solution within the tree.

![alt text](https://www.researchgate.net/profile/Ruben-Gonzalez-Crespo/publication/327289160/figure/fig4/AS:666062085435401@1535812984438/Visualization-of-the-k-d-tree-algorithm.png)
