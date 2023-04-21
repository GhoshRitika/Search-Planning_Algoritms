```
Greedy Search

```
The task is to use greedy hill-climbing search to find minima and solutions to the 10-
queens problem. This problem tries to find a position for all 10 queens on the board where they
cannot attack each other. Reminder, an attack is whenever a queen shares a row, column, or
diagonal with another queen. Here we will provide an initial configuration of the board for the 10-
queens problem, and you are to modify that board with the local minima reached from that starting
board. Here, a single step in the hill-climb is the movement of any one of the queens.

To simplify the problem every initial configuration will have exactly one queen in each column.
We will also require that any intermediate configuration used also has exactly one queen in each
column. This means any step in your hill-climb is the motion of one queen vertically up or down
within her column.

Each board will have the following layout of the x and y coordinates:

![greedy](https://user-images.githubusercontent.com/60728026/233514514-9f3e871f-bfb3-4831-868c-f651fcac313f.png)

The board will be given as a 2D array board[y][x], where x and y are the positions of the board.
Queens are marked with a 1, empty positions are marked with a 0. You are to complete the code
for the function **gradient_search** (board) in the file student_code.py. This function will modify
“board” to be the local minima reached. In addition you will return True if the local minima is also
a solution to the problem, and return False otherwise.

The following Tie breaker was used:

If motion of two or more different queens give the same best reduction in total attacks, choose to
move the queen with the lowest x value. If two or more positions for the same queen give the
same best reduction in total attacks, choose the position with the lowest y value.

Do not move to a new board state unless the total number of attacks are reduced (i.e. don’t move
on ties)

Considerations:
● Queens are considered to have an attack between them even if there is another queen
between them. For example 4 queens in the same row will count as 6 attacks.