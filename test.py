#This is for my testing. It is not important to the project's running

'''

              ."-,.__
                 `.     `.  ,
              .--'  .._,'"-' `.
             .    .'         `'
             `.   /          ,'
               `  '--.   ,-"'
                `"`   |  \
                   -. \, |
                    `--Y.'      ___.
                         \     L._, \
               _.,        `.   <  <\                _
             ,' '           `, `.   | \            ( `
          ../, `.            `  |    .\`.           \ \_
         ,' ,..  .           _.,'    ||\l            )  '".
        , ,'   \           ,'.-.`-._,'  |           .  _._`.
      ,' /      \ \        `' ' `--/   | \          / /   ..\
    .'  /        \ .         |\__ - _ ,'` `        / /     `.`.
    |  '          ..         `-...-"  |  `-'      / /        . `.
    | /           |L__           |    |          / /          `. `.
   , /            .   .          |    |         / /             ` `
  / /          ,. ,`._ `-_       |    |  _   ,-' /               ` \
 / .           \"`_/. `-_ \_,.  ,'    +-' `-'  _,        ..,-.    \`.
.  '         .-f    ,'   `    '.       \__.---'     _   .'   '     \ \
' /          `.'    l     .' /          \..      ,_|/   `.  ,'`     L`
|'      _.-""` `.    \ _,'  `            \ `.___`.'"`-.  , |   |    | \
||    ,'      `. `.   '       _,...._        `  |    `/ '  |   '     .|
||  ,'          `. ;.,.---' ,'       `.   `.. `-'  .-' /_ .'    ;_   ||
|| '              V      / /           `   | `   ,'   ,' '.    !  `. ||
||/            _,-------7 '              . |  `-'    l         /    `||
. |          ,' .-   ,' ||               | .-.        `.      .'     ||
 `'        ,'    `".'    |               |    `.        '. -.'       `'
          /      ,'      |               |,'    \-.._,.'/'
          .     /        .               .       \    .''
        .`.    |         `.             /         :_,'.'
          \ `...\   _     ,'-.        .'         /_.-'
           `-.__ `,  `'   .  _.>----''.  _  __  /
                .'        /"'          |  "'   '_
               /_|.-'\ ,".             '.'`__'-( \
                 / ,"'"\,'               `/  `-.|"

'''

#from pmachines import phys_machine
#from bmachines import virt_machine
#from image import images
from cloud import *

#Big testing function
def test():
	#Testing classes

	'''
	testV = virt_machine()

	testV.setSize_V("YUGE")
	testV.setRam_V(23)
	testV.setDisk_V(123)
	testV.setVcpu_V(22)

	testV.getSize_V()
	testV.getRam_V()
	testV.getDisk_V()
	testV.getVcpu_V()

	testV.printAll_V()
	'''

	#test = phys_machine()
	#test2 = phys_machine("stu")

	#print(test.getName())
	#print(test2.getName())

	'''
	test.setName("poo")
	test.setIp("1.1.1.1")
	test.setDisk(12)
	test.setMem(1)
	test.setVcpu(10)

	test.printAll()
	'''

	'''
	testI = images()
	testI.setI_name("TFM")
	testI.setI_path("......")
	print(testI.getI_name())
	print(testI.getI_path())
	testI.printAll_I()
	'''

	testC = cloud()

	testI = images("testIMG")
	testV = virt_machine("testVIRT")
	testP = phys_machine("testPHYS")

	testI2 = images("testIMG2")
	testV2 = virt_machine("testVIRT2")
	testP2 = phys_machine("testPHYS2")

	listI = [testI,testI]
	listV = [testV, testV]
	listP = [testP, testP]

	testC.setPhys(listP)
	testC.setVirt(listV)
	testC.setImg(listI)

	testC.addPhys(testP2)
	testC.addVirt(testV2)
	testC.addImg(testI2)

	a = testC.getPhysAt(2)
	b = testC.getVirtAt(2)
	c = testC.getImgAt(2)

	#print(*list1)
	#print(*list2)
	#print(*list3)

	print(testC.findPhysMem("testPHYS2"))
	print(testC.findPhysNameBool("testPHYS2"))
