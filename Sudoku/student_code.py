import common

def constraint_check(sudoku, x, y, v):
	# print(v)
	for i in range(9):
		if sudoku[i][y]==v:
			# print("row not satisfied")
			return False
	for j in range(9):
		if sudoku[x][j]==v:
			# print("column not satisfied")
			return False
	if x<3:
		if y<3:
			for i in range(3):
				for j in range(3):
					if sudoku[i][j]==v:
						# print("0 not satisfied", sudoku[i][j], i, j)
						return False
		if y>=3 and y<6:
			for i in range(3):
				for j in range(3,6):
					if sudoku[i][j]==v:
						# print("1 not satisfied", sudoku[i][j], i, j)
						return False
		if y>=6:
			for i in range(3):
				for j in range(6,9):
					if sudoku[i][j]==v:
						# print("2 not satisfied", sudoku[i][j], i, j)
						return False
	if x>=3 and x<6:
		if y<3:
			for i in range(3, 6):
				for j in range(3):
					if sudoku[i][j]==v:
						# print("3 not satisfied", sudoku[i][j], i, j)
						return False
		if y>=3 and y<6:
			for i in range(3, 6):
				for j in range(3,6):
					if sudoku[i][j]==v:
						# print("4 not satisfied", sudoku[i][j], i, j)
						return False
		if y>=6:
			for i in range(3, 6):
				for j in range(6,9):
					if sudoku[i][j]==v:
						# print("5 not satisfied", sudoku[i][j], i, j)
						return False
	if x>=6:
		if y<3:
			for i in range(6, 9):
				for j in range(3):
					if sudoku[i][j]==v:
						# print("6 not satisfied", sudoku[i][j], i, j)
						return False
		if y>=3 and y<6:
			for i in range(6, 9):
				for j in range(3,6):
					if sudoku[i][j]==v:
						# print("7 not satisfied", sudoku[i][j], i, j)
						return False
		if y>=6:
			for i in range(6, 9):
				for j in range(6,9):
					if sudoku[i][j]==v:
						# print("8 not satisfied", sudoku[i][j], i, j)
						return False
	return True


def update_domain(dom, x, y, v, sudoku):
	for i in range(9):
		for j in range(9):
			if sudoku[i][j]==0:
				dom[i][j]=[]
				for k in range(1,10):
					if constraint_check(sudoku, i, j, k):
						dom[i][j].append(k)
			if dom[i][j] == [] and sudoku[i][j]==0:
				return False
	return True


def complete(sudoku):
	for i in range(9):
		for j in range(9):
			if sudoku[i][j]==0:
				return False
	return True

def find_locations(sudoku):
	for i in range(9):
		for j in range(9):
			if sudoku[i][j]==0:
				return (i,j)

def BT(sudoku):
	variables.counter +=1
	if complete(sudoku):
		return True
	else:
		(x,y) = find_locations(sudoku)
		for v in range(1,10):
			if constraint_check(sudoku, x, y, v):
				sudoku[x][y]=v
				r=BT(sudoku)
				if r is True:
					return True
				else:
					sudoku[x][y]=0
		return False

def FwdCheck(sudoku, domain):
	variables.counter +=1
	if complete(sudoku):
		print("complete")
		return True
	else:
		(x,y) = find_locations(sudoku)
		for v in range(1,10):
			if constraint_check(sudoku, x, y, v):
				old_domain=[[[] for x in range(9)] for x in range(9)]
				for i in range(9):
					for j in range(9):
						old_domain[i][j]=domain[i][j]
				sudoku[x][y]=v
				D=update_domain(domain, x, y, v, sudoku)
				if D is True:
					r=FwdCheck(sudoku, domain)
					if r is True:
						return True
				sudoku[x][y]=0
				for i in range(9):
					for j in range(9):
						domain[i][j]=old_domain[i][j]
		return False

#helpful, but not needed
class variables:
	counter=0

def sudoku_backtracking(sudoku):
	variables.counter = 0
	r=BT(sudoku)
	return variables.counter

def sudoku_forwardchecking(sudoku):
	variables.counter = 0
	# dom=[[[0 for x in range(9)] for x in range(9)] for x in range(9)]
	dom=[[[x for x in range(1,10)] for x in range(9)] for x in range(9)]
	r=FwdCheck(sudoku, dom)
	#put your code here
	return variables.counter
