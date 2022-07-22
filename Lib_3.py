import math as name
import random as price

result_1= name.pow(2,4)
print("result_1 is", result_1)

result_2= name.sqrt(16)
print("result_2 is", result_2)


result_3= price.randint(0,100)
print("result_3", result_3)

names= ["ibra", "nawaf", "Naif", "fahad", "moha"]
print("original names:",names)

price.shuffle(names)
print("name after shuffling:",names)

result_4= price.choice(names)
print("chosen name is:", result_4)