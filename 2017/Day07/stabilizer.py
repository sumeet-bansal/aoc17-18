# sets up the tree as a dict where each key corresponds to a node and each value is a list of that
# node's children, plus its weight as the last element in the list of children
DAG = {}
with open('input.txt', 'r') as file:
	for line in file.readlines():
		line = line.rstrip('\n')
		key = line[:line.index(' (')]
		dependencies = []
		if '->' in line:
			dependencies = line[line.index('-> ') + len('-> '):].split(', ')
		DAG[key] = dependencies
		DAG[key].append(int(line[line.index('(') + len('(') : line.index(')')]))

# first half: checks every key to see if it appears as a child in any other node's list
# if a key doesn't appear as a child, it must logically be the root of the tree/DAG
for key in DAG:
	root = True
	for children in DAG:
		if key in DAG[children]:
			root  = False
	if root:
		root = key
		break

print("tree rooted by node \'%s\'" % root)

# second half: balances the tree and prints out any adjustments that were made to do so
def balance(key):

	# base case: only one elem in child list (the weight of the node)
	if len(DAG[key]) == 1:
		return DAG[key][0]

	# recursive case: gets the combined sum of all its children
	sums = [balance(child) for child in DAG[key][:len(DAG[key])-1]]

	# if every sum isn't the same, the child with the different sum must be unbalanced
	if len(set(sums)) > 1:
		diffsum = [elem for elem in set(sums) if sums.count(elem) == 1][0]
		diff = diffsum - [elem for elem in set(sums) if sums.count(elem) > 1][0]
		diffnode = DAG[key][sums.index(diffsum)]
		DAG[diffnode][len(DAG[diffnode])-1] -= diff
		print("node \'%s\' updated to weight %d" % (diffnode, DAG[diffnode][len(DAG[diffnode])-1]))

	# returns the sum of the (now) balanced branch
	return int(DAG[key][len(DAG[key])-1]) + sum([balance(sub) for sub in DAG[key][:len(DAG[key])-1]])

balance(root)
