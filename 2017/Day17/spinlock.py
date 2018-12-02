# takes step num as argument
import sys
steps = int(sys.argv[1])

circbuff = list([0])

# first half
pos = 0
for i in range(1, 2018):
	pos = (pos + steps) % len(circbuff)
	circbuff.insert(pos + 1, i)
	pos += 1
print("value after 2017 in the buffer:\t%d" % circbuff[pos+1])

# second half
pos = 0
nextv = -1
for i in range(1, 50000001):
	pos = (pos + steps) % i
	if pos == 0:
		nextv = i
	pos += 1
print("value after 0 with 50m inserts:\t%d" % nextv)