import common

def minmax_tictactoe(board, turn):
	#put your code here:
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);
	result = minimax(board, turn)
	if(result==1):
		return common.constants.X
	elif(result==-1):
		return common.constants.O
	else:
		return common.constants.NONE

def abprun_tictactoe(board, turn):
	#put your code here:
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);
	result = prune(board, turn, -10000, 10000)
	if(result==1):
		return common.constants.X
	elif(result==-1):
		return common.constants.O
	else:
		return common.constants.NONE

def minimax(board, turn):
	r=common.game_status(board)
	if(r==1):
		return 1	#winner X
	elif(r==2):
		return -1	#winner O
	elif(0 not in board):
		return 0	#Tie
	#maxi
	if(turn==common.constants.X):
		v=-10000
		for l in range(9):
			if(board[l]==0):
				board[l]=common.constants.X
				r_val=minimax(board, common.constants.O)
				board[l]=0
				if r_val>v:
					v=r_val
		return v
	#mini
	if(turn==common.constants.O):
		v=10000
		for l in range(9):
			if(board[l]==0):
				board[l]=common.constants.O
				r_val=minimax(board, common.constants.X)
				board[l]=0
				if r_val<v:
					v=r_val
		return v

def prune(board, turn, alpha, beta):
	r=common.game_status(board)
	if(r==1):
		return 1	#winner X
	elif(r==2):
		return -1	#winner O
	elif(0 not in board):
		return 0	#Tie
	#maxi
	if(turn==common.constants.X):
		v=-10000
		for l in range(9):
			if(board[l]==0):
				board[l]=common.constants.X
				r_val=prune(board, common.constants.O, alpha, beta)
				board[l]=0
				if r_val>v:
					v=r_val
				if v>=beta:
					return v
				if v>alpha:
					alpha=v
		return v
	#mini
	if(turn==common.constants.O):
		v=10000
		for l in range(9):
			if(board[l]==0):
				board[l]=common.constants.O
				r_val=prune(board, common.constants.X, alpha, beta)
				board[l]=0
				if r_val<v:
					v=r_val
				if v<=alpha:
					return v
				if v<beta:
					beta=v
		return v

