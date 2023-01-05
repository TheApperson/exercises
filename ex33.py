i = 0
players_pked = (6, 2)
pks = []

def keys(kills, minutes): 
    i = 0
    while i < kills:
        print(f"At the top i is {i}")
        pks.append(i)
        i = i + minutes
        print("Numbers now: ", pks)
        print(f"At the bottom i is {i}")

print(keys(players_pked[0], players_pked[1]))
print("The numbers: ")
