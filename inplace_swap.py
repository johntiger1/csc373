


a = 3
b = 5
print(a,b)

b = a - b
a = a - b # a = a - (a-b) # a now contains b!
b = b + a # b = a - b + b # b is now a

print (a,b)
