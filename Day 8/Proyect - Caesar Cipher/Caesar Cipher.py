def de_or_code(word,number):
    word =word.lower()
    alphab = "abcdefghijklmnopqrstuvwxyz"
    num = "0123456789"
    
    newword=""
    for x in word:
        
        if x.isalpha():
            new_index = (alphab.find(x))+number
            newword += alphab[(new_index>=26)*(new_index-26) + (0<=new_index<26)*(new_index) + (new_index<0)*(new_index+26)]
        elif x.isnumeric():
            new_index = (num.find(x))+number
            newword += num[(new_index>=10)*(new_index-10) + (0<=new_index<10)*(new_index) + (new_index<0)*(new_index+10)]
        else:
            newword += x
    return newword

while True:
    print("\nWelcome to the Caesar Cipher machine. What do you wanna do? ")
    desicion = input("code or decode?").lower()
    phrase = input("write the words(could be numbers or characters) for it: ").lower()
    shift_n= int(input("type the shift number: "))
    
    shift_n= (desicion=='code')*shift_n + (desicion=='decode')*(-1)*shift_n
    message = de_or_code(word=phrase,number=shift_n)
    print(f"\n The message is:",message)
    