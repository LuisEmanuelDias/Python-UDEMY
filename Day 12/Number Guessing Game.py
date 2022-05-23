import random

logo = '''
                                                                                                                                                   
 _________________  ____   ____      ______          _____   ______    ____   ____      ______  _______         _____        ______        _____   
/                 \|    | |    | ___|\     \        |\    \ |\     \  |    | |    |    |      \/       \   ___|\     \   ___|\     \   ___|\    \  
\______     ______/|    | |    ||     \     \        \\    \| \     \ |    | |    |   /          /\     \ |    |\     \ |     \     \ |    |\    \ 
   \( /    /  )/   |    |_|    ||     ,_____/|        \|    \  \     ||    | |    |  /     /\   / /\     ||    | |     ||     ,_____/||    | |    |
    ' |   |   '    |    .-.    ||     \--'\_|/         |     \  |    ||    | |    | /     /\ \_/ / /    /||    | /_ _ / |     \--'\_|/|    |/____/ 
      |   |        |    | |    ||     /___/|           |      \ |    ||    | |    ||     |  \|_|/ /    / ||    |\    \  |     /___/|  |    |\    \ 
     /   //        |    | |    ||     \____|\          |    |\ \|    ||    | |    ||     |       |    |  ||    | |    | |     \____|\ |    | |    |
    /___//         |____| |____||____ '     /|         |____||\_____/||\___\_|____||\____\       |____|  /|____|/____/| |____ '     /||____| |____|
   |`   |          |    | |    ||    /_____/ |         |    |/ \|   ||| |    |    || |    |      |    | / |    /     || |    /_____/ ||    | |    |
   |____|          |____| |____||____|     | /         |____|   |___|/ \|____|____| \|____|      |____|/  |____|_____|/ |____|     | /|____| |____|
     \(              \(     )/    \( |_____|/            \(       )/      \(   )/      \(          )/       \(    )/      \( |_____|/   \(     )/  
      '               '     '      '    )/                '       '        '   '        '          '         '    '        '    )/       '     '   
                                        '                                                                                       '                  
'''

def tooclose(prediction,machine):
    if prediction<machine:
        print("Too low\nGuess again.")
        return False
    elif prediction>machine:
        
        print("Too high\nGuess again.")
        return False
    else :
        return True
    

def difficult_function(dif,m):
    attemp = 0
    if dif=="easy":
        print("You have 10 attempts!")
        attemp = 10
        while attemp>0:
            player_number = input("Make a guess: ")
            if not tooclose(int(player_number),m):
                attemp -= 1
                print(f"You have {attemp} attempts remaining to guess the number")
            else:
                attemp = -3
        print((attemp==-0)*f"You LOSE, the number correct is {m}" + (attemp==-3)*"You WIN!!")
            
            
    elif dif=="hard":
        attemp = 5
        print("You have 5 attempts!")
        while attemp>0:
            player_number = input("Make a guess: ")
            if not tooclose(int(player_number),m):
                attemp -= 1
                print(f"You have {attemp} attempts remaining to guess the number")
            else:
                attemp = -3
        print((attemp==-0)*f"You LOSE, the number correct is {m}\n\n" + (attemp==-3)*"You WIN!!\n\n")
    
while True:    
    print(f"{logo}\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    number = random.randint(1,100)
    difficult = input("Choose a difficulty. Type 'easy' or 'hard': ")
    difficult_function(difficult,number)