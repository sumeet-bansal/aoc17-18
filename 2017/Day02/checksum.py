# takes input spreadsheet as tuple of tuples
with open('input.txt', 'r') as file:
	spreadsheet = tuple([tuple(map(int, line.split('\t'))) for line in file.readlines()])

# first half
print(sum([max(row) - min(row) for row in spreadsheet]))

# second half
from itertools import combinations
combinations = tuple([tuple(combinations(row, 2)) for row in spreadsheet])
print(int(sum([max(pair)/min(pair) for pairs in combinations for pair in pairs if max(pair) % min(pair) == 0])))
