counter = 5


# when we create a new function, it create a new scope inside the function
def increase_counter(amt):
    global counter # gobal is a way to access the viriable outside the function
    counter += amt

def decrease_counter(amt):
    global counter
    counter -= amt

# print(counter)
increase_counter(3)
# print(counter)


# while loop
myList = []

while len(myList) < 5: # will excutive the code until the statement become false
    myList.append(0)

# print(myList)

myNumber = 2

# while myNumber % 7 != 0:
#     myNumber += 7 # this will create an infinite loop, use break condition to stop loop


counter2 = 1
total = 0
while counter2 < 10:
    counter2 += 1
    if counter % 5 == 0:
        continue
    else:
        total += counter

print(counter2)







pets = {
    "dog": 3,
    "cat": 2,
    "fish": 6
}

for key in pets:
    print(key, pets[key])

for key in pets.keys():
    print(key)

for value in pets.values():
    print(value)

for key, value in pets.items():
    print(key,value)


# del pets["cat"] --- remove key
# pets["dog"] = 5 ---- change value




    
        