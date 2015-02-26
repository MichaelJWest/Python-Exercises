cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#Shows many many cars are available, 100
print "There are", cars, "cars available."
#Prints the amount of drivers, 30
print "There are only", drivers, "drivers available."
#Prints the cars not driven
print "There will be", cars_not_driven, "empty cars today."
#Prints the amount of people we can transport
print "We can transport", carpool_capacity, "people today."
#Prints amount of people requiring lift
print "We have", passengers, "to carpool today."
#Splits up people into cars equally
print "We need to put about", average_passengers_per_car, "in each car."