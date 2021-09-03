def line_intersection(line1,line2,nodes):
	#line = [(x1,y1),(x2,y2)]
	(x1,y1) = line1[0]
	(x2,y2) = line1[1]
	(x3,y3) = line2[0]
	(x4,y4) = line2[1]

	'''
	if the two line segments share a common point then they touch each other,
	but donot intersect
	'''
	if (line1[0]==line2[0]) or (line1[0]==line2[1]):
		return False
	if (line1[1]==line2[0]) or (line1[1]==line2[1]):
		return False

	'''
	if the slope of both the lines is Infinity(x1==x2 and x3==x4) then the only way 
	they can intersect is if both are the same line
	'''	
	if x1==x2 and x3==x4:
		if x1==x3:
			return True
		return False	

	'''
	if line1 has Infinite slope(x1 == x2) then if line1 intersects with line2 then the pt. of intersection
	would be(x1,y_int) 
	'''	
	if x1 == x2:
		m2 = float((y3-y4))/float((x3-x4)) # slope of line2
		y = m2*x1-m2*x3+y3                 # y cordinate of pt. of intersection
		if (y>=min(y1,y2) and y<=max(y1,y2)) and (y>=min(y3,y4) and y<=max(y3,y4))  :
			if x1<=max(x3,x4) and x1>=min(x3,x4):
				pt_of_intersection = (x1,y)
				if pt_of_intersection in nodes:
					return False 
				#print pt_of_intersection	
				return True   # point of intersection does exist and not on a node	
		return False

	'''
	if line1 has Infinite slope(x3 == x4) then if line1 intersects with line2 then the pt. of intersection
	would be(x3,y_int) 
	'''	
	if x3 == x4:
		m1 = float((y1-y2))/float((x1-x2)) # slope of line1
		y = m1*x3-m1*x1+y1                 # y cordinate of pt. of intersection
		if (y>=min(y1,y2) and y<=max(y1,y2)) and (y>=min(y3,y4) and y<=max(y3,y4)):
			if x3<=max(x1,x2) and x3>=min(x1,x2):
				pt_of_intersection = (x3,y)
				if pt_of_intersection in nodes:
					return False
				#print pt_of_intersection	
				return True   # point of intersection does exist and not on a node	
		return False	


	m1 = float((y1-y2))/float((x1-x2)) # slope of line1
	m2 = float((y3-y4))/float((x3-x4)) # slope of line2
	if m1==m2:
		if (-m1*x1+y1) == (-m2*x3+y3): # slope and intercept of both the lines is same or same line
			if (((x1,y1) == (x3,y3)) or ((x1,y1) == (x3,y3))) or (((x1,y1) == (x3,y3)) or ((x1,y1) == (x3,y3))):
				return True #  both lines may be same but the line segment also have to touch each other for intersection
		return False # no line intersection as slope is same and intercepts are different

	x = float((y3-m2*x3-y1+m1*x1))/float((m1-m2))
	y = m1*x -m1*x1+y1	
	if (x>=min(x1,x2) and x<=max(x1,x2)) and (x>=min(x3,x4) and x<=max(x3,x4)):  
		if (y>=min(y1,y2) and y<=max(y1,y2)) and (y>=min(y3,y4) and y<=max(y3,y4)):
			#print (x,y)
			return True

	return False # lines intersect but line segment donot	

def finding_neighbours(pt,nodes,lines):
	edges = []
	edges.append(pt)
	flag = 0
	for node in nodes:
		if pt == node:
			continue
		for line in lines:
			new_line = [pt,node]
			#print 'checking intersection between ',new_line,' and ',line
			if line_intersection(new_line,line,nodes):
				#print 'intersection'
				flag = 1
				break
			else:
				pass
				#print 'no intersection'
		if flag == 0:           # no intersection
			if node not in edges:
				edges.append(node)	
		if flag==1: flag = 0   # there has been an intersection			


	return edges				

def main():
	inf = float("9e999")
	l = [[(2,4),(2,2)],[(2,2),(4,2)],[(4,2),(4,4)],[(4,4),(2,4)],[(5,4),(5,2)],[(5,2),(7,2)],[(7,2),(7,4)],[(7,4),(5,4)]
	   ,[(8,6),(8,3)],[(8,3),(9,3)],[(9,3),(9,6)],[(9,6),(8,6)],[(5,9),(5,6)],[(5,6),(7,6)],[(7,6),(7,9)],[(7,9),(5,9)]]
	obstacle_nodes = [(2,2),(4,2),(4,4),(2,4),(5,2),(7,2),(7,4),(5,4),(8,3),(9,3),(9,6),(8,6),(5,6),(7,6),(7,9),(5,9)]
	nodes = [(1,3),(2,2),(4,2),(5,2),(7,2),(6,1),(8,3),(9,3),(9,6),(8,6),(7,4),(5,4),(4,4),(2,4),(5,6),(7,6),
	        (10,8),(7,9),(5,9),(4,8),(1,8)]
	#nodes = [(1,3),(2,2),(4,2),(5,2),(7,2),(8,3),(9,3),(9,6),(8,6),(7,4),(5,4),(4,4),(2,4),(5,6),(7,6),(7,9),(5,9),(1,8)]
	#obstacle_nodes = []

	list_of_neighbours = [] # stores the list of neighbours(where the first node in each neighbour is the primary node or should be the key of the graph)
	for pt in nodes:
		list_of_neighbours.append(finding_neighbours(pt,nodes,l))

	temp = [(),inf]
	graph={}
	for neighbour in list_of_neighbours:
		graph[neighbour[0]] = neighbour[1:]
		graph[neighbour[0]].extend(temp) 
	#print graph 
	print graph[(6,1)]

	#print line_intersection(l1,l2)

if __name__ == '__main__':
	main()	

