import common

def Expand(node):
	return [(node[0], node[1]+1), (node[0]+1, node[1]), (node[0], node[1]-1), (node[0]-1, node[1])]

def in_range(node):
	if node[0]<0 or node[1]<0 or node[0]>=common.constants.MAP_HEIGHT or node[1]>=common.constants.MAP_WIDTH:
		return False
	return True

def df_search(map):
	found = False
	# PUT YOUR CODE HERE
	frontier=[]
	path=[]
	ht = common.constants.MAP_HEIGHT
	width = common.constants.MAP_WIDTH
	for y in range(ht):
		for x in range(width):
			if map[y][x]== 2:
				map[y][x]=4
				frontier.append((y,x))
				path.append((y,x))
				exit
	result = dfs(map, path[0], path)
	if result!=False:
		found = True
		# for i in range(len(path)):
		# 	node = path[i]
		# 	map[node[0]][node[1]]=5
	return found

def bf_search(map):
	found = False
	# PUT YOUR CODE HERE
	frontier=[]
	final_path = []
	all_paths = []
	ht = common.constants.MAP_HEIGHT
	width = common.constants.MAP_WIDTH
	for y in range(ht):
		for x in range(width):
			if map[y][x]== 2:
				frontier.append((y,x))
				final_path.append((y,x))
				all_paths.append([(y,x)])
				exit
	x = bfs(map, frontier[0], frontier, final_path.copy(), all_paths, ht, width)
	# print("This is the final path", x)
	# final_path+= x
	if x != None:
		final_path = x
		found = True
		for i in range(len(final_path)):
			node = final_path[i]
			map[node[0]][node[1]]=5

	return found

def dfs(map, node, path):
	if map[node[0]][node[1]]==3:
		map[node[0]][node[1]]=5
		path.append(node)
		return True

	for n in Expand(node):
		if in_range(n)==True:
			if map[n[0]][n[1]]!=1 and map[n[0]][n[1]]!=4:
				if map[n[0]][n[1]]==0:
					map[n[0]][n[1]]=4
				if dfs(map, n, path) != False:
					path.append(node)
					map[node[0]][node[1]]=5
					return True
	return False

def bfs(map, node, fr, path, paths, H, W):
	if map[node[0]][node[1]]==3:
		map[node[0]][node[1]]=4
		return path

	else:
		if(len(fr)==0):						#no more nodes but also no more solutions
			# print("Returning empty", fr)
			return None

		element = fr.pop(0)
		p = paths.pop(0)					#first time just empties it
		map[node[0]][node[1]]=4
		if node[1]+1 < W:
			if map[node[0]][node[1]+1]==0 or map[node[0]][node[1]+1]==3:
				fr.append((node[0], node[1]+1))
				path_r = path.copy()
				path_r.append((node[0], node[1]+1))
				paths.append(path_r)
		if node[0]+1 < H:
			if map[node[0]+1][node[1]]==0 or map[node[0]+1][node[1]]==3:
				fr.append((node[0]+1, node[1]))
				path_d = path.copy()
				path_d.append((node[0]+1, node[1]))
				paths.append(path_d)
		if node[1]-1 >= 0:
			if map[node[0]][node[1]-1]==0 or map[node[0]][node[1]-1]==3:
				fr.append((node[0], node[1]-1))
				path_l = path.copy()
				path_l.append((node[0], node[1]-1))
				paths.append(path_l)
		if node[0]-1 >=0:
			if map[node[0]-1][node[1]]==0 or map[node[0]-1][node[1]]==3:
				fr.append((node[0]-1, node[1]))
				path_u = path.copy()
				path_u.append((node[0]-1, node[1]))
				paths.append(path_u)

		return bfs(map, element, fr, p, paths, H, W)
