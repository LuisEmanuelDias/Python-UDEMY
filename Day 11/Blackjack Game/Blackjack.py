import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   


def pick_card(mazo):
    '''pick a card from deck "mazo" and return current deck without
the card picked'''
    pick = random.choice(mazo)
    mazo.remove(pick)
    return [pick,mazo]

def dealer_decision(m,mazo):
    '''m is a list with the first two cards,
mazo is the current deck (without card picked previously),
return cards in accordance with dealer rules 
'''
    cards = {}
    picked = 0
    cards[sum(m)]=m
    s=m+[]
    if 1 in m:
        s[s.index(1)]=11
        cards[sum(s)]= s
    while True in [True for x in cards.keys() if x<17] and (not 21 in cards.keys()) and (not 20 in cards.keys()) :
        premazo= []
        
        premazo = pick_card(mazo)
        mazo=premazo[1]
        picked = premazo[0]
        
        premazo = {}
        premazo = cards.copy()
        cards.clear()
        
        for k,l in premazo.items():
            cards[sum(l+[picked])]= l+[picked]
                   
        if picked==1:
            for k,l in premazo.items():
                cards[sum(l+[11])]= l+[11]
    premazo= list(cards.keys())
    premazo.sort(reverse=True)
    for x in premazo:
        if x<22:
            return cards.get(x)
            break
    return cards.get(premazo[len(premazo)-1])

def who_win(user,dealer):
    '''Depending of user and dealer's cards, the function return Win,Lose or Tie'''
    user = sum(user)
    dealer = sum(dealer)
    if user>21:
        return "YOU LOSE"
    elif user==dealer:
        return "Tie"
    elif dealer>21:
        return "YOU WIN!!"
    elif user>dealer:
        return "YOU WIN!!"
    else:
        return "YOU LOSE"


while True:
    print(logo)
    print("Welcome to the blackjack game")
    get_card = True
    mazo = [1,2,3,4,5,6,7,8,9,10]*4 + [10,10,10]*4
    cards_dealer=[]
    cards_user = []
    tomar_carta = [0,mazo]
    for n in range(2):
        tomar_carta= pick_card(tomar_carta[1])
        cards_dealer += [tomar_carta[0]]
    
    for n in range(2):
        tomar_carta= pick_card(tomar_carta[1])
        cards_user += [tomar_carta[0]]
        
    while get_card:
        print(f"Your cards: {cards_user}\n Computer's first card: {cards_dealer[0]}")
        if sum(cards_user)<22:
            get_card = input("Type 'yes' to get another card, whatever to pass:\n\n")=='yes'
        else: get_card = False
        
        if get_card:
            tomar_carta=pick_card(tomar_carta[1])
            cards_user += [tomar_carta[0]]
            
        else:
            cards_dealer = dealer_decision(cards_dealer,tomar_carta[1])
            print(f"-Your cards:\t{cards_user}\n-Computer's cards:\t{cards_dealer}\n")
            print(who_win(cards_user,cards_dealer),"\n - - - - - - - - - - - - - - - - -")
            
    

    