import sys

# first half
genA = int(sys.argv[1])
genB = int(sys.argv[2])

mask = 0xffff
matches = 0
for i in range(40000000):
	genA *= 16807
	genB *= 48271
	genA %= 2147483647
	genB %= 2147483647
	sam = genA & mask
	rin = genB & mask
	if sam == rin:
		matches += 1

print("judge's final count without generator criteria:\t%d" % matches)

# second half
genB = int(sys.argv[2])

def generateA():
	genA = int(sys.argv[1])
	while True:
		genA *= 16807
		genA %= 2147483647
		if genA % 4 == 0:
			yield genA

def generateB():
	genB = int(sys.argv[2])
	while True:
		genB *= 48271
		genB %= 2147483647
		if genB % 8 == 0:
			yield genB

mask = 0xffff
matches = 0
genA = generateA()
genB = generateB()
for i in range(5000000):
	sam = genA.next() & mask
	rin = genB.next() & mask
	if sam == rin:
		matches += 1

print("judge's final count with filtered generators:\t%d" % matches)
