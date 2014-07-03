import re
import sys

f = open("trace_after_crash.txt")            


while f:
	line = f.readline()
	print line
f.close()