import sys
import os
from pathlib import Path
from cloud import *

#For testing purposes. Comment out if I forget
from test import test

#Variable to track whether to run AggieStack
running = True

#Create a cloud
the_cloud = cloud()

#Create/open a log file. Remember to close at the end
log = open("aggiestack-log.txt", "a+")

log.write(stamp() + "Started AggieStack\n")

#Main body
while running:
	try:
		#Take user commands
		command = input("Please enter your commands.\naggiestack>")
		command = command.lower()
		command_split = command.split(" ")

		#In case you don't want to chane the scripts
		if command_split[0] == "aggiestack":
			command_split.pop(0)
		else:
			pass

		#Pad the command to avoid index out of bounds during error checking
		if len(command_split) < 15:
			while len(command_split) < 15:
				command_split.append("")
		else:
			pass

		#Accept exit command
		if command_split[0] == "exit":
			log.write(stamp() + "Exited with \"exit\" command\n")
			break

		#Test command. Debugging only
		if command_split[0] == "test":
			#test()
			for x in range(the_cloud.getRackNum()):
				print(the_cloud.getRackAt(x).getMachAt(x))
				print(str(the_cloud.getRackAt(x).getStorage()))

		#=================================================#
		#Config Commands
		#=================================================#

		elif command_split[0] == "config":

			#Conifg Hardware command
			if command_split[1] == "--hardware":
				my_file = Path(command_split[2])

				#Handle hardware file not existing
				if my_file.is_file() == False:
					log.write(stamp() + "FAILURE - Hardware file entered does not exist\n")
					print("Error - Hardware file does not exist!")
					continue
				elif command_split[2] != "hdwr-config.txt":
					print("Wrong file entered for hardware")
					log.write(stamp() + "FAILURE - File " + command_split[2] 
						+ " is the wrong file\n")
					continue
				else:
					#Get file contents
					file = open(command_split[2], "r")
					hardware = file.readlines()[1:]

					#Read through file
					for line in hardware:
						line_split = line.split(" ")
						if len(line_split) < 2:
							continue
						elif len(line_split) == 2:
							new_rack = rack(line_split[0], int(line_split[1]))
							the_cloud.addRack(new_rack)
						else:
							t_name = line_split[0]
							t_rack = line_split[1]
							t_ip = line_split[2]
							t_mem = int(line_split[3])
							t_dsk = int(line_split[4])
							t_vcpu = int(line_split[5])
							temp_machine = phys_machine(t_name, t_ip, t_mem, t_dsk, t_vcpu, t_rack)
							the_cloud.addPhys(temp_machine)
					log.write(stamp() + "SUCCESS - Config Hardware command\n")

					#Close file. Don't forget
					file.close()

			#Config Images command
			elif command_split[1] == "--images":
				my_file = Path(command_split[2])

				#Handle images file not existing
				if my_file.is_file() == False:
					log.write(stamp() + "FAILURE - Image file entered does not exist\n")
					print("Error - Image file does not exist!")
					continue
				elif command_split[2] != "image-config.txt":
					print("Wrong file entered for images")
					log.write(stamp() + "FAILURE - File " + command_split[2] 
						+ " is the wrong file\n")
					continue
				else:
					file = open(command_split[2], "r")
					hardware = file.readlines()[1:]

					#Read through file
					for line in hardware:
						line_split = line.split(" ")
						t_name = line_split[0]
						t_path = line_split[1]
						temp_image = images(t_name, t_path)
						the_cloud.addImg(temp_image)

					log.write(stamp() + "SUCCESS - Config Images command\n")

					#Close file. Don't forget
					file.close()

			#Config Flavors command
			elif command_split[1] == "--flavors":
				my_file = Path(command_split[2])

				#Handle flavors file not existing
				if my_file.is_file() == False:
					log.write(stamp() + "FAILURE - Flavors file entered does not exist\n")
					print("Error - Flavors file does not exist!")
					continue
				elif command_split[2] != "flavor-config.txt":
					print("Wrong file entered for flavors")
					log.write(stamp() + "FAILURE - File " + command_split[2] 
						+ " is the wrong file\n")
					continue
				else:
					file = open(command_split[2], "r")
					hardware = file.readlines()[1:]

					#Read through file
					for line in hardware:
						line_split = line.split(" ")
						t_size = line_split[0]
						t_ram = int(line_split[1])
						t_dsk = int(line_split[2])
						t_vcpu = int(line_split[3])
						temp_flav = flavor(t_size, t_ram, t_dsk, t_vcpu)
						the_cloud.addFlav(temp_flav)

					log.write(stamp() + "SUCCESS - Config Flavors command\n")

					#Close file. Don't forget
					file.close()

			#Invalid inputs
			else:
				log.write(stamp() + "FAILURE - Invalid \"config\" command entered\n")
				print("FAILURE - Invalid command")

		#=================================================#
		#Show Commands
		#=================================================#

		elif command_split[0] == "show":

			#Show Hardware command
			if command_split[1] == "hardware":
				the_cloud.printPhys_C()
				log.write(stamp() + "SUCCESS - Show Hardware command\n")

			#Show Images command
			elif command_split[1] == "images":
				the_cloud.printImg_C()
				log.write(stamp() + "SUCCESS - Show Images command\n")

			#Show Flavors command
			elif command_split[1] == "flavors":
				the_cloud.printFlav_C()
				log.write(stamp() + "SUCCESS - Show Flavors command\n")

			#Show All command
			elif command_split[1] == "all":
				the_cloud.printAll_C()
				log.write(stamp() + "SUCCESS - Show All command\n")

			#Invalid inputs
			else:
				log.write(stamp() + "FAILURE - Invalid \"show\" command entered\n")
				print("Invalid command")

		#=================================================#
		#Admin Commands
		#=================================================#

		elif command_split[0] == "admin":

			#Show command
			if command_split[1] == "show":

				#=====Admin Show sub-commands=======#

				#Show Hardware command
				if command_split[2] == "hardware":
					the_cloud.printAdminPhys_C()
					log.write(stamp() + "SUCCESS - admin show hardware command\n")

				#Show Instances command
				elif command_split[2] == "instances":
					the_cloud.printInstMach_C()
					log.write(stamp() + "SUCCESS - admin show instances command\n")

				#Catch invalid commands
				else:
					log.write(stamp() + "FAILURE - Invalid \"admin\" command\n")
					print("Invalid command")

				#=====Admin Show sub-commands=======#

			#Evacuate command
			elif command_split[1] == "evacuate":
				rack_name = command_split[2]

				#Find if input exists
				valid = False
				for x in range(the_cloud.getRackNum()):
					if rack_name == the_cloud.getRackAt(x).getName():
						valid = True
						break
				#Validate input
				if valid == False:
					print("Rack entered does not exist")
					log.write(stamp() + "FAILURE - Rack \"" + rack_name + "\" does not exist\n")
					continue
				else:
					pass

				count = 0
				temp = the_cloud.findRack(rack_name)
				the_cloud.rmRackName(rack_name)
				mig_rack = the_cloud.getRackAt(0).getName()
				for x in range(the_cloud.getPhysNum()):
					if the_cloud.getPhysAt(x).getRack() == rack_name:
						the_cloud.getPhysAt(x).setRack(mig_rack)
						count += 1
						log.write(stamp() + "SUCCESS - Machine " + the_cloud.getPhysAt(x).getName() +
							" evacuated to rack " + mig_rack + " from " + rack_name + "\n")
					else:
						pass
				log.write(stamp() + "SUCCESS - Number of machines evacuated: " + str(count) + "\n")

			#Remove command
			elif command_split[1] == "remove":

				#Find if input exists
				valid = False
				for x in range(the_cloud.getPhysNum()):
					if command_split[2] == the_cloud.getPhysAt(x).getName():
						valid = True
						break
				#Validate input
				if valid == False:
					print("Machine entered does not exist")
					log.write(stamp() + "FAILURE - Machine \"" + command_split[2] 
						+ "\" does not exist\n")
					continue
				else:
					pass

				temp_machine = the_cloud.findPhysObj(command_split[2])
				if temp_machine.getInstNum() == 0:
					the_cloud.rmPhysName(temp_machine.getName())
					log.write(stamp() + "SUCCESS - Machine " + temp_machine.getName() + " removed\n")
				else:
					print("Machine hosting instances. Cannot remove.")
					log.write(stamp() + "FAILURE - Cannot remove machine\n")

			#Add command
			elif command_split[1] == "add":
				temp_mem = int(command_split[3])
				temp_disk = int(command_split[5])
				temp_vcpu = int(command_split[7])
				temp_ip = command_split[9]
				temp_rack = command_split[11]
				temp_name = command_split[12]
				new_machine = phys_machine(temp_name,temp_ip, temp_mem, 
					temp_disk, temp_vcpu, temp_rack)
				the_cloud.addPhys(new_machine)
				log.write(stamp() + "SUCCESS - Machine \"" + temp_name + "\" added to cloud\n")

			#Can_Host command
			elif command_split[1] == "can_host":
				mac_name = command_split[2]
				fla_name = command_split[3]
				mac_exist = the_cloud.findPhysNameBool(mac_name)
				flav_exist = the_cloud.findFlavSizeBool(fla_name)

				#Machine entered exists, but flavor doesn't
				if mac_exist == True and flav_exist != True:
					print("The flavor \"" + fla_name + "\" does not exist")
					log.write(stamp() + "FAILURE - The flavor \"" + fla_name + "\" does not exist\n")
					continue
				#Flavor entered exists, but machine doesn't
				elif mac_exist != True and flav_exist == True:
					print("The machine \"" + mac_name + "\" does not exist")
					log.write(stamp() + "FAILURE - The flavor \"" + mac_name + "\" does not exist\n")
					continue
				#Nether exist
				elif mac_exist != True and flav_exist != True:
					print("The machine \"" + mac_name + "\" and flavor \"" + 
						fla_name + "\" do not exist")
					log.write(stamp() + "FAILURE - The machine \"" + mac_name + "\" and flavor \"" + 
						fla_name + "\" do not exist")
					continue
				else:
					pass
				host = can_host(mac_name, fla_name, the_cloud)
				if host == True:
					log.write(stamp() + "SUCCESS - can_host command, it CAN host\n")
					print("Yes")
				else:
					print("No")
					log.write(stamp() + "SUCCESS - can_host command, it CANNOT host\n")
				
			#Invalid inputs
			else:
				log.write(stamp() + "FAILURE - Invalid \"show\" command entered\n")
				print("Invalid command")

		#=================================================#
		#Server Commands
		#=================================================#

		elif command_split[0] == "server":

			#=====Server sub-commands=======#
			#Create sub-command
			if command_split[1] == "create":
				can_host = False
				#Name of the image
				t_img = command_split[3]
				#Name of the flavor
				t_flav = command_split[5]
				#Name of the instance
				t_inst = command_split[6]
				#Get the flavor the user typed in first. This is a flavor object
				the_flavor = the_cloud.findFlavObj(t_flav)
				the_machine = phys_machine()
				#Now that the flavor is obtained, search through the hardware for free spot
				for x in range(the_cloud.getPhysNum()):
					try_mach = the_cloud.getPhysAt(x)
					if (try_mach.getMem() >= the_flavor.getRam_F() and
					try_mach.getDisk() >= the_flavor.getDisk_F() and
					try_mach.getVcpu() >= the_flavor.getVcpu_F()):
						can_host = True
						the_machine = try_mach
						#Remove the machine. It will be updated and added back in
						the_cloud.rmPhys(x)
						break
					else:
						pass

				if can_host == False:
					print("No machines available to create instance")
					log.write(stamp() + "SUCCESS - No machines availbe for instance\n")
					continue
				else:
					#This is where the hardware available is updated
					temp_mem = the_flavor.getRam_F()
					temp_disk = the_flavor.getDisk_F()
					temp_vcpu = the_flavor.getVcpu_F()
					the_machine.setMem(the_machine.getMem() - temp_mem)
					the_machine.setDisk(the_machine.getDisk() - temp_disk)
					the_machine.setVcpu(the_machine.getVcpu() - temp_vcpu)
					temp_instance = instance(t_inst, t_img, t_flav, the_machine.getName(),
						temp_mem, temp_disk, temp_vcpu)

					#Add instance to the machine's list of instances
					the_machine.addInst(temp_instance)
					the_cloud.addPhys(the_machine)
					the_cloud.addInst(temp_instance)
					log.write(stamp() + "SUCCESS - Instance " + t_inst + " was created on the machine " 
						+ the_machine.getName() + "\n")
					print("instance " + t_inst + " was successfully created on machine " + 
						the_machine.getName())

			#Delete sub-command
			elif command_split[1] == "delete":
				del_inst = command_split[2]
				exist = False
				for x in range(the_cloud.getInstNum()):
					if the_cloud.getInstAt(x).getInstName() == del_inst:

						#First get the instance to delete
						temp_instance = the_cloud.getInstAt(x)
						temp_mem = temp_instance.getInstMem()
						temp_disk = temp_instance.getInstDisk()
						temp_vcpu = temp_instance.getInstVcpu()

						#Second get the machine the instance is on
						temp_machine = the_cloud.findPhysObj(temp_instance.getInstMach())

						#Third give the machine back its resources
						temp_machine.setMem(temp_machine.getMem() + temp_mem)
						temp_machine.setDisk(temp_machine.getDisk() + temp_disk)
						temp_machine.setVcpu(temp_machine.getVcpu() + temp_vcpu)
						temp_machine.rmInst(del_inst)
						the_cloud.rmPhysName(temp_machine.getName())
						the_cloud.addPhys(temp_machine)

						#Remove the instance from the list
						the_cloud.rmInst(x)
						exist = True
						break
					else:
						pass
				
				if exist == False:
					print("The instance entered does not exist")
					log.write(stamp() + "FAILURE - Instance \"" + del_inst + "\" does not exist")
				else:
					pass

				log.write(stamp() + "SUCCESS - Instance" + del_inst + " was deleted from machine " +
					temp_machine.getName() + "\n")

			#List sub-command
			elif command_split[1] == "list":
				the_cloud.printAdminInst_C()
				log.write(stamp() + "SUCCESS - server list command\n")

			#Invalid command
			else:
				log.write(stamp() + "FAILURE - Invalid \"server\" command entered\n")
				print("Invalid command")

			#=====Server sub-commands=======#

		#Catch invalid inputs
		else:
			log.write(stamp() + "FAILURE - Command \"" + command_split[0] + "\" is not valid\n")
			print("Invalid command")

	#Let me exit with Ctrl + C for convenience
	except KeyboardInterrupt:
		log.write(stamp() + "Exited with Ctrl + C\n")
		log.close()
		running = False

#Close the log file at the end
log.close()