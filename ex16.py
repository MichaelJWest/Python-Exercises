from sys import argv
#allows us to use argument variables
script, filename = argv
#sets the argument variables
print "We're going to erase %r." % filename
#says what we're going to erase
print "If you don't want that, hit CTRL-C (^C)."
#asks user to stop the script if they want to opt out
print "If you do want that, hit RETURN."
#asks user to hit return to continue
raw_input("?")
#user hits enter here
print "Opening the file..."
target = open(filename, 'w')
#opens the file listed in the argument variables, filename
print "Truncating the file. Goodbye!"
target.truncate()
#this truncates the desired file
print "Now I'm going to ask you for three lines."
#asks for 3 lines
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
#sets line1-3 variables with raw input
print "I'm going to write these to the file."

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

#this writes line1-3 with a new line in-between
target = open(filename, 'r')
#this sets the file available for reading
print "Here's your file %r:" % filename
print target.read()
print "And finally, we close it."
target.close()
#this closes the chosen file having written line1-3 to it
