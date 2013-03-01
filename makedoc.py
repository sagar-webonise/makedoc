




class Initialize():
	"""
	   Initializing the variables and accepting the required values from user
	"""
	
	root = "/";
	excludeDirectories = []
	def acceptInput(self):
		print "Welcome to the makeDoc Here you goes just give me the following inpputs"
		print "Enter the directory name:"
		self.root = raw_input()
		print "Please enter the name of sub-directories to exclude separated by comma (,)"
		self.excludeDirectories  = raw_input().split(",")

		print self.root
		print self.excludeDirectories

		
if __name__== "__main__":
	init  =Initialize()
	init.acceptInput()

# login for selector and accepting the project directory path


	
