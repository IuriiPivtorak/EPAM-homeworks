x = abs(int(input("input 1st value: "))) # 1st value
y = abs(int(input("input 2nd value: "))) # 2nd value

while (x!=0) & (y!=0): # until values become 0
    if x > y: # looking for bigger value
        x = x % y # updating it with mod
    else:
        y = y % x # updating
print (x+y) # greatest common diviser
