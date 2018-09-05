#===========================================#
#Class for physical machines
#===========================================#

from instance import instance

class phys_machine:

	#Default contructor
	def __init__(self, name = "", ip = "0.0.0.0", mem = 0, num_disks = 0, 
		num_vcpus = 0, rack = "", instances = []):
		self.name = name
		self.ip = ip
		self.mem = mem
		self.num_disks = num_disks
		self.num_vcpus = num_vcpus
		self.instances = instances
		self.rack = rack

	#=======================================#
	#Accessor methods

	#Get name
	def getName(self):
		return self.name
	
	#Get IP address
	def getIp(self):
		return self.ip

	#Get memory
	def getMem(self):
		return self.mem

	#Get num-disks
	def getDisk(self):
		return self.num_disks

	#Get num-vcpus
	def getVcpu(self):
		return self.num_vcpus

	#Get rack
	def getRack(self):
		return self.rack

	#Get instances
	def getInst(self):
		return self.instances

	#Get instance size
	def getInstNum(self):
		return len(self.instances)

	#Get instances at index
	def getInstAt(self, i):
		return self.instances[i]

	#Find instance by name
	def findInst(self, name):
		for x in range(self.getInstNum):
			if instances[x].getInstName() == name:
				return instances[x]
			else:
				pass

	#=======================================#
	#Mutator Methods

	#Set name
	def setName(self, name):
		self.name = name
	
	#Set IP address
	def setIp(self, ip):
		self.ip = ip

	#Set memory
	def setMem(self, mem):
		self.mem = mem

	#Set num-disks
	def setDisk(self, disk):
		self.num_disks = disk

	#Set num-vcpus
	def setVcpu(self, vcpu):
		self.num_vcpus = vcpu

	#Set rack
	def setRack(self, rack):
		self.rack = rack

	#Set instances
	def setInst(self, inst):
		self.instances = inst

	#Set instances at index
	def setInstAt(self, inst, i):
		self.instances[i] = inst

	#Add an instance
	def addInst(self, inst):
		self.instances.append(inst)

	#Remove an instance by name
	def rmInst(self, inst):
		for x in range(self.getInstNum()):
			if self.instances[x].getInstName() == inst:
				self.instances.pop(x)
				return
			else:
				pass

	#=======================================#
	#Print Methods

	#Print name
	def printName(self):
		print("Machine Name: " + self.name)
	
	#Print IP address
	def printIp(self):
		print("Machine IP Address: " + self.ip)

	#Print memory
	def printMem(self):
		print(str("Machine Memory available: " + str(self.mem)))

	#Print num-disks
	def printDisk(self):
		print(str("Machine Disk Num available: " + str(self.num_disks)))

	#Print num-vcpus
	def printVcpu(self):
		print(str("Machine VCPU Num available: " + str(self.num_vcpus)))

	#Print rack
	def printRack(self):
		print("Machine on rack: " + self.rack)

	#Print All
	def printAll_P(self):
		self.printName()
		self.printIp()
		self.printMem()
		self.printDisk()
		self.printVcpu()
		self.printRack()


