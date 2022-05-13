
#openNumbers = open('week1input.txt', 'r')
#readNumbers = openNumbers.read()
#print (readNumbers)
#openNumbers.close()

"""
with open('week1input.txt') as x:
   for line in x:

       print (line)
    """

#with open('week1input.txt') as x:
 #   for i in range(len(x)):
 #       print(x[i])


"""
a_file = open("week1input.txt")
y = 0
x = [y-1]

for i, value in enumerate(a_file):
   
    newnum = i+1
    print(i, value)
    i+=1
    if newnum < i:
        print("counted")
    
    if x < i:
        print(i)
"""



"""
a_file = open("week1input.txt")

i = 0
counter = 0
for line1 in a_file:
    i +=1

    for line2 in a_file:

        if line1 < line2:
            counter +=1


print(counter)
"""


with open('week1input.txt', 'r') as f:

    lines = f.readlines()
    measurements = [int(entry.strip()) for entry in lines]

prev_entry = measurements[0]
increases = 0

for entry in measurements[1:]:
    if entry > prev_entry:
        increases += 1
    prev_entry = entry

print (increases)

f.close