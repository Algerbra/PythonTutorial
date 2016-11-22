# 
# reference to http://askubuntu.com/questions/470982/how-to-add-a-python-module-to-syspath
# Definition:
#	module		\\ a module is a single python file with a extension of .py
#	package		\\ a folder containing python files accompanied by a file named __init__.py
#				\\ this .py tells python interpreter it is a package to import modules from.

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('/DGTraversal')
'''	Reference
		http://stackoverflow.com/questions/154443/how-to-avoid-pyc-files
'''
sys.dont_write_bytecode = True

from DGTraversal import *

def main():
	DG_Traversal.main_UGraph_DFS_Traversal()

main()