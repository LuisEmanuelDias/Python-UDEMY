import os

def clearConsole():
    command = 'cls'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

from art import logo

#HINT: You can call clear() to clear the output in the console.

print(f"{logo}\nWelcome to the secret auction program")
new_bidder=True
best_bidder = {}
bidders = {}
while new_bidder:
  name = input("What's your name?: ")
  bid = input("What's your bid?: ")

  bidders[name] = int(bid)

  new_bidder = input("Are there any other bidders? (yes or no) ").lower() == 'yes'

  clearConsole()
  
for k,l in bidders.items():
    if  l== max(bidders.values()):
        best_bidder[k]=l

print(f"The winner is {list(best_bidder.keys())[0]} with a bid of {list(best_bidder.values())[0]}")
  
