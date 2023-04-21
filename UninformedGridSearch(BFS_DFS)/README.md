## Uninformed Search

The task in this lab is to create a search algorithm to help a robot find its way to a destination. The robot
exists in a grid world named “map” of size MAP_WIDTH by MAP_HEIGHT, and it can move in all 4
directions (diagonals not allowed) through empty space cells only by steps of exactly 1 cell distance.

The starting location of the robot is marked in map with a number “2” and the goal with a number “3”.
The other two values you can find in the map are “1” for walls and “0” for empty space.

![AI_uninformed](https://user-images.githubusercontent.com/60728026/233513686-5dcd869d-f04e-41cf-a80a-2e0c91f78ff4.png)

There are two main functions:

**df_search** (map) and **bf_search** (map)

The first one uses depth first search and the second one uses breadth first search to find a path from the
robot starting location to the goal. The functions should return a boolean value “true” if the destination
was reached and “false” otherwise. An additional condition is to mark the map with a number “4” in all
explored cells and with a number “5” in the cells that are part of path found.

To make sure everybody arrives to the same results (very important for the automated grader) you must
use the following search order for map[y][x]: First [y][x+1], then [y+1][x], then [y][x-1], and finally [y-1][x]
Search order means order nodes are expanded from the frontier.

No additional python modules or packages were used.

Considerations:

● The starting location of the robot and the destination are part of the path and should be marked with a
“5” in the map.

● All maps will have a maximum of 1 possible path between the starting location and the destination (to
make it easier).

● Unreachable goals are possible.

● There will be no loops in the maps (to make it easier).

● There will always be exactly 1 starting position and 1 goal