from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want to continue, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I am going to write these to the file."

target.write(line1 + "\n" + line2 + "\n" + line3)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
target.close()
target = open(filename)
#line4 = target.read()
print "Here is the data you entered"
print target.read()
#print "The file now reads: %s." % line4
print "And finally, we close the file %r." % filename
target.close()
