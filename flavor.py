#===========================================#
#Class for flavors
#===========================================#

class flavor:

	#Default contructor
	def __init__(self, size = "", ram = 0, num_disks = 0, num_vcpus = 0):
		self.size = size
		self.ram = ram
		self.num_disks = num_disks
		self.num_vcpus = num_vcpus

	#=======================================#
	#Accessor methods

	#Get size
	def getSize_F(self):
		return self.size

	#Get RAM
	def getRam_F(self):
		return self.ram

	#Get num-disks
	def getDisk_F(self):
		return self.num_disks

	#Get num-vcpus
	def getVcpu_F(self):
		return self.num_vcpus

	#=======================================#
	#Mutator Methods

	#Set size
	def setSize_F(self, size):
		self.size = size

	#Set RAM
	def setRam_F(self, ram):
		self.ram = ram

	#Set num-disks
	def setDisk_F(self, disk):
		self.num_disks = disk

	#Set num-vcpus
	def setVcpu_F(self, vcpu):
		self.num_vcpus = vcpu

	#=======================================#
	#Print Methods

	#Print size
	def printSize_F(self):
		print("Flavor Size: " + self.size)

	#Print RAM
	def printRam_F(self):
		print("RAM: " + str(self.ram) + "GB")

	#Print num-disks
	def printDisk_F(self):
		print("Disk Num: " + str(self.num_disks))

	#Print num-vcpus
	def printVcpu_F(self):
		print("VCPU Num: " + str(self.num_vcpus))

	#Print All
	def printAll_F(self):
		self.printSize_F()
		self.printRam_F()
		self.printDisk_F()
		self.printVcpu_F()