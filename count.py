import os.path
import sys

sum = 0
addr_list = []
#filename = raw_input("Enter file name\n")
if len(sys.argv) < 2:
	print "Filename not passed. Exiting\n"
	exit(1)

filename = sys.argv[1]
filename += ".txt"
if os.path.isfile(filename):
	f = open(filename).read()
else:
	print "File does not exist\n"
	exit()

addr_list.append(f.count("0x42a000"))
addr_list.append(f.count("0x42d000"))
addr_list.append(f.count("0x42e000"))
addr_list.append(f.count("0x42f000"))
addr_list.append(f.count("0x430000"))
addr_list.append(f.count("0x431000"))
addr_list.append(f.count("0x405000"))


for val in addr_list:
	sum += val
#	print val,
	
print sum

