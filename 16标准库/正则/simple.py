import re

line = "Cats are smarter than dogs"

pattern = re.compile('^Cat(.)+dogs$')
match = pattern.match(line)

print("match", match)


match = pattern.match("tom")

print("match", match)

