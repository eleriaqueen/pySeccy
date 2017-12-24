import sys

USAGE = "usage: pySeccy name\n\
       pySeccy [-h] [-f NAME] [-F NAME] [-l]\n\n\
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

def basicMode(arg1):
	# PSO 'Classic' only accepts up to 12 characters which must be ASCII
	if (len(arg1) >= 1) and (len(arg1) <= 12) and (len(arg1) == len(arg1.encode())):
		print("Classic:")
		print("  " + SectionID(arg1) + "")
		
	elif (len(arg1) != len(arg1.encode())):
		print("Classic: (!) Invalid character(s) detected\n")
		
	else: print("Classic: (!) 12-characters limit exceeded\n")
	
	# PSO-BB only accepts 10-character names
	if (len(arg1) <= 10):
		# We compute Section ID for every class in the game
		print("\nBlueBurst:")
		BB_PrntSecIDList(arg1)
		
	else: print("\nBlueBurst: (!) 10-characters limit exceeded\n")
	
def classicMode(arg2):
	if (len(arg2) >= 1) and (len(arg2) <= 12) and (len(arg2) == len(arg2.encode())):
		print(SectionID(arg2))
			
	elif len(arg2) != len(arg2.encode()): 
		print("Classic: (!) Invalid character(s) detected\n")
			
	else: print("Classic: (!) 12-characters limit exceeded\n")
	
def bbMode(arg2):
	if (len(arg2) >= 1) and (len(arg2) <= 10):
		BB_PrntSecIDList(arg2)
			
	else: print("\n'" + arg2 + "' (!) 10-characters limit exceeded\n")
	
def loopMode():
	buf = input("Name :\n  ")
		
	if (buf == 'exit') or (buf == 'Exit'):
		return
		
	if (len(buf) >= 1) and (len(buf) <= 12) and (len(buf) == len(buf.encode())):
		print("\nClassic:")
		print("  " + SectionID(buf))
			
	elif (len(buf) != len(buf.encode())):
		print("\nClassic: (!) Invalid character(s) detected\n")
		
	else: print("\n(!) 12-characters limit exceeded\n")
		
	if (len(buf) >= 1) and (len(buf) <= 10):
		print("\nBlueBurst:")
		BB_PrntSecIDList(buf)
		print("")
		
	else: print("\nBlueBurst: (!) 10-characters limit exceeded\n")
	
argNum = len(sys.argv)
arg = sys.argv
	
if (argNum == 2) and not ((arg[1] == '-l') or (arg[1] == '--loop')):
	if (arg[1] != '-h') and (arg[1] != '--help'):
		basicMode(arg[1])
		
	else: print(USAGE)
	
elif (argNum == 3):
	if ((arg[1] == '-fc') or (arg[1] == '--force-classic')):
		classicMode(arg[2])
		
	elif ((arg[1] == '-fb') or (arg[1] == '--force-bb')):
		bbMode(arg[2])
		
	else: print(USAGE)
	
elif (argNum == 2) and ((arg[1] == '-l') or (arg[1] == '--loop')):
	while True:
		loopMode()
		
else: print(USAGE)