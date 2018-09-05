from pmachine import phys_machine
from flavor import flavor
from image import images
from instance import instance
from rack import rack
import time
import datetime

#===========================================#
#Class for the Cloud
#===========================================#

class cloud:

	#Default contructor
	def __init__(self, phys_machineL = [], flavorL = [] , imagesL = [], instanceL = [], racks = []):
		self.phys_machineL = phys_machineL
		self.flavorL = flavorL
		self.imagesL = imagesL
		self.instanceL = instanceL
		self.racks = racks

	#=======================================#
	#Accessor methods

	#Get physical_machines
	def getPhys(self):
		return self.phys_machineL

	#Get flavor_machines
	def getFlav(self):
		return self.flavorL

	#Get images
	def getImg(self):
		return self.imagesL

	#Get instances
	def getInst(self):
		return self.instanceL

	#Get instances
	def getRack(self):
		return self.racks

	#-----------------------------#

	#Get physical_machine at index
	def getPhysAt(self, i):
		return self.phys_machineL[i]

	#Get flavor_machine at index
	def getFlavAt(self, i):
		return self.flavorL[i]

	#Get image at index
	def getImgAt(self, i):
		return self.imagesL[i]

	#Get instance at index
	def getInstAt(self, i):
		return self.instanceL[i]

	#Get rack at index
	def getRackAt(self, i):
		return self.racks[i]

	#-----------------------------#

	#Get number of physical_machines
	def getPhysNum(self):
		return len(self.phys_machineL)

	#Get number of flavor_machines
	def getFlavNum(self):
		return len(self.flavorL)

	#Get number of images
	def getImgNum(self):
		return len(self.imagesL)

	#Get number of images
	def getInstNum(self):
		return len(self.instanceL)

	#Get number of racks
	def getRackNum(self):
		return len(self.racks)

	#-----------------------------#
	#=======================================#
	#Return if search is True/False
	#=======================================#

	#Search physical machines names
	def findPhysNameBool(self, find):
		for x in range(self.getPhysNum()):
			if self.getPhysAt(x).getName() == find:
				return True
			else:
				continue
		print("Machine " + find +" not found")
		return False

	#Search instance names
	def findInstNameBool(self, find):
		for x in range(self.getInstNum()):
			if self.getInstAt(x).getInstName() == find:
				return True
			else:
				continue
		print("Instance " + find +" not found")
		return False

	#Search physical machines IP
	def findPhysIpBool(self, find):
		for x in range(self.getPhysNum()):
			if self.getPhysAt(x).getIp() == find:
				return True
			else:
				continue
		print("IP address " + find + " not found")
		return False

	#Search physical machines memory
	def findPhysMemBool(self, find):
		for x in range(self.getPhysNum()):
			if self.getPhysAt(x).getMem() == find:
				return True
			else:
				continue
		print("Memory " + str(find) + " not found")
		return False

	#Search physical machines disk num
	def findPhysDiskBool(self, find):
		for x in range(self.getPhysNum()):
			if self.getPhysAt(x).getDisk() == find:
				return True
			else:
				continue
		print("Disk count " + str(find) + " not found")
		return False

	#Search physical machines VCPU num
	def findPhysVcpuBool(self, find):
		for x in range(self.getPhysNum()):
			if self.getPhysAt(x).getVcpu() == find:
				return True
			else:
				continue
		print("VCPU count " + str(find) + " not found")
		return False

	#-----------------------------#


	#Search flavor size
	def findFlavSizeBool(self, find):
		for x in range(self.getFlavNum()):
			if self.getFlavAt(x).getSize_F() == find:
				return True
			else:
				continue
		print("Flavor size " + find + " not found")
		return False

	#Search flavor RAM
	def findFlavRamBool(self, find):
		for x in range(self.getFlavNum()):
			if self.getFlavAt(x).getRam_F() == find:
				return True
			else:
				continue
		print("Flavor size " + str(find) + " not found")
		return False

	#Search flavor disk num
	def findFlavDiskBool(self, find):
		for x in range(self.getFlavNum()):
			if self.getFlavAt(x).getDisk_F() == find:
				return True
			else:
				continue
		print("Flavor size " + str(find) + " not found")
		return False

	#Search flavor VCPU
	def findFlavVcpuBool(self, find):
		for x in range(self.getFlavNum()):
			if self.getFlavAt(x).getSize_F() == find:
				return True
			else:
				continue
		print("Flavor size " + str(find) + " not found")
		return False

	#---------------------------------------#
	#=======================================#
	#Return the value of the search
	#=======================================#

	#Search physical machines object
	def findPhysObj(self, find):
		for x in range(self.getPhysNum()):
			if self.getPhysAt(x).getName() == find:
				return self.getPhysAt(x)
			else:
				continue
		print("Machine " + find +" not found")

	#Search physical machines names
	def findPhysName(self, find):
		for x in range(self.getPhysNum()):
			if self.getPhysAt(x).getName() == find:
				return self.getPhysAt(x).getName()
			else:
				continue
		print("Machine name " + find +" not found")

	#Search physical machines IP
	def findPhysIp(self, find):
		for x in range(self.getPhysNum()):
			if self.getPhysAt(x).getName() == find:
				return self.getPhysAt(x).getIp()
			else:
				continue
		print("IP address " + find + " not found")

	#Search physical machines memory
	def findPhysMem(self, find):
		for x in range(self.getPhysNum()):
			if self.getPhysAt(x).getName() == find:
				return self.getPhysAt(x).getMem()
			else:
				continue
		print("Memory " + str(find) + " not found")


	#Search physical machines disk num
	def findPhysDisk(self, find):
		for x in range(self.getPhysNum()):
			if self.getPhysAt(x).getName() == find:
				return self.getPhysAt(x).getDisk()
			else:
				continue
		print("Disk count " + str(find) + " not found")
		return False

	#Search physical machines VCPU num
	def findPhysVcpu(self, find):
		for x in range(self.getPhysNum()):
			if self.getPhysAt(x).getName() == find:
				return self.getPhysAt(x).getVcpu()
			else:
				continue
		print("VCPU count " + str(find) + " not found")

	#-----------------------------#

	#Search flavor size, return flavor object
	def findFlavObj(self, find):
		for x in range(self.getFlavNum()):
			if self.getFlavAt(x).getSize_F() == find:
				return self.getFlavAt(x)
			else:
				continue
		print("Flavor size " + find + " not found")

	#Search flavor size, return flavor name
	def findFlavSize(self, find):
		for x in range(self.getFlavNum()):
			if self.getFlavAt(x).getSize_F() == find:
				return self.getFlavAt(x).getSize_F()
			else:
				continue
		print("Flavor size " + find + " not found")

	#Search flavor RAM
	def findFlavRam(self, find):
		for x in range(self.getFlavNum()):
			if self.getFlavAt(x).getSize_F() == find:
				return self.getFlavAt(x).getRam_F()
			else:
				continue
		print("Flavor size " + str(find) + " not found")

	#Search flavor disk num
	def findFlavDisk(self, find):
		for x in range(self.getFlavNum()):
			if self.getFlavAt(x).getSize_F() == find:
				return self.getFlavAt(x).getDisk_F()
			else:
				continue
		print("Flavor size " + str(find) + " not found")

	#Search flavor VCPU
	def findFlavVcpu(self, find):
		for x in range(self.getFlavNum()):
			if self.getFlavAt(x).getSize_F() == find:
				return self.getFlavAt(x).getVcpu_F()
			else:
				continue
		print("Flavor size " + str(find) + " not found")

	#-----------------------------#

	#Search for an instance by name of instance
	def findInstName(self, find):
		for x in range(self.getInstNum()):
			if self.getInstAt(x).getInstName() == find:
				return self.getInstAt(x)
			else:
				continue
		print("Instance " + find +" not found")

	#-----------------------------#

	#Search for a rack by name
	def findRack(self, find):
		for x in range(self.getRackNum()):
			if self.getRackAt(x).getName() == find:
				return self.getRackAt(x)
			else:
				continue
		print("Rack not found!")

	#=======================================#
	#Mutator Methods

	#Set physical_machines
	def setPhys(self, phys):
		self.phys_machineL = phys

	#Set flavor_machines
	def setFlav(self, Flav):
		self.flavorL = Flav

	#Set images
	def setImg(self, image):
		self.imagesL = image

	#Set instances
	def setInst(self, inst):
		self.instanceL = inst

	#Set rack
	def setInst(self, rack):
		self.racks = rack

	#-----------------------------#

	#Set physical_machine at index
	def setPhysAt(self, phys, i):
		self.phys_machineL[i] = phys

	#Set flavor_machine at index
	def setFlavAt(self, Flav, i):
		self.flavorL[i] = Flav

	#Set image at index
	def setImgAt(self, img, i):
		self.imagesL[i] = img

	#Set instances at index
	def setInst(self, inst, i):
		self.instanceL[i] = inst

	#Set racks at index
	def setRackAt(self, rack, i):
		self.racks[i] = rack

	#-----------------------------#

	#Append physical_machines
	def addPhys(self, phys):
		self.phys_machineL.append(phys)

	#Append flavor_machines
	def addFlav(self, Flav):
		self.flavorL.append(Flav)

	#Append images
	def addImg(self, image):
		self.imagesL.append(image)

	#Append instances
	def addInst(self, inst):
		self.instanceL.append(inst)

	#Append racks
	def addRack(self, rack):
		self.racks.append(rack)

	#-----------------------------#

	#Remove physical_machine at index
	def rmPhys(self, i):
		self.phys_machineL.pop(i)

	#Remove flavor_machines at index
	def rmFlav(self, i):
		self.flavorL.pop(i)

	#Remove images at index
	def rmImg(self, i):
		self.imagesL.pop(i)

	#Remove instance at index
	def rmInst(self, i):
		self.instanceL.pop(i)

	#Remove rack at index
	def rmRack(self, i):
		self.racks.pop(i)

	#Remove physical_machine by name
	def rmPhysName(self, name):
		for x in range(self.getPhysNum()):
			if self.phys_machineL[x].getName() == name:
				self.phys_machineL.pop(x)
				return
			else:
				pass
		print("Machine " + name + " not found!")

	#Remove rack by name
	def rmRackName(self, name):
		for x in range(self.getRackNum()):
			if self.racks[x].getName() == name:
				self.racks.pop(x)
				return
			else:
				continue
		print("Rack" + name + " not found!")

	#=======================================#
	#Print Methods

	#Print admin physical_machines
	def printAdminPhys_C(self):
		for x in range(self.getPhysNum()):
			self.phys_machineL[x].printAll_P()
			print()

	#Print admin flavor_machines
	def printAdminFlav_C(self):
		for x in range(self.getFlavNum()):
			self.flavorL[x].printAll_F()

	#Print admin images
	def printAdminImg_C(self):
		for x in range(self.getImgNum()):
			self.imagesL[x].printAll_I()

	#Print admin instances
	def printAdminInst_C(self):
		for x in range(self.getInstNum()):
			self.instanceL[x].printInstAll()

	#-----------------------------#

	#Print physical_machines names
	def printPhys_C(self):
		for x in range(self.getPhysNum()):
			self.phys_machineL[x].printName()
			print()

	#Print flavor_machine sizes
	def printFlav_C(self):
		for x in range(self.getFlavNum()):
			self.flavorL[x].printSize_F()
			print()

	#Print images available
	def printImg_C(self):
		for x in range(self.getImgNum()):
			self.imagesL[x].printI_name()
			print()

	#Print instances
	def printInst_C(self):
		for x in range(self.getInstNum()):
			self.instanceL[x].printInstName()

	#Print machine instances are running on
	def printInstMach_C(self):
		for x in range(self.getInstNum()):
			self.instanceL[x].printInstMach()

	#-----------------------------#

	#Print all admin
	def printAdminAll_C(self):
		self.printAdminPhys_C()
		self.printAdminFlav_C()
		self.printAdminImg_C()

	#Print all non-admin
	def printAll_C(self):
		self.printPhys_C()
		self.printFlav_C()
		self.printImg_C()

#===========================================#
#Helper Functions for the Cloud Class
#===========================================#

#Function for can host
def can_host(phys, flav, cloud):
	can_host = cloud.findPhysNameBool(phys)
	can_host = cloud.findFlavSizeBool(flav)
	if can_host == False:
		return can_host
	else:
		pass

	if cloud.findPhysMem(phys) < cloud.findFlavRam(flav):
		can_host = False
		return can_host
	elif cloud.findPhysDisk(phys) < cloud.findFlavDisk(flav):
		can_host = False
		return can_host
	elif cloud.findPhysVcpu(phys) < cloud.findFlavVcpu(flav):
		can_host = False
		return can_host
	else:
		return can_host

#Function for time stamps
def stamp():
	the_time = time.time()
	log_time = datetime.datetime.fromtimestamp(the_time).strftime('%Y-%m-%d %H:%M:%S') + ": "
	return log_time;