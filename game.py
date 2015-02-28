from sys import exit


def how():

	choice = raw_input("> ")

	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		print "Separate those numbers from letters. Numbers only."
		if how_much < 100:
			print "Greedy. Get some decent manners with that gold."
			trapped()
		elif how_much == 1:
			print "You are quite a unusual person."

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

def guard():
	print "You found the source of the noises."
	print "A guard enjoying himself on some crystal meth."
	print "You can either leave the guard or kill him?"

	choice = raw_input ("> ")

	if choice == "Leave":
		perimeter()
	elif choice == Kill:
		print "After killing the guard you find a stack of gold."
		print "Do you take any gold?"
		choice = raw_input ("> ")
		if choice == "Yes":
			print "Greed. :( but I guess you have to survive."
			print "How much did you take?"
			how()
		elif choice == "No":
			print "Surprising!"
			trapped()
		elif choice == "Some":
			print "I bet quite a bit how much?"
			how()
		else:
			print "Can you repeat that? You were mumbling."
	else:
		dead("The guard lifts the alarm about your escape.")

def Loser_ending():
	print "Traitors and cowards always die."
	exit(0)

def mad_scientist():
	print "You pick up a blade."
	print "A deep urge picks up within you to kill this woman."
	print "Do you tell the woman your a Nazi or kill her?"

	choice  = raw_input ("> ")

	if choice == "Nazi":
		print "She turns. Suddenly she shoots you."
		Loser_ending()
	elif choice == "Kill":
		print "After a short brutal fight you pierce her throat."
		gate_house()
	else:
		print "Hurry up or die already."
		mad_scientist()

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
		dead("The prisoner straggles you to death.")

def snake():
	print "Another prisoner is up ahead."
	print "You slowly approach him."
	print "He turns slowly."
	print "If you can successfully answer my riddle you can pass."
	print "Or ..... I kill you."
	print "Retorted, the prisoner towards you."
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


name = raw_input ("What is your name?")
print "So you are %r." % (name)
print "Is it right that you are %r?" % (name)
choice = raw_input ("> ")

if choice == "yes":
	print "Ok %r let's play." % (name)
	start()
elif choice == "no":
	name = raw_input ("So what is your name?")
	print "Is it right that you are %r?" % (name)
	choice = raw_input ("> ")

	if choice == "yes":
		print "Ok %r let's play." % (name)
		start(0)
	elif choice == "no":
		name = raw_input ("So what is your name?")
		print "I'm bored of this bye."
		exit(0)
	else:
		print "Please repeat that."
else:
	print "Don't type gibberish."
