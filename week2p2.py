
import re

with open('week2input.txt', 'r') as f:
    lines = f.readlines()
a = "forward"
b = "up"
c = "down"
forward = 0
depth = 0
aim = 0
for entry in lines:
    num = re.findall(r'\d+', entry)[-1]
    if a in entry:
        forward += int(num)
        depth += (int(num)*aim)
    elif b in entry:
        aim -= int(num)
    else:
        aim += int(num)
fin_answer = depth*forward
print(f"Total distance travelled forward is: {forward}")
print(f"Finishing depth value is: {depth}")
print(f"Final Answer = {fin_answer}")

