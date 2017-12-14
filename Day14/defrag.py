# rotates the list n times; n < 0 for left shift, otherwise right shift
def rotate(l, n):
    return l[n:] + l[:n]

# reverses a sublist using the given indices
def subrev(lst, start, end):
    lst[start:end] = lst[start:end][::-1]
    return lst

with open('input.txt', 'r') as file:
	key = file.readline()


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
	return ''.join(dense)

print(''.join([knothash('%s-%d' % (key, i)) for i in range(128)]).count('1'))

# num of islands for pt 2
# print([[int(char) for char in knothash('%s-%d' % (key, i))] for i in range(128)])