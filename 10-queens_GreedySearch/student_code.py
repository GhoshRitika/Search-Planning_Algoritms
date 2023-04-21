QUEENS = 10
def attacks(queens):
	attacks = 0
	for i in range(QUEENS-1):
		q1 = queens[i]
		for j in range(i+1, QUEENS):
			q2 = queens[j]
			#check 4 diagonals
			if(abs(q1[0]-q2[0])==abs(q1[1]-q2[1])):
				attacks+=1
			#check rows
			if(q1[0]==q2[0]):
				attacks+=1
	# print("attacks", attacks)
	return attacks

def gradient_search(board):
	#put yor code here
	flag = False
	current_q=[]
	#the queens are filled in order of column 0-9
	for i in range(QUEENS):#columns
		for j in range(QUEENS):#rows
			if (board[j][i]==1):
				current_q.append((j,i))
				board[j][i]=0
	current_attack=attacks(current_q)
	new_state_found=1
	while new_state_found:
		new_state_found=0
		best_state=[(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9)]
		best_attack=attacks(best_state)
		for q in range(QUEENS):
			for r in range(QUEENS):
				if(r!=(current_q[q])[0]):
					new_state=[current_q[0],current_q[1],current_q[2],current_q[3],current_q[4],current_q[5],current_q[6],current_q[7],current_q[8],current_q[9]]
					new_state[q]=(r,current_q[q][1])
					new_attack=attacks(new_state)
					if (new_attack<best_attack):
						best_state=[new_state[0],new_state[1],new_state[2],new_state[3],new_state[4],new_state[5],new_state[6],new_state[7],new_state[8],new_state[9]]
						best_attack=new_attack
		if(best_attack<current_attack):
			new_state_found=1
			current_q=[best_state[0],best_state[1],best_state[2],best_state[3],best_state[4],best_state[5],best_state[6],best_state[7],best_state[8],best_state[9]]
			current_attack=best_attack
	for q in current_q:
		board[q[0]][q[1]]=1

	if (current_attack==0):
		flag=True

	return flag

