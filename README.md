Project 1: A* Pathfinding Exploration
Garrett Zhou
Due 9/17/26

## Overview
This project is for Mr. Cochran's ADV CS III: AI and Machine Learning class at Durham Academy. 
This is an A* pathfinding algorithm project where the user can start the program and a blank grid will show up.
The user will be able to choose the start and end nodes for the A* pathfinding program, and then they will be able
to create walls that the program must navigate around, as well as mud patches that have higher edge costs compared to normal nodes (triple the cost). While running, the program will use A* to find the fastest/most efficient
path between the start node and the goal node.
I used python in Pycharm for this project, and I used 4 libraries:
pygame (for the UI and graphics), math (for the calculations required to find the cost of each path), 
heapq (managing the different paths explored and keeping track of the most efficient one), and time (for my additional timer in the header).
The problem that A* solves is the knowledge of where the goal is and approximately how far the goal is from the current node,
something that both Dijkstra and BFS do not have. This is called A*'s heuristic. 
Pathfinding is a simple and applicable example of a search algorithm. 
This can be used in many different scenarios such as autonomous navigation or resource optimization across both digital and physical systems.
Pathfinding allows computers to evaluate millions of possible routes to find the most efficient one based on pre-determined factors.
The key features of my project include all 3 heuristics with the ability for the user to switch between them easily, 
a reset button that allows the user to reset the program at the end of every run, 
a timer to allow the user to track how long each program takes for certain setups, a cost tracker variable that tracks the cost of the optimal path, a heading above the actual grid showing the current heuristic, time, and cost with a line separating the grid and the header, and the ability for the user to draw both walls (the algorithm must go around) and mud (cost is 3x more than a normal node)
## How A* works - basic background
A very basic pathfinding algorithm is called Breadth-First-Search (BFS) that explores every node in each layer before moving on to the next layer. 
It's very simple to implement and is guaranteed to find the quickest path BASED ON NUMBER OF EDGES EXPLORED; it does not take into consideration edge weights.
For example, some edges may be more costly than others, but BFS doesn't account for that. 
Building on that, a slightly more advanced pathfinding algorithm is called Dijkstra. Dijkstra builds on BFS by incorporating edge weights into its cost-benefit analysis
of each node. It is also guaranteed to find the quickest path if one exists, but it has one key flaw; it doesn't know where the goal and has no sense of direction.
In that sense, Dijkstra can be incredibly wasteful by exploring paths in the opposite direction of the goal. It works by having a priority queue based on g(n) that ensures 
that once a node is popped, no unvisited node can lead to a cheaper path since any other path costs at least as much as the current g(n) (greedy property). Then, the
node is settled and its neighbors are checked for cheaper paths.
A* is the best of both algorithms. At each step, it calculates a value f(n) = g(n) + h(n) for each neighboring node, where g(n) is the cost to get from the starting point
to the current node and h(n) is the estimated cost to get from the current node to the finish (this is called a heuristic - educated guess).
## Heuristics
There are 3 main types of heuristics: Diagonal (Chebyshev), Manhattan, and Euclidean. The diagonal heuristic can go in 8 directions like a king on a chessboard and the formula to calculate 
it is: Max(abs[x1 - x2], abs[y1 - y2]) where (x1, y1) are the coordinates of the goal node, and (x2, y2) are the coordinates of the current node. 
The manhattan heuristic can only go in 4 directions (1, 0), (0, 1), (-1, 0), (0, -1). The way that you calculate it is: (abs[x1 - x2] + abs[y1 - y2]). Finally, the euclidean 
heuristic is the most complex one. It is calculated using straight-line distance between two points , but on a 2D plane it has the same functionality as the diagonal heuristic. The formula is:
sqrt([x1-x2]^2 + [y1-y2]^2). The most simple heuristic is manhattan, but it's more time consuming since it can't go into as many different directions, which leads it to predict
a higher estimated cost to get to the goal. Euclidean is the most complex to implement but the most efficient in a 3D environment; however, in a 2D environment it behaves the same as the diagonal heuristic. The intermediate, and the most efficient for this project is diagonal. Diagonal behaves the same as euclidean, but is more simple to implement. The only benefit of euclidean is that it is more efficient in a 3D environment, but my grid is 2D. 
## How to run
Python 3.10.2 or higher is required, along with the pygame library (install in terminal with pip install pygame).
To run the program, clone or download the repository, open a terminal in the project folder or open the project in an IDE such as Pycharm, and run python main.py.
## Controls 
Using all of the features in the program is easy. 
The first click on the grid (not the header) after the program is running sets the start (yellow).
The second click sets the goal (blue).
Subsequent clicks or drags can either add walls (program must go around these, black) or mud (cost is triple a normal node, brown).
The user can switch between adding walls and mud by clicking the key "m". 
The user can also switch between the heuristic options by clicking the key "h". 
Then, the user can run A* by hitting the space bar. 
Once the program is done, the header will show the heuristic of choice, the time, and the cost of the path. 
The user can hit the key "r" to reset the program completely and choose new start, goal, wall, and mud nodes, as well as a new heuristic.
A* can only be run once per setup; hit R to reset before running again. This is to fix a bug, which is described in the code.
## Color Legend
White nodes are unexplored
Grey nodes are open (meaning the algorithm knows of the node as a possibility for the optimal path, but it hasn't been fully explored and the cheapest path to get there hasn't been found)
Red nodes are closed (meaning that the algorithm has already explored the node and found the cheapest path to get there)
The optimal path between the start and goal nodes will be shown in green after it is found. 
Black nodes are walls.
Brown nodes are mud.
The start node is yellow.
The goal node is blue. 
## AI Use and Sources
AI Use: Only Flint was used for this project. Here is the link to the chat with Flint I had: https://app.flintk12.com/activities/a-pathfinding-h-26efda/sessions/ac6cc35c-d43b-4962-9871-1109f3e720aa. No other AI tools were consulted or used for this project. In terms of external sources (non-AI) for research:
https://www.geeksforgeeks.org/dsa/a-search-algorithm/
https://www.codementor.io/blog/basic-pathfinding-explained-with-python-5pil8767c1
Sources used for images in the slideshow will be linked on the last slide of the presentation on the slide titled: "Sources"
