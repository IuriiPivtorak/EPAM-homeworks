x = int(input()) # 1st value
y = int(input()) # 2nd value

while (x!=0) & (y!=0): # until values become 0
    if x > y: # looking for bigger value
        x = x % y # updating it with mod
    else:
        y = y % x # updating
print (x+y) # greatest common diviser
