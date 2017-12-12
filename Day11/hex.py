# takes input as list of steps
with open('input.txt', 'r') as file:
	path = file.readline().rstrip('\n').split(',')

# navigates the hex coord grid
x = 0
y = 0
z = 0
dists = []
for step in path:
  if step == 'n':
    y += 1
    z -= 1
  elif step == 'nw':
    x -= 1
    y += 1
  elif step == 'sw':
    x -= 1
    z += 1
  elif step == 's':
    y -= 1
    z += 1
  elif step == 'se':
    x += 1
    y -= 1
  elif step == 'ne':
    x += 1
    z -= 1
  dists.append((abs(x) + abs(y) + abs(z)) / 2)

# first half
print("hex distance at end of path:\t%d steps" % dists[-1])

# second half
print("max hex dist at any path step:\t%d steps" % max(dists))
