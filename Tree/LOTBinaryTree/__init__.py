#
'''
	reference to
		http://mikegrouchy.com/blog/2012/05/be-pythonic-__init__py.html
		
	[Citation]
		another thing to do is at the package level make subpackages/modules
			available with the __all__ variable.
	
		when the interpreter sees an __all__ variable defined in an __init__.py
		it imports the modules listed in the __all__ variable when you do :
			from package import *
'''
__all__	=	['BinaryTree', 'TestModule']