from sys import argv #argv holds the arguments you pass to your script
#argument variable

script, user_name = argv #this argv is holding two arguments
prompt = '> '

#arguments held in following f strings will be filled by argv
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt) #input calls prompt var to add flavor to request for input

print(f"Where do you live {user_name}?")
lives = input(prompt) # variable is filled by user input

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""") #prints multiline string with variables filled by prev input