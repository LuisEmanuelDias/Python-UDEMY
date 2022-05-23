# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

decimal = 0
unit= 0
name = name1+name2
name = name.lower()

for x in "true":
  decimal += name.count(x) 

for x in "love":
  unit += name.count(x) 

print(f"Your score is {decimal}{unit}")

