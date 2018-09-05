from pmachine import phys_machine

#===========================================#
#Class for racks
#===========================================#

class rack:

	#Default contructor
	def __init__(self, name = "", storage = 0, machine = []):
		self.name = name
		self.storage = storage
		self.machine = machine
		self.mech = phys_machine("Test mech")

	#=======================================#
	#Accessor methods

	#Set test mech
	def setMech(self, c):
		self.mech = c

	#Get mech
	def getMech(self):
		return self.mech

	#Get Name
	def getName(self):
		return self.name

	#Get storage
	def getStorage(self):
		return self.storage

	#Get machine
	def getMach(self):
		return self.machine

	#Get machine at index
	def getMachAt(self, i):
		self.machine[i]

	#Get machines length
	def getMachNum(self):
		return len(self.machine)

	#=======================================#
	#Mutator Methods

	#Set Name
	def setName(self, name):
		self.name = name

	#Set storage
	def setStorage(self, storage):
		self.storage = storage

	#Set machine
	def setMach(self, mach):
		self.machine = mach

	#Set machine at index
	def setMachAt(self, mach, i):
		self.machine[i] = mach

	#Add machine
	def addMach(self, mach):
		self.machine.append(mach)
		#print("Added " + mach.getName())

	#Remove machine by name
	def rmMach(self, find):
		for x in range(self.machine.getMachNum()):
			if self.machine[x].getName() == find:
				self.machine.pop(x)
				return
			else:
				continue


		