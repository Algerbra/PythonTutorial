# 
# reference to http://askubuntu.com/questions/470982/how-to-add-a-python-module-to-syspath
# Definition:
#	module		\\ a module is a single python file with a extension of .py
#	package		\\ a folder containing python files accompanied by a file named __init__.py
#				\\ this .py tells python interpreter it is a package to import modules from.
#
#	$PYTHONPATH	\\ by default python-interpreter looks for its modules and packages in $PYTHONPATH
#				\\ to find what is included in $PYTHONPATH, run the code (python-2.7 python-3)
#				\\			import sys
#				\\			print (sys.path)
#
# other reference maybe useful
#	[0] http://stackoverflow.com/questions/4383571/importing-files-from-different-folder-in-python
# 	[1]What is a packages and its purposes?
#		referencing to https://docs.python.org/3/tutorial/modules.html#packages
#	[2]# What is the __init__.py for ?
#		referencing to http://mikegrouchy.com/blog/2012/05/be-pythonic-__init__py.html
#
'''	for the following 3-code-lines you can reference to 
	http://stackoverflow.com/questions/3828723/why-should-we-not-use-sys-setdefaultencodingutf-8-in-a-py-script	'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

''' the appended Module-Path ('/LOTBinaryTree') is relative to current module, i.e. main.py
	you can also reference to the usage of sys.path.insert(.)'''
sys.path.append('/LOTBinaryTree')

''' import the Modules in the directory of (Tree/LOTBinaryTree), 
		i.e. the BinaryTree.py and TestModule.py files
	After operations above we can reference to the class, function, and variables
	defined in those Modules, i.e. in the LOTBinaryTree.py and TestModule.py files.
	Also donot forget the namespace, i.e. the Module name BinaryTree and the TestModule	'''
from LOTBinaryTree import *

def main():
	root 					= BinaryTree.Node(1)
	root._left 				= BinaryTree.Node(2)
	root._right 			= BinaryTree.Node(3)
	root._left._left 		= BinaryTree.Node(4)
	root._left._right 		= BinaryTree.Node(5)
	root._left._left._left 	= BinaryTree.Node(9)
	root._right._left 		= BinaryTree.Node(21)
	root._right._right 		= BinaryTree.Node(23)
	BinaryTree.printLevelOrder(root)

main()
TestModule.print_sentence()	#modules defined by TestModule.py
print sys.path	#list all the modules in $PYTHONPATH