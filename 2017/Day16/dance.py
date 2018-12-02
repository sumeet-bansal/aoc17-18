# takes input as list of instructions
with open('input.txt', 'r') as file:
	routine = file.read().split(',')

def spin(lineup, n):
	return lineup[-n:] + lineup[:-n]

def exchange(lineup, i, j):
	lineup[i], lineup[j] = lineup[j], lineup[i]
	return lineup

def partner(lineup, a, b):
	i = lineup.index(a)
	j = lineup.index(b)
	lineup[i], lineup[j] = lineup[j], lineup[i]
	return lineup

# runs through the routine on a given lineup n times
def dance(lineup, n):
	seen = []
	for i in range(n):
		s = ''.join(lineup)
		if s in seen:
			return seen[n % i]
		seen.append(s)

		for move in routine:
			if move[0] == 's':
				lineup = spin(lineup, int(move[1:]))
			elif move[0] == 'x':
				i, j = map(int, move[1:].split('/'))
				lineup = exchange(lineup, i, j)
			elif move[0] == 'p':
				a, b = move[1:].split('/')
				lineup = partner(lineup, a, b)

	return ''.join(lineup)

lineup = list("abcdefghijklmnop")

# first half
print(dance(lineup[:], 1))

# second half
print(dance(lineup[:], 1000000000)) #1000000000))
