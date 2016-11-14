#
# recursive python program for level order traversal of binary tree;
# References: http://stackoverflow.com/questions/6578487/init-as-a-constructor
#

class Node:
	''' a utility function to create a new node;
		we can use Node() as constructor for this class Node
		when create a new instance'''
	def __init__(self, key):
		self._data	=	key
		self._left	=	None
		self._right	=	None


# function to print level order traversal of tree;
def printLevelOrder(root):
	h	=	height(root)
	for i in range(1, h + 1):
		printGivenLevel(root, i)

# print nodes at a given level;
def printGivenLevel(root, level):
	if (root is None):
		return

	if (1 == level):
		print ("%d" % (root._data))

	elif (1 < level):
		printGivenLevel(root._left, level - 1)
		printGivenLevel(root._right, level - 1)

'''compute the height of a tree-- the number of nodes along
the longest path from the root node down to the farthest leaf node;'''
def height(node):
	if (node is None):
		return 0

	else:
		#compute the height of each subtree;
		lheight	=	height(node._left)
		rheight	=	height(node._right)

		#use the larger one;
		if (lheight > rheight):
			return lheight + 1
		else:
			return rheight + 1

# driver program to test above function;
'''
root = Node(1)
root._left = Node(2)
root._right = Node(3)
root._left._left = Node(4)
root._left._right = Node(5)
root._right._left = Node(9)
root._right._right = Node(0)
root._right._left._left = Node(23)
root._right._right._right = Node(32)


printLevelOrder(root)


'''