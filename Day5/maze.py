from copy import deepcopy	# necessary to regenerate the original tuple for each part

# takes input list of instructions as a tuple
with open('input.txt', 'r') as file:
	instruction_set = [int(instr.rstrip('\n')) for instr in file.readlines()]

# first half
jumps = 0
index = 0

instructions = deepcopy(instruction_set)

while (index < len(instructions)):
	instructions[index] += 1
	index += instructions[index] - 1
	jumps += 1

print(jumps)

# second half
jumps = 0
index = 0
crumb = 0

instructions = deepcopy(instruction_set)

while (index < len(instructions)):
	crumb = index
	index += instructions[index]
	instructions[crumb] += 1 if instructions[crumb] < 3 else -1
	jumps += 1

print(jumps)
