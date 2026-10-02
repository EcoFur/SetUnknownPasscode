import random
b = int(input("Digs="))
s = int(input("Steps="))
lp = input("Left ex-keys(1)=")
if(lp==""):
 lp = 1
lp=int(lp)
rp = input("Right ex-keys(2)=")
if(rp==""):
 rp = 2
rp=int(rp)

now = 0
output = "O"

for i in range(b):
  for j in range(s-1):
    rand = 0
    while(rand == 0):
      rand = random.randint(-now-lp, 9+rp-now)
    if(rand > 0):
        output += "R" + str(rand)
        now += rand
    if(rand < 0):
        output += "L" + str(-rand)
        now += rand

  rand = 0
  while(rand == 0):
    rand = random.randint(-now, 9-now)
  if(rand > 0):
    output += "R" + str(rand)
    now += rand
  if(rand < 0):
    output += "L" + str(-rand)
    now += rand
  output += "P"
output += "O"
print(output)
