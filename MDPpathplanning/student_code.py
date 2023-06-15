import common

def compute_next_states(state):
	#south, west, north, east
	next=[(state[0]+1,state[1]), (state[0],state[1]-1), (state[0]-1,state[1]), (state[0],state[1]+1)]
	if state[0]==0:#north direction will bounce back
		next[2]=state #[(state[0]+1,state[1]), (state[0],state[1]+1), (state[0],state[1]), (state[0],state[1]-1)]
	elif state[0]==5:#south direction will bounce back
		next[0]=state
	if state[1]==0:#west direction will bounce back
		next[1]=state
	elif state[1]==5:#east direction will bounce back
		next[3]=state
	# print("current state", state)
	# print("Next states", next)
	#s->w,e; w->s,n; n->e,w; e->n,s
	next_states=[[next[1], next[3]], [next[0], next[2]], [next[1], next[3]], [next[2], next[0]]]
	return next, next_states

def compute_sum(vals):
	sum=0
	for i in range(6):
		for j in range(6):
			sum+=vals[i][j]
	return sum

def deep_copy_list(v1, v2):
	for i in range(6):
		for j in range(6):
			v1[i][j]= v2[i][j]

def drone_flight_planner (map,policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount):
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# access the policies using "policies[y][x]"
	# access the values using "values[y][x]"
	# y between 0 and 5
	# x between 0 and 5
	# function must return the value of the cell corresponding to the starting position of the drone
	error = 10
	values_next=[[0 for x in range(6)] for x in range(6)]
	while(error>0.001):
		# values_next=[[0 for x in range(6)] for x in range(6)]
		for i in range(6):
			for j in range(6):
				if map[i][j]==1: #STARTING 
					start=(i,j)
				if map[i][j]==2: #CUSTOMER
					policies[i][j]=0
					values_next[i][j]=delivery_fee
					# continue
				elif map[i][j]==3: #ENEMY
					policies[i][j]=0
					values_next[i][j]=-dronerepair_cost
					# continue
				else:
					q=[]
					keys, next=compute_next_states((i,j))
					# print(i,j)
					# print("next values", len(keys))
					for key in range(4):
						k=keys[key]
						r=-battery_drop_cost
						n1=next[key][0]
						n2=next[key][1]
						Q = (0.7*(r + (discount*values[k[0]][k[1]])))+(0.15*(r + (discount*values[n1[0]][n1[1]])))+(0.15*(r + (discount*values[n2[0]][n2[1]])))
						q.append(round(Q, 10))
					for key in range(4):
						k=keys[key]
						r=-battery_drop_cost*2
						n1=next[key][0]
						n2=next[key][1]
						Q = (0.8*(r + (discount*values[k[0]][k[1]])))+(0.1*(r + (discount*values[n1[0]][n1[1]])))+(0.1*(r + (discount*values[n2[0]][n2[1]])))
						q.append(round(Q, 10))
					# print("Q values", len(q))
					# print(q.index(max(q))+1)
					# if i==5 and j ==0:
					# 	print("q list", q)
					# 	print("Q max", max(q))
					# 	print("policy", q.index(max(q))+1)
					policies[i][j]=q.index(max(q))+1
					values_next[i][j]=max(q)
		error = abs(compute_sum(values)-compute_sum(values_next))
		# print("Error", error)
		deep_copy_list(values, values_next)

	#find value at starting pont and return that
	return values[start[0]][start[1]]
