from sys import exit

def mad_scientist():
	print "You pick up a blade."
	print "A deep urge picks up within you to kill this woman."
	print "Do you tell the woman your a Nazi or kill her?"

	choice  = raw_input ("> ")
	if choice == "Nazi":
		print

def happy_ending():
	print "You survive until 1982 after a falling off a boat in the Atlantic."
	exit(0)

def SIS():
	print "Outside this cut you find some agents of SIS."
	print "They offer immunity in Britain if you join their nuclear programme."
	happy_ending()

def perimeter():
	print "You find a precut section in the fence curious you head through it."
	SIS()

def gate_house():
	print "You enter the gate house of this prison to find it empty."
	print "The sound of clapping is faintly heard."
	print "Do you leave this prison or explore the noises?"

	choice = raw_input ("> ")
	if choice == "Leave":
		perimeter()
	elif choice == "Explore":
		guard()
	else:
		dead("You are found a patrol and sentenced to death.")

def snake_2():
	print "You accepted my challenge."
	print "Clearly surprised you accepted his challenge."
	print "Here it is ....."
	print """
	I'm teary-eyed but never cry.
	Silver-tongued, but never lie.
	Double-winged, but never fly.
	Air-cooled, but never dry.

	What am I?
	"""
	choice = raw_input ("> ")
	if choice == "Mercury":
		print "Well done the prisoner congratulates you. Moving aside for you to pass."
		gate_house()
	else:
		dead(The prisoner straggles you to death.)

def snake():
	print "Another prisoner is up ahead."
	print "You slowly approach him."
	print "He turns slowly."
	print "If you can successfully answer my riddle you can pass."
	print "Or ..... I kill you."
	print "Retorted the prisoner towards you."
	print "Do you accept the challenge or run?"

	choice = raw_input ("> ")
	if choice == "Accept":
		snake_2()
	elif choice == "Run":
		trapped()
	else:
		snake_2()

def fire():
	print """
	After a few days you smell smoke. 
	A British bombing raid!
	Out of nowhere fires crackle the floorboards.
	Making you very hot.
	You can either run or attempt to put out the flames.
	"""
	choice = raw_input ("> ")
	if choice == "Run":
		snake()
	elif choice == "Attempt":
		burnt()
	else:
		dead("Your lack of a decision killed you.")

def dead(why):
	print why, "That run was quite a disappointment."
	start()

def start():
	print "Welcome to the infamous Nazi prison Bavarian Munich Camp."
	print """
	You have been brought here as a spy against the mighty 1000 year Reich.
	Upon arrival you are situated in a unlocked room.
	Do you leave or wait?
	"""

	choice = raw_input ("> ")
	if choice == "Leave":
		mad_scientist()
	elif choice == "Wait":
		fire()
	else:
		dead("The Reich had high hopes for your escape.")
start()