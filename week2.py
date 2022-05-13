
import re

with open('week2input.txt', 'r') as f:

    lines = f.readlines()
a = "forward"
b = "up"
c = "down"
forward = 0
depth = 0
for entry in lines:
    num = re.findall(r'\d+', entry)[-1]
    if a in entry:
        forward += int(num)
    elif b in entry:
        depth -= int(num)
    else:
        depth += int(num)
answer = forward*depth
print(f"Total distance travelled forward is: {forward}")
print(f"Finishing depth value is: {depth}")
print(f"Final Answer = {answer}")
