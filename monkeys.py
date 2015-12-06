import string
from random import choice

def write_shakespeare():
	goal = "methinks it is like a weasel"
	alphabet = string.ascii_lowercase
	alphabet += " "
	attempt = ""
	trials = 0
	while attempt != goal:
		attempt = ""
		for  i in range(len(goal)):
			letter = choice(alphabet)
			attempt += letter
		if not trials % 1000:
			print attempt
		trials += 1
	print "Result:", attempt
	print "Trials:", trials

"""For the next version, I want to compare the attempt string with 
the goal string and store the correct characters in a list at that 
character's index. Then make guess only for the unsolved characters 
and see how long that takes."""