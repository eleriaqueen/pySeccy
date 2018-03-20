#!/usr/bin/env python

import sys

from seccyfn import *

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
	
argNum = len(sys.argv)
arg = sys.argv

if (argNum == 2):
	LOOP = True if ((arg[1] == '-l') or (arg[1] == '--loop')) else False
	HELP = True if ((arg[1] == '-h') or (arg[1] == '--help')) else False
	
	FORCE_CLASSIC = True if ((arg[1] == '-fc') or (arg[1] == '--force-classic')) else False
	FORCE_BB      = True if ((arg[1] == '-fb') or (arg[1] == '--force-bb'     )) else False
	
	if not (LOOP or FORCE_CLASSIC or FORCE_BB):
		if not HELP:
			basicMode(arg[1])
		
		else: print(USAGE)
	
	elif LOOP:
		while True:
			loopMode()
			
	else: print(USAGE)	

elif (argNum == 3):
	FORCE_CLASSIC = True if ((arg[1] == '-fc') or (arg[1] == '--force-classic')) else False
	FORCE_BB      = True if ((arg[1] == '-fb') or (arg[1] == '--force-bb'     )) else False
	
	if FORCE_CLASSIC:
		classicMode(arg[2])
		
	elif FORCE_BB:
		bbMode(arg[2])
		
	else: print(USAGE)
		
else: print(USAGE)
