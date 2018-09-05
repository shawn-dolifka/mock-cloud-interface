#===========================================#
#Class for instances
#===========================================#

class instance:

	#Default constructor
	def __init__(self, name = "", image = "", flavor = "", machine_on = "", 
		memory = 0, disk = 0, vcpu = 0, migrate = False):
		self.name = name
		self.image = image
		self. flavor = flavor
		self.machine_on = machine_on
		self.memory = memory
		self.disk = disk
		self.vcpu = vcpu
		self.migrate = migrate

	#=======================================#
	#Accessor methods

	#Get instance name
	def getInstName(self):
		return self.name

	#Get instance image
	def getInstImg(self):
		return self.image

	#Get instance flavor
	def getInstFlav(self):
		return self.flavor

	#Get instance machine on
	def getInstMach(self):
		return self.machine_on

	#Get instance memory
	def getInstMem(self):
		return self.memory

	#Get instance disks
	def getInstDisk(self):
		return self.disk

	#Get instance vcpu
	def getInstVcpu(self):
		return self.vcpu

	#Get instance migration
	def getInstMig(self):
		return self.migrate

	#=======================================#
	#Mutator Methods

	#Set instance name
	def setInstName(self, name):
		self.name = name

	#Set instance image
	def setInstImg(self, img):
		self.image = img

	#Set instance flavor
	def setInstFlav(self, flav):
		self.flavor = flav

	#Set instance machine on
	def setInstMach(self, mach):
		self.machine_on = mach

	#Set instance memory
	def setInstMem(self, memory):
		self.memory = memory

	#Set instance disks
	def setInstDisk(self, dsk):
		self.disk = dsk

	#Set instance vcpu
	def setInstMem(self, vcpu):
		self.vcpu = vcpu

	#Set instance migration
	def setInstMig(self, mig):
		self.migrate = mig

	#=======================================#
	#Print Methods

	#Print instance name
	def printInstName(self):
		print("Instance name: " + self.name)

	#Print instance name
	def printInstImg(self):
		print("Instance "+ self.name + " image: " + self.image)

	#Print instance flavor
	def printInstFlav(self):
		print("Instance " + self.name + " flavor: " + self.flavor)

	#Print instance machine on
	def printInstMach(self):
		print("Instance " + self.name + " on machine: " + self.machine_on)

	#Print instance name
	def printInstAll(self):
		self.printInstName()
		self.printInstImg()
		self.printInstFlav()
		#self.printInstMach()