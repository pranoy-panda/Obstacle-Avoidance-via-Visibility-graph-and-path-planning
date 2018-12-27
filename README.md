## Obstacle Avoidance via Visibility graph and path planning
### (Note: Yellow blocks are objects to be visited, White blocks are the obstacles, Red block is the start node, Green block is the end node)
Visibility-graph is a graph of inter visible locations, typically for a set of
points and obstacles in the Euclidean plane. Each node in the graph
represents a point location, and each edge represents a visible 
connection between them. That is, if the line segment connecting
two locations does not pass through any obstacle, an edge is drawn
between them in the graph.

[image1]: ./input.JPG 
[image2]: ./result.png 

| First Header  | Second Header |
| ------------- | ------------- |
| ![](./input.JPG )  | ![](./result.png )   |

# Input image
![alt text][image1]

# Result
![alt text][image2]
