# takes input list of phrases as list of lists
with open("input.txt", "r") as file:
	passphrases = [line.rstrip('\n').split(' ') for line in file.readlines()]

# first half
print(sum([1 for phrase in passphrases if len(phrase) == len(set(phrase))]))

# second half
print(sum([1 for phrase in [["".join(sorted(word)) for word in phrase] for phrase in passphrases] if len(phrase) == len(set(phrase))]))