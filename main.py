import re

infile = open("fiveLetters.txt", "r")

#potential letters for each spot
potentialLetters = input("Enter potential letters: ")

#create regex for any letter
anyPattern = "["
for letter in potentialLetters:
    anyPattern += letter.upper()
     
anyPattern += "]"

pattern = "" #overall regex pattern
#construct the overall pattern
for i in range(5):
    userInput = input("Enter the letter in position " + str(i) + ", or use * for any of the potential letters: ")
    if(len(userInput) != 1):
        print("Please enter only one character.")
    else:
        if(userInput == "*"):
            pattern += anyPattern
        else:
            pattern += userInput.upper()

print("Pattern is: " + pattern)

#loop over the words in dictionary to see if there is a match
for word in infile:
    if re.match(pattern, word.upper()):
        print(word, end="")

