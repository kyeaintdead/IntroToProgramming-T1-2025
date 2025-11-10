for i in range(20):
    if i == 16:
        break
    print(i)

for i in range(30):
    if i % 2 == 0:
        continue
    print(i)    


for i in range(15):
    if i == 13:
        pass #have a break here 
    print(i)


for i in range(10,0,-1):
    if i == 5:
        continue
    print(i)



list = [1,2,3,4,5,6, -7]
total = 0
for num in list:
    if num < 0:
        break
    total += num

print(total)