import random

try:
	file = open("lstA.txt","r")
	lestA=file.read()
except:
	lestA=[0,1,2,3,4,5,6,7,8,9]

file = open("repeatA.txt","r")
blockA=str(file.read())
print("Block is "+str(blockA))
print([ele for ele in lestA if ele != blockA])
resA = random.choice([ele for ele in lestA if ele != blockA])
print("Updated "+resA)
with open("repeatA.txt", "w") as file:
	file.write(str(resA))