import math
def dijstra_short_path(start,end,graph):
	to_be_visited_list = []
	graph[start][-1] = 0   # setting start node's distance from itself = 0
	to_be_visited_list.append(start)
	while len(to_be_visited_list)!=0:
		current,_ = node_with_short_dist(to_be_visited_list,graph)
		to_be_visited_list.remove(current)         # remove current from the list
		for neighbour in graph[current][:-2]:
			if graph[neighbour][-1] > (graph[current][-1] + length_of_edge(neighbour,current)):
				graph[neighbour][-1] = (graph[current][-1] + length_of_edge(neighbour,current))
				graph[neighbour][-2] = current
				if neighbour not in to_be_visited_list:
					to_be_visited_list.append(neighbour)
	#print graph
	parent = graph[end][-2]
	path = []
	path.append(end)
	while len(parent)!=0:
		path.append(parent)
		parent = graph[parent][-2]

	first_node = path[0]
	total_cost = 0
	for node in path[1:]:
		second_node = node
		total_cost+=length_of_edge(first_node,second_node)
		first_node = second_node	
	#print 'path from start node to end node is:'
	return path,total_cost	

def node_with_short_dist(to_be_visited_list,graph):
	minimum = graph[to_be_visited_list[0]][-1]
	node = to_be_visited_list[0]
	for elem in to_be_visited_list:
		if minimum > graph[elem][-1]:
			minimum = graph[elem][-1]
			node = elem		
	return node,minimum		

def length_of_edge(destination,source):
	length = math.sqrt((destination[0]-source[0])**2 + (destination[1]-source[1])**2)
	return length

def generate_edges(graph):
	edges = []
	for node in graph: # iterating over the keys
		for neighbour in graph[node][:2]:  # iterating over the neighbours of the node
			cost_of_edge = math.sqrt((neighbour[0]-node[0])**2 + (neighbour[1]-node[1])**2)
			edges.append([node,neighbour,cost_of_edge])	
	return edges		

def main():
	inf = float("9e999")
	# here we are discussing undirected graphs

	# here I have represented graph as a dictionary, where the keys are the nodes and their corresponding
	# values are the neighbours of the key
	# for eg. in the below given graph, 'a' is a node and 'c' is its only neighbour

	# node--> (1,1), its neighbours--> (2,2),(1,3), distance from start node-->inf, parent = ()
	graph = { (1,1) : [(2,2),(1,3),(),inf], #[neighbour,parent,distance from start node]
	          (2,2) : [(1,1),(1,3),(3,1),(5,3),(),inf],
	          (1,3) : [(1,1),(2,2),(),inf],
	          (3,1) : [(2,2),(5,3),(),inf],
	          (5,3) : [(2,2),(3,1),(),inf]
	        }
	start = (1,1)
	end = (5,3)       
	total_cost,path = dijstra_short_path(start,end,graph)

	print path
	print total_cost	
	#edges = generate_edges(graph)
if __name__ == '__main__':
	main()	        

