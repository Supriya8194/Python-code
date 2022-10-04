import random




values = []  #10 numbers --> kaise- -> divisible by 3 numbers --> which loop you will

# i want 10 numbers -- div by 3
for item in range(10):
    num = random.randint(1, 100)
    #print(num)
    if num%3 == 0:
        values.append(num)

print(values)

print('-------------------------')
val = []
counter = 0
while len(val)<10:
    counter = counter + 1
    num = random.randint(1, 100)
    if num % 3 == 0:
        val.append(num)

print(val)# min - max --> in
print(counter)
#there can 0-10

#values = [573, 766, 288, 200, 393, 527, 788, 642, 995, 810]

#for element in values:
#   if element % 3 == 0:
#       print(element)