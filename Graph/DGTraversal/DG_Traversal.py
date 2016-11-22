# 
# Reference
#	http://www.geeksforgeeks.org/depth-first-traversal-for-a-graph/
#
#
# Python Program to print DFS traversal from a given path.
# reference to http://askubuntu.com/questions/470982/how-to-add-a-python-module-to-syspath
# Definition:
#	module		\\ a module is a single python file with a extension of .py
#	package		\\ a folder containing python files accompanied by a file named __init__.py
#				\\ this .py tells python interpreter it is a package to import modules from.
#
import os
from collections import defaultdict

# class for a directed graph with Adjacency List Representation
class	Graph:
	# constructor function
	def	__init__(self):
		#default dictionary to store graph..
		self.graph	=	defaultdict(list)
		
	#function to add an Edge to Graph
	def	addEdge(self, u, v):
		self.graph[u].append(v)
		
	# function used by DFS for inner recur calling.
	def	DFSUtil(self, v, visited):
		# mark the current node as visited before.
		visited[v]	=	True
		print (v),
		
		# recur for all the vertices adjacency to this EXACT vertex..
		for	i in self.graph[v]:
			if (False == visited[i]):
				self.DFSUtil(i, visited)
				
	# DFS-Traversal with usage of DFSUtil() function..
	def	DFS(self, v):
		# marked all the vertices as false visited...
		visited	=	[False] * (len(self.graph))
		
		# call the recursive helper function to print DFS-Traversal..
		self.DFSUtil(v, visited)
		
	# Function to print a Breadth First Search of Directed-Graph..
	def breadth_first_search(self, Vert):
		# initialize marking block storage.
		visited = [False] * (len(self.graph))
		
		# create a queue for breadth-first-search
		tQueue	=	[]
		# Visited Marking and Enqueue Pushing
		visited[Vert]	=	True
		tQueue.append(Vert)
		
		while (tQueue):
			# dequeue THE Vertex from pop_front/print_it.
			Vert	=	tQueue.pop(0)
			print (Vert),
			
			'''	each time after pop_front THE_Vert
				Then following Enqueue_All_Adjacent_Vertices_of_the_dequeued_Vertex
				: if an adjacent has not been visited,
				: then mark it visited and enqueue it. '''
			for i in self.graph[Vert]:
				if (False == visited[i]):
					tQueue.append(i)
					visited[i] = True
					
'''end class Graph'''


''' Driver code / Create a graph given in the above diagram..'''
def main_UGraph_DFS_Traversal():
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)
	print ("%s" %(r'Following is DFS from (starting from vertex 2)'))
	g.DFS(2)
	print
	print ("%s" %(r'Following is Breadth-First-Search from (starting from vertex 2)'))
	g.breadth_first_search(2)
'''
	end main_UGraph_DFS_Traversal
'''