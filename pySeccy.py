C_DESC = "Classic mode:"
BB_DESC = "Blue-Burst mode:"
NOTASCII = "[!] Name contains non-ASCII characters"
LEN_REMINDER = "[!] Name must be 12 characters long in Classic mode"
BB_LEN_REMINDER = "[!] Name must be 10 characters long in BB mode"
TYPE_IN_NAME = "Type in a character name: "
MODE_SELECT = "(C)lassic or (B)lue-Burst calculation ? "

PSOBB_CLASSES = ['HUmar', 'HUnewearl', 'HUcast', 'HUcaseal', 'RAmar', 'RAmarl', 'RAcast', 'RAcaseal', 'FOmar', 'FOmarl', 'FOnewm', 'FOnewearl']
PSOBB_CLASSESVAL = [0, 1, 2, 9, 3, 11, 4, 5, 10, 6, 7, 8]
PSO_LEGACY_CLASSVAL = 5 # Pre-BB
PSO_SECTIONID = ["Viridia", "Greenill", "Skyly", "Bluefull", "Purplenum", "Pinkal", "Redria", "Oran", "Yellowboze", "Whitill"]

def unicode_sum ( input_str, cval ):
	sum = 0
	flag = 0
	for i in input_str:
		
		sum += ord(i)
		cur = ord(i)
		if (cur > 256) and (cur < 65377):

			if (flag != 2):

				flag = 2
				sum = sum + 83
				
		elif (cur < 0xFF91):

			if (flag != 1):

				flag = 1
				sum = sum + 0x2D
				
	return ((sum + cval) % 10)

def isascii ( input_str ):
		if len(input_str) != (len(input_str.encode())):
			return False
		else:
			return True
			
modechar = input(str(MODE_SELECT))
if ((modechar == 'c') or (modechar == "C")): # Classic calculation mode
    print(C_DESC)
    while (1):
        charname = input(str(TYPE_IN_NAME))
        if (isascii(charname)):
            if (len(charname) <= 12):
                # Get the right section ID in the table and print it
                print(PSO_SECTIONID[unicode_sum(charname, PSO_LEGACY_CLASSVAL)])
                break
            else:
                print("\n" + LEN_REMINDER + "\n")
        else:
            print("\n" + NOTASCII + "\n")

elif ((modechar == 'b') or (modechar == "B")): # Blue Burst calculation mode
    print(BB_DESC)
    while (1):
        charname = input(str(TYPE_IN_NAME))
        if (len(charname) <= 10):
        
            print("")
            print("HUmar       " + PSO_SECTIONID[unicode_sum(charname, PSOBB_CLASSESVAL[0])])
            print("HUnewearl   " + PSO_SECTIONID[unicode_sum(charname, PSOBB_CLASSESVAL[1])])
            print("HUcast      " + PSO_SECTIONID[unicode_sum(charname, PSOBB_CLASSESVAL[2])])
            print("HUcaseal    " + PSO_SECTIONID[unicode_sum(charname, PSOBB_CLASSESVAL[3])])
            print("")
            print("RAmar       " + PSO_SECTIONID[unicode_sum(charname, PSOBB_CLASSESVAL[4])])
            print("RAmarl      " + PSO_SECTIONID[unicode_sum(charname, PSOBB_CLASSESVAL[5])])
            print("RAcast      " + PSO_SECTIONID[unicode_sum(charname, PSOBB_CLASSESVAL[6])])
            print("RAcaseal    " + PSO_SECTIONID[unicode_sum(charname, PSOBB_CLASSESVAL[7])])
            print("")
            print("FOmar       " + PSO_SECTIONID[unicode_sum(charname, PSOBB_CLASSESVAL[8])])
            print("FOmarl      " + PSO_SECTIONID[unicode_sum(charname, PSOBB_CLASSESVAL[9])])
            print("FOnewm      " + PSO_SECTIONID[unicode_sum(charname, PSOBB_CLASSESVAL[10])])
            print("FOnewearl   " + PSO_SECTIONID[unicode_sum(charname, PSOBB_CLASSESVAL[11])])
            break
        else:
            print("\n" + BB_LEN_REMINDER + "\n")
