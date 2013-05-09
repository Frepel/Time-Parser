#!/usr/bin/python
import re
import sys
global time 
global inputdata
#time = 'default'
inputdata = ''

def theScript():
	askTime()


def askTime():
	global time
	#time = raw_input('What time is it?\n (please answer in following format 10, 10.00)')
	#time = raw_input('Please insert your time in the following format: hh:mm, hh.mm, hh,mm or hh'\n What time do you have?\n ')
	time = raw_input('Please insert your time in the following format: hh:mm, hh.mm, hh,mm or hh.\nWhat time do you have? \n')

	if validateInput(time):
		printTime(inputdata)
		sys.exit()
	else:
		inputFail()


#Validates the input
def validateInput(time):
	inputlength = len(time)
	#If the input is in hh format. The validity of the hours will be checked and 00 will be appended to the time -> new format hh:mm
	#If the input is in incorrect format the user is asked to insert it again or quit
	if inputlength == 2:
		global inputdata
		inputdata = re.split(',|\.|:', time)
		
		#Testing the that the hours are valid
		if testHours(inputdata[0]):
			inputdata.append('00')
			return 1
	#If the inserted format it hh:mm or simiilar the input is checked  for correct separators and the hours and minutes are validated.
	#If the input is in incorrect format the user is asked to insert it again or quit
	elif inputlength == 5:
		separator = time [2:3]
		
		#validates the separator
		if separator not in [',','.',':']:
			inputFail()
		
		inputdata = re.split(',|\.|:', time)

		#Validates hours	
		if testHours(inputdata[0]):

			if testMinutes(inputdata[1]):
				return 1
	#if the user inserts Q or q to quit, the program exits
	elif time == 'Q' or time == 'q':
		sys.exit()



#Test that the hours are valid
def testHours(hours):
	hours = int(hours)
	if 0 <= hours < 24:
		return 1

#Test that the minutes are valid
def testMinutes(minutes):
	minutes = int(minutes)
	if 0 < minutes < 60:
		return 1

#If the input is invalid, the user is asked to insert it again or quit
def inputFail ():
	print 'The date format is invalid! Please try again or quit by typing Q and hit enter:'
	askTime()	

#Prints the time in formta hh:mm
def printTime(inputdata):
	sys.stdout.write("The time is %s:%s\n" % (inputdata[0], inputdata[1]))
	
#Main program
theScript() 	

