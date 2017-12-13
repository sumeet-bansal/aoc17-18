firewalls = {}
with open('input.txt', 'r') as file:
	for line in file.read().splitlines():
		depth = int(line[:line.index(':')])
		scanrange = int(line[line.index(' ') + len(' '):])
		firewalls[depth] = [scanrange, 1, True]

severity = 0
pos = -1
while pos < depth:
	pos += 1
	if pos in firewalls and firewalls[pos][1] == 1:
		severity += pos * firewalls[pos][0]
	for layer in firewalls:
		if firewalls[layer][1] == firewalls[layer][0]:
			firewalls[layer][-1] = False
		if firewalls[layer][1] == 1:
			firewalls[layer][-1] = True
		firewalls[layer][1] += 1 if firewalls[layer][-1] else -1

print(severity)