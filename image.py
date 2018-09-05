#===========================================#
#Class for images
#===========================================#

class images:
	#Default contructor
	def __init__(self, name = "", path = ""):
		self.name = name
		self.path = path

	#=======================================#
	#Accessor methods

	#Get image name
	def getI_name(self):
		return self.name

	#Get image path
	def getI_path(self):
		return self.path

	#=======================================#
	#Mutator Methods

	#Set image name
	def setI_name(self, name):
		self.name = name

	#Set image path
	def setI_path(self, path):
		self.path = path

	#=======================================#
	#Print Methods

	#Print image name
	def printI_name(self):
		print("Image name: " + self.name)

	#Print image path
	def printI_path(self):
		print("Image path: " + self.path)

	def printAll_I(self):
		self.printI_name()
		self.printI_path()
