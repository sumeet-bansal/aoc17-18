# sets up the graph as a dict with vertices for keys and neighbor lists for values
vertices = {}
with open('input.txt', 'r') as file:
	for line in file.read().splitlines():
		vertex = line[:line.index(' <')]
		adj = line[line.index('> ') + len('> '):].split(', ')
		vertices[int(vertex)] = map(int, adj)

# recursively adds all vertices in the connected components containing param vertices
def getComponent(existing):

	# retrieves all immediate neighbors of all queried vertices
	potential = set()
	for node in existing:
		potential |= set(vertices[node])

	# param is complete component if all immediate neighbors are contained
	if potential.issubset(existing):
		return existing
	else:
		existing |= potential
		return getComponent(existing)

# first half
print("vertices in connected component containing 0:\t%d" % len(getComponent(set([0]))))

# second half
remaining = vertices.keys()
components = []
while len(remaining) > 0:
	subgraph = getComponent(set(vertices[remaining[0]]))
	remaining = [vertex for vertex in remaining if vertex not in subgraph]
	components.append(list(subgraph))
print("number of connected components in graph:\t%d" % len(components))
