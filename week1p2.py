

data = open('week1input.txt', 'r').read().splitlines()

depths = [int(x) for x in data]

increases = sum(x < y for x, y in zip(depths, depths[3:]))

print(increases)