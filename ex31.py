import random

print("""You enter a dark room with two doors.
Do you go through door #1,#2, or #3""")

door = input("> ")

if door == "1" or door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print ("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2" or door == "two":
    print("You stare into the endless abyss at Cthulu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == "3" or door == "three":
    print("You've woken up in the falador castle courtyard.")
    print("Time to make a decision...")
    print("1. Regear and teleport back to the wilderness to face f3w.")
    print("2. Sell your pk tab.")
    
    fight_or_resign = input("> ")

    if fight_or_resign == "1" or fight_or_resign == "one":
        print("You teleport and f3w stands before you.")
        print("You both unsheath your godswords...")
        print("Both swords glow with special energy!")
        f3w = 99
        you = 99
        x = random.randint(0,81)
        you = you - x
        y = random.randint(0,81)
        f3w = 99 - y
        print(f"F3w specs you for {x} damage leaving you at {you} hp.")
        print(f"You spec f3w for {y} damage, he has {f3w} hp.")
        print(f"F3w looks at your salad robes, scoffs and raises his sword...")
        print("_______________")
        print("Quick!")
        print("1. Run?")
        print("2. AGS spec again?")
        print("3. Gmaul instant spec and pray?")

        fight_or_flight = input("> ")
        if fight_or_flight == "1" or fight_or_flight == "one": #Run
            x = random.randint(0,81)
            you = you - x
            if you <= 0:
                x = x + you
                print(f" F3w hits a freeze and specs you for {x} as you try to run past.")
                print("Few: A q p")
                print("Few:    w")
            else:
                print(f"F3w splashes a freeze.")
                print(f"With {you} hp, you seed pod and say \"ez\".")
        elif fight_or_flight == "2" or fight_or_flight == "two": #Fight
            pid_f3w = random.randint(0,100)
            pid_you = random.randint(0,100)
            while f3w > 0 and you > 0:
                print("______________")
                if pid_f3w > pid_you:
                    x = random.randint(0,81)
                    you = you - x
                    if you <= 0:
                        x = x + you
                        print(f"F3w specs you for {x}.")
                        print("oh dear, you're dead.")
                        print("F3w: sit.")
                    else:
                        print(f"F3w hits you for {x}.")
                        print(f"You live with {you} hp")
                        gloat = input("You: ")
                        y = random.randint(0,81)
                        f3w = f3w - y
                        if f3w <= 0:
                            y = y + f3w
                            print(f"You spec f3w for {y}, slaying him.")
                            input("You: ")
                            print("You grab the loot key from his corpse.")
                            if y >= 50:
                                print("You smited his AGS. 11.5m pk")
                            else:
                                print("The loot key contains a spade")
                        else:
                            print(f"You spec a {y}.")
                            print(f"F3w survives with {f3w} hp.")
                else:
                    y = random.randint(0,81)
                    f3w = f3w - y
                    if f3w <= 0:
                        y = y + f3w
                        print(f"You spec f3w for {y}, slaying him.")
                        input("You: ")
                        print("You grab the loot key from his corpse.")
                        if y >= 50:
                            print("You smited his AGS. 11.5m pk")
                        else:
                            print("The loot key contains a spade")
                    else:
                        print(f"You spec a {y}.")
                        print(f"F3w survives with {f3w} hp.")
                        x = random.randint(0,81)
                        you = you - x
                        print(f"F3w specs you for {x}.")
                        if you <= 0:
                            print("oh dear, you're dead.")
                            print("F3w: sit.")
        elif fight_or_flight == "3" or fight_or_flight == "three": #Pray
            y = random.randint(0,51)
            print(f"You swap out the Gmaul hitting an instant {y}.")
            f3w = f3w - y
            if f3w <= 0:
                y = y + f3w
                print("Gthunk~ sweet granite justice!")
                print("F3w: RNG..")
                input("You: ")
                print("You grab the loot key from his corpse.")
                if y >= 50:
                    print("You smited his AGS. 11.5m pk")
                else:
                    print("The loot key contains a spade") 
            else:
                print("F3w: ??????")
                print(f"F3w AGS smack to gmaul combos you for {you}.")
                print("...")
                print("...")
                print("...you wake up in the Falador Castle courtyard with nothing.")
                input("You: ")
                print("You got smited.")
    else:
        print("You sell your pking gear and begin fletching everyday, afraid to leave the GE.")
        print("While wearing a black elegant top.")
        print("Congratulations! You've reached 200m experience in fletching!")
        input("You:")
        print("F3w: grats cuck.")

else:
    print("You stumble around and fall on a knife and die. Good job!")