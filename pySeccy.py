C_DESC = "Player-character name can only be 12 characters long and must contain ASCII characters in Classic mode"
BB_DESC = "Player-character name can only be 10 characters long but can contain unicode characters in Blue-Burst mode"
NOTASCII = "[!] Name contains non-ASCII characters"
LEN_REMINDER = "[!] Player-character name can only be 12 characters long in Classic mode, input a shorter one: "
BB_LEN_REMINDER = "[!] Player-character name can only be 10 characters long in BB mode, input a shorter one: "
TYPE_IN_NAME = "Type in a character name: "
MODE_SELECT = "(C)lassic or (B)lue-Burst calculation ? "

PSOBB_CLASSES = ['HUmar', 'HUnewearl', 'HUcast', 'HUcaseal', 'RAmar', 'RAmarl', 'RAcast', 'RAcaseal', 'FOmar', 'FOmarl', 'FOnewm', 'FOnewearl']
PSOBB_CLASSESVAL = [0, 1, 2, 9, 3, 1, 4, 5, 0, 6, 7, 8]
PSO_LEGACY_CLASSVAL = 5 # Calculations for PSO games older than BB assume class is a Racaseal
PSO_SECTIONID = ['Pinkal', 'Redria', 'Oran', 'Yellowboze', 'Whitill', 'Viridia', 'Greenill', 'Skyly', 'Bluefull', 'Purplenum']

def unicode_sum ( input_str ):
        i = 0
        total = 0
        while 1:
            if i >= (len(input_str)):
               break
            total += ord(input_str[i])
            i += 1
        return total

def isascii ( input_str ):
    if len(input_str) != (len(input_str.encode())):
        return 0
    else:
        return 1

modechar = input(str(MODE_SELECT))
if ((modechar == 'c') or (modechar == "C")): # Classic calculation mode
    print(C_DESC)
    while (1):
        charname = input(str(TYPE_IN_NAME))
        if (isascii(charname)):
            if (len(charname) <= 12):
                # Get the right section ID in the table and print it
                print(PSO_SECTIONID[(unicode_sum(charname) + PSO_LEGACY_CLASSVAL) % 10])
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
        
            def PSO_SectionID ( input_str, classval ):
                return PSO_SECTIONID[(unicode_sum(charname) + PSOBB_CLASSESVAL[classval]) % 10]
            print("")
            print("HUmar       " + PSO_SectionID(charname, 0))
            print("HUnewearl   " + PSO_SectionID(charname, 1))
            print("HUcast      " + PSO_SectionID(charname, 2))
            print("HUcaseal    " + PSO_SectionID(charname, 3))
            print("")
            print("RAmar       " + PSO_SectionID(charname, 4))
            print("RAmarl      " + PSO_SectionID(charname, 5))
            print("RAcast      " + PSO_SectionID(charname, 6))
            print("RAcaseal    " + PSO_SectionID(charname, 7))
            print("")
            print("FOmar       " + PSO_SectionID(charname, 8))
            print("FOmarl      " + PSO_SectionID(charname, 9))
            print("FOnewm      " + PSO_SectionID(charname, 10))
            print("FOnewearl   " + PSO_SectionID(charname, 11))
            break
        else:
            print("\n" + BB_LEN_REMINDER + "\n")
