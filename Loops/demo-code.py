# printing date into the screen
print("hello world")
print("Goodbye world")

# storing data / variable
temperature = 79.5

print("the temp is", temperature)

print(type(temperature))
# this will print float, number with decimal

# int is whole positive or negative numbers

# converter
int() # remove decimal, make number whole, does not round
str() # convert to a string
float() # add decimal

# round number
round(2.343, 2) # 2 define how many space after .

temperature = 36

print(temperature)

temperature = 25

print(temperature)

temperature = temperature - 5
print(temperature)

temperature = (temperature - 32) * 5/9
print(temperature)

greeting = "Hello, how are you doing?"
greeting = greeting * 5 # duplicate the the sting 5 times, etc
greeting = greeting + " I am doing well"
print(greeting)

# Booleans
is_sunny = True
is_weekend = False
is_holiday = True
is_raingin = False

is_nice_day = is_sunny and is_weekend
print("Is is a good day to go out?" + str(is_nice_day))

# list
temperature  = [20,4,5,5,6,7]

# loops
for temp in temperature:
    print(temp)

for i in range(6):
    print("temp on day " + str(i) + " is " + str(temperature[i]))

for i in range(len(temperature)):
    print("temp on day " + str(i) + " is " + str(temperature[i]))


loopRange = range(0, 8 , 1) #(start point, end point, step)
for i in loopRange:
    i = i - 1
    print(i)

for i,temp in enumerate(temperature,3):
    print("temp " + str(i) + " is " + str(temp))

# slice
print(temperature[3:])
print(temperature[:-2])


user_age = 15

if user_age < 13: 
    category = "child"
elif user_age <20:
    category = "teenager"
elif user_age < 65:
    category = "adult"
else:
    category = "senior"

print(category)

# functions
def categorize_age(age):
    if age < 13: 
        category = "child"
    elif age <20:
        category = "teenager"
    elif age < 65:
        category = "adult"
    else:
        category = "senior"
    return category

print("category is", categorize_age(5))









