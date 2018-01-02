import sys

USAGE = "usage: pySeccy name\n\
       pySeccy [-h] [-fc NAME] [-fb NAME] [-l]\n\n\
optional arguments:\n\
  -h, --help            show this help message and exit\n\
  -fc, --force-classic NAME  compute Section ID\n\
                        for PSO V1\\V2\\PC\\GC only\n\
  -fb, --force-bb NAME  compute Section ID\n\
                        for PSO Blue Burst only\n\
  -l, --loop            enter multiple names one after the other\n\
                        type-in the word 'exit' to leave\n"

def isTenCharLong(string):
	if (len(string) >= 1) and (len(string) <= 10):
		return True
	else:
		return False
		
def isTwelveCharLong(string):
	if (len(string) >= 1) and (len(string) <= 12):
		return True
	else:
		return False		
						
def isAscii(string):
	if len(string) != len(string.encode()):
		return False
	else:
		return True
						
def SectionID(name):
	idList = ["Viridia", "Greenill", "Skyly", "Bluefull", "Purplenum", "Pinkal", "Redria", "Oran", "Yellowboze", "Whitill"]
	classicVal = 5
	total = 0
	
	total += SpecialCases(name)
				
	return(idList[(total + classicVal) % 10])
	
def BB_SectionID(name, BBVal):
	idList = ["Viridia", "Greenill", "Skyly", "Bluefull", "Purplenum", "Pinkal", "Redria", "Oran", "Yellowboze", "Whitill"]
	total = 0
	flag = 0
	
	total += SpecialCases(name)
				
	return(idList[(total + BBVal) % 10])

def SpecialCases(string):
	temp = 0
	flag = 0
	for i in string:
		temp += ord(i)
		cur = ord(i)
		
		if (cur > 256) and (cur < 65377):

			if (flag != 2):

				flag = 2
				temp += 83
				
		elif (cur < 0xFF91):

			if (flag != 1):

				flag = 1
				temp += 0x2D
	return temp
	
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

def basicMode(arg):
	argLen = len(arg)
	
	# PSO 'Classic' only accepts up to 12 characters which must be ASCII
	if isTwelveCharLong(arg) and \
	isAscii(arg):
		print("Classic:")
		print("  " + SectionID(arg) + "")
		
	elif not isAscii(arg):
		print("Classic: (!) Invalid character(s) detected\n")
		
	else: print("Classic: (!) 12-characters limit exceeded\n")
	
	# PSO-BB only accepts 10-character names
	if isTenCharLong(arg):
		# We compute Section ID for every class in the game
		print("\nBlueBurst:")
		BB_PrntSecIDList(arg)
		
	else: print("\nBlueBurst: (!) 10-characters limit exceeded\n")
	
def classicMode(arg):
	argLen = len(arg)
	
	if isTwelveCharLong(arg) and \
	isAscii(arg):
		print(SectionID(arg))
			
	elif not isAscii(arg): 
		print("Classic: (!) Invalid character(s) detected\n")
			
	else: print("Classic: (!) 12-characters limit exceeded\n")
	
def bbMode(arg):
	argLen = len(arg)
	if isTenCharLong(arg):
		BB_PrntSecIDList(arg)
			
	else: print("\n'" + arg + "' (!) 10-characters limit exceeded\n")
	
def loopMode():
	buf = input("Name :\n  ")
	bufLen = len(buf)
		
	if (buf == 'exit') or \
	(buf == 'Exit'):
		sys.exit()
		
	if isTwelveCharLong(buf) and \
	isAscii(buf):
		print("\nClassic:")
		print("  " + SectionID(buf))
			
	elif not isAscii(buf):
		print("\nClassic: (!) Invalid character(s) detected\n")
		
	else: print("\n(!) 12-characters limit exceeded\n")
		
	if isTenCharLong(buf):
		print("\nBlueBurst:")
		BB_PrntSecIDList(buf)
		print("")
		
	else: print("\nBlueBurst: (!) 10-characters limit exceeded\n")
	
argNum = len(sys.argv)
arg = sys.argv
	
LOOP			= True if ((arg[1] == '-l')		or	(arg[1] == '--loop'))			else False
FORCE_CLASSIC	= True if ((arg[1] == '-fc')	or	(arg[1] == '--force-classic'))	else False
FORCE_BB		= True if ((arg[1] == '-fb')	or	(arg[1] == '--force-bb')		else False
HELP			= True if ((arg[1] != '-h')		and	(arg[1] != '--help'))			else False
	
if (argNum == 2) and not (LOOP or FORCE_CLASSIC or FORCE_BB):
	if HELP:
		basicMode(arg[1])
		
	else: print(USAGE)
	
elif (argNum == 3):
	if FORCE_CLASSIC:
		classicMode(arg[2])
		
	elif FORCE_BB:
		bbMode(arg[2])
		
	else: print(USAGE)
	
elif (argNum == 2) and LOOP:
	while True:
		loopMode()
		
else: print(USAGE)