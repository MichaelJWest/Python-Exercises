#takes a function/module from the library to use in this program
from sys import argv
#sets the argument variables to be used
script, filename = argv
#opens the text file for use in this program
txt = open(filename)
#prints a user message naming the filename the user entered at the start
print "Here's your file %r:" % filename
#prints the opening txt file
print txt.read()
#prints request for same file name again
print "Type the filename again:"
#asks for raw input of the filename again
file_again = raw_input("> ")
#opens the file again
txt_again = open(file_again)
#prints the openetext file again
print txt_again.read()
