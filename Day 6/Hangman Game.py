import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def pick_word():    
    file_words= open("L:/Universidad/2021/New Courses UDEMY/100 Days of Code - Python bootcamp/Day 6/words.txt")
    file_words = file_words.read()
    word = ""
    while len(word)<4:
        word= random.choice(file_words.split())
    return word

def find_word(a,actual_word,word):    
    if a== 0:
        return ("_ "*(len(word)))[:len(word)*2 - 1]
    elif a== 1:
        return " ".join(list(word.lower()))
    else:
        word= " ".join(list(word.lower()))
        for x in range(len(word)):
            if word[x].lower()==a.lower():
                actual_word = actual_word[:x]+a+actual_word[x+1:]
    return actual_word

while True:
    print("Welcome to HANGMAN GAME, you have 5 lives. Be careful. Don't lose the head!")
    life_counter=5
    word = pick_word()
    word_show= find_word(0,"",word)

    while life_counter>0:
        print(stages[5-life_counter])
        print(word_show)
        word_input =input("Adivine a word: ").lower()
         
        if word_show is not find_word(word_input,word_show,word):
            word_show = find_word(word_input,word_show,word)
            
        else:
            life_counter -= 1
            print(f'You have {life_counter} lives')
            
        if life_counter==0:
            print(f'You Lose, the word was "{word}"')
            print(stages[6])
        if word_show == find_word(1,"",word):
            print('You Win!!')
            life_counter=0
    
        
#    print()
#    if 

#r