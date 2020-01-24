def isSafe(x,y,maze):
    if(x >= 0 and y >= 0 and x < len(maze) and y < len(maze) and maze[x][y] == 1):
        return True
    return False

def printSolution(solution):
    print solution

def solveMazeutil(maze, solution, cur_x, cur_y, n):
    if cur_x == (n-1) and cur_y == (n-1):
        return True

    move_x = [1, 0]
    move_y = [0, 1]

    for i in range(2):
        new_x = cur_x + move_x[i]
        new_y = cur_y + move_y[i]
        if (isSafe(new_x, new_y, maze)):
            solution[new_x][new_y] = 1
            if (solveMazeutil(maze, solution, new_x, new_y, n)):
                return True

            solution[new_x][new_y] = 0

    return False


def solveMaze(maze):
    n = len(maze)
    solution = [[0 for j in range(n)] for i in range(n)]
    solution[0][0] = 1
    if maze[0][0] == 0:
        print "Path not possible since starting position is blocked"
        return False

    if not solveMazeutil(maze, solution, 0, 0, n):
        print "path not possible"
        return False
    else:
        printSolution(solution)
        return True


if __name__ == "__main__":
    # Initialising the maze
    maze = [ [1, 0, 0, 0],
             [1, 1, 0, 1],
             [0, 1, 0, 0],
             [1, 1, 1, 1] ]

    print solveMaze(maze) 
