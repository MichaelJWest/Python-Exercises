def gold_room():
	print "This room is full of gold, How much do you take?"
	
	next = raw_input("> ")
	try:
		how_much = int(next)
	except ValueError:
		dead('man, learn how to type a number')
	
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		end_room()
	else:
		dead("You greedy bastard!")

def gold_room():
	print "This room is full of gold, How much do you take?"
	
	next = raw_input("> ")
	if next.isdigit():
		how_much = int(next)
	else:
		dead('man, learn how to type a number')
	
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		end_room()
	else:
		dead("You greedy bastard!")
		