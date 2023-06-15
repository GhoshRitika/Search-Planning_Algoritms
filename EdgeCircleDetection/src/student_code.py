import common
import math #note, for this lab only, your are allowed to import math

def detect_slope_intercept(image):
	# PUT YOUR CODE HERE
	# access the image using "image[y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# set line.m and line.b
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	H=common.init_space(2001, 2001) #voting space
	img_ht=common.constants.HEIGHT
	img_width=common.constants.WIDTH
	m_range=[x*0.01 for x in range(-1000, 1001)]
	line=common.Line()
	line.m=0
	line.b=0
	for y in range(img_width):
		for x in range(img_ht):
			#checking for black pixels
			if image[y][x] == 0:
				for m in m_range:
					b = -m*x + y
					if -1000 <= b <= 1000:
						b_index = int(round(b)) + 1000
						m_index = int(round(m*100)) + 1000
						H[m_index][b_index] += 1
	maximum_votes = 0
	for m in range(2001):
		for b in range(2001):
			if H[m][b] > maximum_votes:
				maximum_votes = H[m][b]
				line.m = (m - 1000) * 0.01
				line.b = b - 1000
	return line

def detect_circles(image):
	# PUT YOUR CODE HERE
	# access the image using "image[y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	img_ht=common.constants.HEIGHT
	img_width=common.constants.WIDTH
	H=common.init_space(img_ht, img_width) #voting space
	rad = 30
	b_range = [x for x in range(img_ht)]
	for y in range(img_width):
		for x in range(img_ht):
			#checking for black pixels
			if image[y][x] == 0:
				for b in b_range:
					if (rad**2 >= (y - b)**2):
						a = x - (rad**2 - (y - b)**2)**0.5
						if 0 <= a <=200:
							H[int(round(a))][b] += 1
	thresh = 38
	quarters = 0
	for a in range(img_width):
		for b in range(img_ht):
			if H[a][b] > thresh:
				quarters += 1
	return quarters
				