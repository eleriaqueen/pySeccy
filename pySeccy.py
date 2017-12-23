import sys

USAGE = "usage: hildebear name\n\
       hildebear [-h] [-f NAME] [-F NAME] [-l]\n\n\
optional arguments:\n\
  -h, --help            show this help message and exit\n\
  -fc, --force-classic NAME  compute Section ID\n\
                        for PSO V1\\V2\\PC\\GC only\n\
  -fb, --force-bb NAME  compute Section ID\n\
                        for PSO Blue Burst only\n\
  -l, --loop            enter multiple names one after the other\n\
                        type-in the word 'exit' to leave\n"

def SectionID(name):
	idList = ['Pinkal', 'Redria', 'Oran', 'Yellowboze', 'Whitill', 'Viridia', 'Greenill', 'Skyly', 'Bluefull', 'Purplenum']
	classicVal = 5
	total = 0
	
	for i in name:
		total += ord(i)
		
	return(idList[(total + classicVal) % 10] )
	
def BB_SectionID(name, BBVal):
	idList = ["Viridia", "Greenill", "Skyly", "Bluefull", "Purplenum", "Pinkal", "Redria", "Oran", "Yellowboze", "Whitill"]
	total = 0
	flag = 0
	
	for i in name:
		total += ord(i)
		cur = ord(i)
		
		if (cur > 256) and (cur < 65377):

			if (flag != 2):

				flag = 2
				total += 83
				
		elif (cur < 0xFF91):

			if (flag != 1):

				flag = 1
				total += 0x2D
				
	return(idList[(total + BBVal) % 10] )

def PrntSecID(name):
	print(SectionID(name), lega)
	
def BB_PrntSecIDList(name):
	BB_CLASSVAL = [0, 1, 2, 9, 3, 11, 4, 5, 10, 6, 7, 8]
	print("  HUmar     = " + BB_SectionID(name, BB_CLASSVAL[0]))
	print("  HUcast    = " + BB_SectionID(name, BB_CLASSVAL[1]))
	print("  HUcaseal  = " + BB_SectionID(name, BB_CLASSVAL[2]))
	print("  HUnewearl = " + BB_SectionID(name, BB_CLASSVAL[3]))
			
	print("  RAmar     = " + BB_SectionID(name, BB_CLASSVAL[4]))
	print("  RAmarl    = " + BB_SectionID(name, BB_CLASSVAL[5]))
	print("  RAcast    = " + BB_SectionID(name, BB_CLASSVAL[6]))
	print("  RAcaseal  = " + BB_SectionID(name, BB_CLASSVAL[7]))
			
	print("  FOmar     = " + BB_SectionID(name, BB_CLASSVAL[8]))
	print("  FOmarl    = " + BB_SectionID(name, BB_CLASSVAL[9]))
	print("  FOnewm    = " + BB_SectionID(name, BB_CLASSVAL[10]))
	print("  FOnewearl = " + BB_SectionID(name, BB_CLASSVAL[11]))
	return 0
	
argNum = len(sys.argv)
arg = sys.argv
	
if (argNum == 2) and not ((arg[1] != '-l') or (arg[1] != '--loop')):
	if (arg[1] != '-h') and (arg[1] != '--help'):
		if (len(arg[1]) >= 1) and (len(arg[1]) <= 12):
			# PSO 'Classic' only accepts up to 12 characters which must be ASCII
			if len(arg[1]) == len(arg[1].encode()):
				print("Classic:")
				print("  " + SectionID(arg[1]) + "")
			
			else: print("Classic: (!) Invalid character(s) detected\n")
		else: print("Classic: (!) 12-characters limit exceeded\n")
		# PSO-BB only accepts 10-character names
		if (len(arg[1]) <= 10):
			# We compute Section ID for every class in the game
			print("\nBlueBurst:")
			BB_PrntSecIDList(nameBuf)
			
		else: print("\nBlueBurst: (!) 10-characters limit exceeded\n")
		
	else: print(USAGE)
elif (argNum == 3):
	if ((arg[1] == '-fc') or (arg[1] == '--force-classic')):
		if (len(arg[2]) >= 1) and (len(arg[2]) <= 12):
			if len(arg[2]) == len(arg[2].encode()):
				print(SectionID(arg[2]))
			
			else: print("Classic: (!) Invalid character(s) detected\n")
		else: print("Classic: (!) 12-characters limit exceeded\n")
		
	elif ((arg[1] == '-fb') or (arg[1] == '--force-bb')):
		if (len(arg[2]) >= 1) and (len(arg[2]) <= 10):
			BB_PrntSecIDList(arg[2])
			
		else: print("\n'" + arg[2] + "' (!) 10-characters limit exceeded\n")
		
	else: print(USAGE)
	
elif (argNum == 2) and ((arg[1] == '-l') or (arg[1] == '--loop')):
	while True:
		nameBuf = input("Name :\n  ")
		
		if (nameBuf == 'exit') or (nameBuf == 'Exit'):
			break
			
		if (len(nameBuf) >= 1) and (len(nameBuf) <= 12):
			if len(nameBuf) == len(nameBuf.encode()):
				print("\nClassic:")
				print("  " + SectionID(nameBuf))
				
			else: print("\nClassic: (!) Invalid character(s) detected\n")
		else: print("\n(!) 12-characters limit exceeded\n")
			
		if (len(nameBuf) >= 1) and (len(nameBuf) <= 10):
			print("\nBlueBurst:")
			BB_PrntSecIDList(nameBuf)
			print("")
			
		else: print("\nBlueBurst: (!) 10-characters limit exceeded\n")	
		
else: print(USAGE)