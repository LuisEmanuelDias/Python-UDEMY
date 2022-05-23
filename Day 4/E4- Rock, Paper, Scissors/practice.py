rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def R_P_S(a):
    if a==0:
        return (rock)
    if a==1:
        return (paper)
    if a==2:
        return (scissors)

#Write your code below this line 👇
import random
while 1:
    
    election = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")
    machine = random.randint(0,2)
    data= (int(election),machine)

    win= [(0,2),(1,0),(2,1)]
    lose=[(0,1),(1,2),(2,0)]
    tie= [(1,1),(2,2),(0,0)]
  
    print("You"+R_P_S(data[0])+'\n'+"Machine\n"+R_P_S(data[1]))

        
    print( "\n"+ (data in win)*"You win\n" + (data in lose)*"You lose\n" + (data in tie)*"TIE\n")


  
  
  