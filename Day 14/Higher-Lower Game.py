from art import logo


def pick_data(a):
    from game_data import data
    from random import randint
    number = randint(0,len(data)-1)
    while number == a:
        number = randint(0,len(data)-1)
    return data[number]


def comparing(p1,p2):
    if p1 == -1 and p2 == -1:
        people = [pick_data(-1),pick_data(-1)]
    else:
        people=[p1,p2]
    
    print(f"\n\n- {people[0]['name']},{people[0]['description']},{people[0]['country']} has 'higher' or 'lower' follower than:\n")
    print(f"- {people[1]['name']},{people[1]['description']},{people[1]['country']}?")
    #print(f"{people[0]}")
    #print(f"{people[1]}")
    answer = input("\nHigher or Lower?: ").lower()
    
    global score
    if (answer == "lower" and people[0]["follower_count"] < people[1]["follower_count"]) or (answer == "higher" and people[0]["follower_count"] > people[1]["follower_count"]):
        score += 1
        print(f"Your SCORE: {score}\n")
        return comparing(people[1],pick_data(-1))
    else:
        print(f"The game end\n YOUR SCORE: {score}")
        return None
    

print(f"{logo}\nWelcome to my Higher-Lower game ||| Instagram followers edition")
score = 0
comparing(-1, -1)

