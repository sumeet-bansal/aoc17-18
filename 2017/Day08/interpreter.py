import operator

# opcode dict, keys are opcodes as strings and values are operation defs
OPS = {
	'=='	:	operator.eq,
	'!='	:	operator.ne,
	'>='	:	operator.ge,
	'<='	:	operator.le,
	'<'		:	operator.lt,
	'>'		:	operator.gt,
}

# takes the input as instructions formatted [reg, inc/dec, offset, if, condreg, opcode, condval]
with open('input.txt', 'r') as file:
		instructions = [i.split(' ') for i in [line.rstrip('\n') for line in file.readlines()]]

# sets up the registers
registers = {}
for line in instructions:
	registers[line[0]] = 0

# runs through the instruction set and records postmax and max at any point
maxval = registers[max(registers, key=registers.get)]
for line in instructions:
	if OPS[line[5]](registers[line[4]], int(line[6])):
		registers[line[0]] += int(line[2]) * (1 if line[1] == 'inc' else -1)
		statemax = registers[max(registers, key=registers.get)]
		maxval = max(maxval, statemax)

# first half
print(statemax)

# second half
print(maxval)
