# rotates the list n times; n < 0 for left shift, otherwise right shift
def rotate(l, n):
    return l[n:] + l[:n]

# reverses a sublist using the given indices
def subrev(lst, start, end):
    lst[start:end] = lst[start:end][::-1]
    return lst

# first half
with open('input.txt', 'r') as file:
	lengths = [int(length) for length in file.readline().split(',')]

pos = 0
skip = 0
knot = list(range(256))
for length in lengths:
	knot = rotate(knot, pos % len(knot))
	subrev(knot, 0, length)
	knot = rotate(knot, -pos % len(knot))
	pos += length + skip
	skip += 1

print(knot[0] * knot[1])

# second half
with open('input.txt', 'r') as file:
	lengths = [ord(char) for char in file.readline()] + [17, 31, 73, 47, 23]

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
dense = ['{:02x}'.format(reduce(lambda i, j: i^j, dense)) for dense in sparse]

print(''.join(dense))
