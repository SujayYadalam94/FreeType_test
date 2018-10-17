import os.path
import sys

'''
This is for dynamic linked test
val_list= {'a':2923, 'b':1706, 'c':1978, 'd':2095, 'e':2880, 'f':2294, 'g':4511, 'h':2564, 'i':2411, 'j':2180, 'k':4033, 'l':1921, 'm':3780, 'n':2618, 'o':2039, 'p':2285, 'q':2025, 'r':1761, 's':3466, 't':1513, 'u':2001, 'v':4367, 'w':5930, 'x':4907, 'y':4033, 'z':2402}
'''

val_list = {'a':2222, 'b':1201, 'c':1592, 'd':1496, 'e':2762, 'f':1801, 'g':3509, 'h':1842, 'i':2090, 'j':1658, 'k':3331, 'l':1703, 'm':2616, 'n':1962, 'o':1709, 'p':1480, 'q':1427, 'r':1166, 's':2858, 't':1125, 'u':1492, 'v':4335, 'w':5826, 'x':4166, 'y':3410, 'z':2140}


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
'''
For dynamic linked library	
addr_list.append(f.count("0x7ffff7b62000"))
addr_list.append(f.count("0x7ffff7b63000"))
addr_list.append(f.count("0x7ffff7b64000"))
addr_list.append(f.count("0x7ffff7b67000"))
addr_list.append(f.count("0x7ffff7b68000"))
addr_list.append(f.count("0x7ffff7b69000"))
addr_list.append(f.count("0x7ffff7b6a000"))
addr_list.append(f.count("0x7ffff7b53000"))
addr_list.append(f.count("0x7ffff7b55000"))
addr_list.append(f.count("0x7ffff7b4e000"))
addr_list.append(f.count("0x7ffff7b4f000"))
'''

addr_list.append(f.count("0x42a000"))
addr_list.append(f.count("0x42d000"))
addr_list.append(f.count("0x42e000"))
addr_list.append(f.count("0x42f000"))
addr_list.append(f.count("0x430000"))
addr_list.append(f.count("0x431000"))
addr_list.append(f.count("0x405000"))

for val in addr_list:
	sum += val

try:
	print val_list.keys()[val_list.values().index(sum)]
except:
	print "Value %d not present in list\n" % sum
