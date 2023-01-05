#in inches [length, depth]
desk_colin = [40, 29.5]

credenza = [47.5, 16]

desk_anna = [46.5, 24]

display_case = [16.5, 14.5]

pc_colin = [8.5, 17]

file_case = [12, 13]

west_window = 59 #35 in from south wall

south_window = 59 #6.5 in from east wall

room = [122, 130] #first measure is closet to wall

room_entry = [28, 45] # [e/w, n/s]

def room_area(length, width):
    length = length / 12 #in feet
    width = width / 12 #in feet
    area = length * width
    print(f"The area of the room is {round(area, 2)} square feet.")
    return area

room_area(room[0], room[1])