import sys
from math import sqrt, floor, fabs

def main(n):
	pos = floor(sqrt(n))
	pos = pos - 1 if pos % 2 == 0 else pos
	print("lower bound of %d" % pow(pos, 2))
	x = pos // 2
	y = -x

	print("initial position at (%d, %d), value %d" % (x, y, pow(pos, 2)))

	if (pow(pos, 2) == n):
		print("no additional steps needed")
		return

	x += 1
	if n < (pow(pos, 2) + 1 + pos):
		y += n - (pow(pos, 2) + 1)
	elif n < (pow(pos, 2) + 2*pos + 2):
		y += pos
		x -= n - (pow(pos, 2) + 1 + pos)
	elif n < (pow(pos, 2) + 3*pos + 3):
		y += pos
		x -= pos + 1
		y -= n - (pow(pos, 2) + 2*pos + 2)
	elif n < pow(pos + 2, 2):
		y -= 1
		x -= pos + 1
		x += n - (pow(pos, 2) + 3*pos + 3)

	print("final position at (%d, %d)" % (x, y))
	x = fabs(x)
	y = fabs(y)
	print("%d + %d = %d" % (x, y, x + y))

if __name__ == "__main__":
	n = int(sys.argv[1])
	main(n)
