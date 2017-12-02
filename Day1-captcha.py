# takes captcha as argument
import sys
input = sys.argv[1]

# first half
print(sum([int(num) for i, num in enumerate(input) if (input[i] == input[(i+1) % len(input)])]))

# second half
print(sum([int(num) for i, num in enumerate(input) if (input[i] == input[(i + int(len(input)/2)) % len(input)])]))
