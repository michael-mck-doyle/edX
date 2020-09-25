
# variables in python

x = "yellow"
print(x.capitalize())

print(x.lower())

# for loops & range

print("No range step included")
for i in range(0, 10):
    print(i)

print()

print("Range step = 2")
for i in range(0, 10, 2):
    print(i)

print()
print("Starting at value 3, range step 3")
for i in range(3, 17, 3):
    print(i)

print()
print("going backwards, counting down")
for i in range(15, 0, -2):
    print(i)

# while loops
print()
print("While loops")
i = 2
while i < 10:
    print(i)
    i += 2

# conditionals
print()
print("Conditionals")
for i in range(0, 10):
    if i % 2 == 0:
        print(i)
    else:
        print(str(i) + " is not a modulo")
