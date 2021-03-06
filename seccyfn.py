BB_CLASSVAL = [0, 1, 2, 9, 3, 11, 4, 5, 10, 6, 7, 8]

idList = ["Viridia", "Greenill", "Skyly", "Bluefull", "Purplenum", "Pinkal", "Redria", "Oran", "Yellowboze", "Whitill"]
		
def lenEquals(string, length):
	if (length >= 1) and (len(string) >= 1) and (len(string) <= length):
		return True
	else:
		return False	
			
def isAscii(string):
	if len(string) != len(string.encode()):
		return False
	else:
		return True
						
def SectionID(name):
	classicVal = 5
	total = 0
	
	total += SpecialCases(name)
				
	return(idList[(total + classicVal) % 10])
	
def BB_SectionID(name, BBVal):
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
	print("  HUmar     = " + BB_SectionID(name, BB_CLASSVAL[0]))
	print("  HUnewearl = " + BB_SectionID(name, BB_CLASSVAL[1]))
	print("  HUcast    = " + BB_SectionID(name, BB_CLASSVAL[2]))
	print("  HUcaseal  = " + BB_SectionID(name, BB_CLASSVAL[3]))
			
	print("  RAmar     = " + BB_SectionID(name, BB_CLASSVAL[4]))
	print("  RAmarl    = " + BB_SectionID(name, BB_CLASSVAL[5]))
	print("  RAcast    = " + BB_SectionID(name, BB_CLASSVAL[6]))
	print("  RAcaseal  = " + BB_SectionID(name, BB_CLASSVAL[7]))
			
	print("  FOmar     = " + BB_SectionID(name, BB_CLASSVAL[8]))
	print("  FOmarl    = " + BB_SectionID(name, BB_CLASSVAL[9]))
	print("  FOnewm    = " + BB_SectionID(name, BB_CLASSVAL[10]))
	print("  FOnewearl = " + BB_SectionID(name, BB_CLASSVAL[11]))

def basicMode(arg):
	argLen = len(arg)
	
	# PSO 'Classic' only accepts up to 12 characters which must be ASCII
	if lenEquals(arg, 12) and \
	isAscii(arg):
		print("Classic:")
		print("  " + SectionID(arg) + "")
		
	elif not isAscii(arg):
		print("Classic: (!) Invalid character(s) detected\n")
		
	else: print("Classic: (!) 12-characters limit exceeded\n")
	
	# PSO-BB only accepts 10-character names
	if lenEquals(arg, 10):
		# We compute Section ID for every class in the game
		print("\nBlueBurst:")
		BB_PrntSecIDList(arg)
		
	else: print("\nBlueBurst: (!) 10-characters limit exceeded\n")
	
def classicMode(arg):
	argLen = len(arg)
	
	if lenEquals(arg, 12) and \
	isAscii(arg):
		print(SectionID(arg))
			
	elif not isAscii(arg): 
		print("Classic: (!) Invalid character(s) detected\n")
			
	else: print("Classic: (!) 12-characters limit exceeded\n")
	
def bbMode(arg):
	argLen = len(arg)
	if lenEquals(arg, 10):
		BB_PrntSecIDList(arg)
			
	else: print("BlueBurst: (!) 10-characters limit exceeded\n")
	
def loopMode():
	buf = input("Name :\n  ")
	bufLen = len(buf)
		
	if (buf == 'quit') or \
	(buf == 'Quit'):
		print("Leaving loop mode, see you on Ragol!")
		exit()
		
	if lenEquals(buf, 12) and \
	isAscii(buf):
		print("\nClassic:")
		print("  " + SectionID(buf))
			
	elif not isAscii(buf):
		print("\nClassic: (!) Invalid character(s) detected\n")
		
	else: print("\n(!) 12-characters limit exceeded\n")
		
	if lenEquals(buf, 10):
		print("\nBlueBurst:")
		BB_PrntSecIDList(buf)
		print("")
		
	else: print("\nBlueBurst: (!) 10-characters limit exceeded\n")
