from sys import argv #imported argument variable module from system

script, filename = argv#arguments for argv(2 args must be added in terminal)

txt = open(filename) #var txt is command open with the filename argument
#since the argument is a document, it will open when txt is called

print(f"Here's your file {filename}:") #format string
print(txt.read())# function call on txt to read 

print("Type the filename again:")
file_again = input("> ") # using input instead of argv which is better?

txt_again = open(file_again)

print(txt_again.read())

txt_again.close()
txt.close() #closing open files

txt.read() #error! closed files can not be read