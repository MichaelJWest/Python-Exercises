#Sets the function, and states it's variables, amounts of cheese and crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	#prints amount of cheese
	print "You have %d cheeses!" % cheese_count	
	#rpints amount of crackers
	print "You have %d boxes of crackers!" % boxes_of_crackers
	#prints 2 strings with new line at end
	print "Man that's enough for a party!"
	print "Get a blanket. \n"
#calls the function with values 20 and 30 
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)
#sets variables then calls the function with the variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10 
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#does math inside the calling
print "we can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
#combines the variables and the math
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
