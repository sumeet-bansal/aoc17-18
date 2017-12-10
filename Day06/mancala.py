with open('input.txt', 'r') as file:
	banks = [int(blocks.rstrip('\n')) for blocks in file.readline().split('\t')]

configs = []
redists = 0

while True:
	redists += 1
	maxelem = max(banks)
	index = banks.index(maxelem)
	banks[index] = 0
	for i in range(maxelem):
		index += 1
		banks[index % len(banks)] += 1
	encode = " ".join(map(str, banks))
	if encode in configs:
		print("circular list of %d redistributions" % (len(configs)-configs.index(encode)))
		break
	else:
		configs.append(encode)

print("%d redistributions of the wealth" % redists)
