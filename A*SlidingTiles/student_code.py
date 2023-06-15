import copy

def change_display(board):
    state=[[board[0], board[1], board[2]], [board[3], board[4], board[5]], [board[6],board[7],board[8]]]
    return state

def manhatten(board):
    state = change_display(board)
    original = [(2,2),(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1)]
    current = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    for i in range(3):
        for j in range(3):
            current[state[i][j]]=(i,j)
    distance = 0
    for k in range(1,9):
        orig=original[k]
        cur=current[k]
        distance+= abs(orig[0]-cur[0]) + abs(orig[1]-cur[1])
    return distance

def tie_breaker(board):
    concat=0
    for i in range(9):
        k=8-i
        concat+=board[i]*(10**k)
    return concat

def move(board, action):
    board_copy=copy.deepcopy(board)
    k=0
    #up
    if(action==0):
        k=-3
    #right
    elif(action==1):
        k=1
    #down
    elif(action==2):
        k=3
    #left
    elif(action==3):
        k=-1
    for i in range(9):
        if board_copy[i]==0:
            temp=board_copy[i+k]
            board_copy[i+k]=0
            board_copy[i]=temp
            break
    return board_copy

def validate(board, action):
    state=change_display(board)
    pos = (-1,-1)
    for i in range(3):
        for j in range(3):
            if(state[i][j]==0):
                pos=(i, j)
                break
    if(action==0 and pos[0]==0):
        return 0
    elif(action==1 and pos[1]==2):
        return 0
    elif(action==2 and pos[0]==2):
        return 0
    elif(action==3 and pos[1]==0):
        return 0
    else:
        return 1


#astar search
def astar(board):
    #your code here
    actions=[0, 1, 2, 3]
    expanded=[]
    path_frontier=[[]]
    frontier=[board]
    depth=[0]
    heuristic=[manhatten(board)]
    step=0
    found=False
    # while(len(frontier)!=0):
    while found != True:
    # for k in range(4):
        # print(step)
        step+=1
        min=1000
        for i in range(len(frontier)):
            fn=depth[i]+heuristic[i]
            if(fn==min):
                if tie_breaker(frontier[i])>tie_breaker(state):
                    node=i
                    state=copy.deepcopy(frontier[i])
                    min = fn
            elif(fn<min):
                node=i
                state=copy.deepcopy(frontier[i])
                min = fn
        #checking if the state is goal
        # if manhatten(state)==0:
        # print("fRONTIER", frontier)
        # print("cost list", heuristic)
        # print("current depth", depth)
        # print("paths", path_frontier)
        # print_board(state)
        if state==[1,2,3,4,5,6,7,8,0]:
            found==True
            return depth[node], step, path_frontier[node]
        for a in actions:
            if validate(state, a)==1:
                c=move(state, a)
                if c not in expanded:
                    path=copy.deepcopy(path_frontier[node])
                    # path = path_frontier[node]
                    path.append(a)
                    frontier.append(c)
                    depth.append(depth[node]+1)
                    heuristic.append(manhatten(c))
                    path_frontier.append(path)
        # if(max(depth)>30):
        #     print("too deep")
        #     break
        #remove node
        frontier.pop(node)
        path_frontier.pop(node)
        heuristic.pop(node)
        depth.pop(node)
        expanded.append(state)
        while(state in frontier):
            i = frontier.index(state)
            frontier.pop(i)
            path_frontier.pop(i)
            heuristic.pop(i)
            depth.pop(i)


#graphic print of board, feel free to use, or not
def print_board(board):
    print("\n")
    print("------------")
    print(
        "{:02d}".format(board[0]),
        "|",
        "{:02d}".format(board[1]),
        "|",
        "{:02d}".format(board[2]),
    )
    print("------------")

    print(
        "{:02d}".format(board[3]),
        "|",
        "{:02d}".format(board[4]),
        "|",
        "{:02d}".format(board[5]),
    )
    print("------------")

    print(
        "{:02d}".format(board[6]),
        "|",
        "{:02d}".format(board[7]),
        "|",
        "{:02d}".format(board[8]),
    )
    print("------------")



