# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


if not year%4:
  if not year%100:
    if not year%400:
      print("Leap!") 
    else:
      print("Not Leap")
  else:
    print("Leap!") 
else:
  print("Not Leap")

