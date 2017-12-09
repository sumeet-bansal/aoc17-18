with open('input.txt', 'r') as file:
	stream = file.readline()

score = 0
level = 0
garbage = False
ignored = False
count = 0
for char in stream:
	if ignored:
		ignored = False
		continue

	if char == '!':
		ignored = True
		continue

	if char == '>':
		garbage = False

	if garbage:
		count += 1
		continue

	if char == '<':
		garbage = True
		continue

	if char == '{':
		level += 1

	if char == '}':
		score += level
		level -= 1

print("garbage count: %d" % count)
print("stream score: %d" % score)