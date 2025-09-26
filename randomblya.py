import random as rd
count=0
number=0
while number<12:
    number=rd.randint(2, 12)
    print(number) 
    count+=1
print(number, "after", count, "tries") 