from math import pow as prob 
from math import sqrt as square 
from random import randint as rad 
from random import shuffle as shuf
from random import choice as cho

result_1= prob(2,4)
print("result_1 is", result_1)

result_2= square(16)
print("result_2 is", result_2)


result_3= rad(0,100)
print("result_3", result_3)

names= ["ibra", "nawaf", "Naif", "fahad", "moha"]
print("original names:",names)

shuf(names)
print("name after shuffling:",names)

result_4= cho(names)
print("chosen name is:", result_4)