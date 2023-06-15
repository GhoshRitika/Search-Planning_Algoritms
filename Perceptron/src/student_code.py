import common

def compute_weighted_sum(f, w):
	sum = 0
	for i in range(common.constants.NUM_FEATURES):
		sum += w[i] * f[i]
	return sum

def predicted_label(weighted_sum):
	if weighted_sum >=0:
		return 1
	else:
		return 0

def part_one_classifier(data_train, data_test):
	# PUT YOUR CODE HERE
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 1
	w = [0, 0, 0]
	not_correct_classes = False
	while not not_correct_classes:
		not_correct_classes = True
		for i in range(common.constants.TRAINING_SIZE):
			#last element of features is bias
			features = [data_train[i][0], data_train[i][1], 1]
			label = data_train[i][2]
			w_sum = compute_weighted_sum(features, w)
			p_label = predicted_label(w_sum)
			if p_label != label:
				not_correct_classes = False
				error = label - p_label
				for j in range(common.constants.NUM_FEATURES):
					w[j] += error*features[j]


	for i in range(common.constants.TEST_SIZE):
		features = [data_test[i][0], data_test[i][1], 1]
		w_sum = compute_weighted_sum(features, w)
		data_test[i][2] = predicted_label(w_sum)
	return  0

def compute_multi_weighted_sum(f, w):
	sum = [0 for x in range(common.constants.NUM_CLASSES)]
	for i, weight in enumerate(w):
		for j in range(common.constants.NUM_FEATURES):
			sum[i] += weight[j] * f[j]
	return sum

def predicted_multi_label(weighted_sum):
	max_w = max(weighted_sum)
	i = weighted_sum.index(max_w)
	return i

def part_two_classifier(data_train, data_test):
	# PUT YOUR CODE HERE
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 8
	f_num = common.constants.NUM_FEATURES
	c_num = common.constants.NUM_CLASSES
	train_num = common.constants.TRAINING_SIZE
	test_num = common.constants.TEST_SIZE
	w=[[0 for x in range(f_num)] for x in range(c_num)]
	not_correct_classes = False
	while not not_correct_classes:
		not_correct_classes = True
		for i in range(train_num):
			features = [data_train[i][0], data_train[i][1], 1]
			label = data_train[i][2]
			w_sum = compute_multi_weighted_sum(features, w)
			p_label = predicted_multi_label(w_sum)
			if p_label!=label:
				not_correct_classes=False
				for j in range(f_num):
					w[p_label][j] -= features[j]
					w[int(label)][j] += features[j]
	for i in range(test_num):
		features = [data_test[i][0], data_test[i][1], 1]
		w_sum = compute_multi_weighted_sum(features, w)
		data_test[i][2] = predicted_multi_label(w_sum)
	return 0
