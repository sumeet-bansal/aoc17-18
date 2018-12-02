from functools import reduce

# rotates the list n times; n < 0 for left shift, otherwise right shift
def rotate(l, n):
    return l[n:] + l[:n]

# reverses a sublist using the given indices
def subrev(lst, start, end):
    lst[start:end] = lst[start:end][::-1]
    return lst

key = open('input.txt', 'r').readline()

def knothash(key):
	lengths = [ord(char) for char in key] + [17, 31, 73, 47, 23]

	pos = 0
	skip = 0
	knot = list(range(256))
	for n in range(64):
		for length in lengths:
			knot = rotate(knot, pos % len(knot))
			subrev(knot, 0, length)
			knot = rotate(knot, -pos % len(knot))
			pos += length + skip
			skip += 1

	sparse = [knot[i:i+16] for i in range(0, len(knot), 16)]
	dense = ['{:02b}'.format(reduce(lambda i, j: i^j, dense)) for dense in sparse]
	dense = [('0' * (8-len(d))) + d for d in dense]
	return ''.join(dense)

print(''.join([knothash('%s-%d' % (key, i)) for i in range(128)]).count('1'))

def findIsland(graph):
	for xi, x in enumerate(graph):
		for yi, y in enumerate(x):
			if y == 1:
				return (xi, yi)
	return (-1, -1)

graph = [[int(char) for char in knothash('%s-%d' % (key, i))] for i in range(128)]
islands = 0
while True:
	isl = findIsland(graph)
	if isl == (-1, -1):
		break
	neighbors = set()
	neighbors.add(isl)
	while len(neighbors):
		(x, y) = neighbors.pop()
		if x < 0 or x >= len(graph) or y < 0 or y >= len(graph[x]):
			continue
		if graph[x][y] == 0:
			continue
		graph[x][y] = 0
		for nx in [x-1, x+1]:
			neighbors.add((nx, y))
		for ny in [y-1, y+1]:
			neighbors.add((x, ny))
	islands += 1

print(islands)