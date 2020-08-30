# Additionally add to chosen dictionary for brute force attacks
import sys

toolbar_width = 40

# setup a toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

BoldText = '\033[1m'
RedTextColor = '\033[31m'
GreenTextColor = '\033[32m'
YellowTextColor = '\033[33m'
ResetColor = '\033[m'

print(YellowTextColor + BoldText + "  ____   _____   ____")
print(" / ___| |_   _| |  _ \\")
print("| |  _    | |   | |_) |")
print("| |_| |   | |   |  __/")
print(" \\____|   |_|   |_|\n" + ResetColor)
print("WELCOME TO GUESS THE PASS\n")
print("Author: " + GreenTextColor + "Ahmadreza Vakil" + ResetColor)

print(RedTextColor + "\nNOTE THAT THIS SCRIPT IS ONLY MADE FOR EDUCATIONAL PURPOSES!"
                     "\nDO NOT USE THIS SCRIPT FOR NASTY PURPOSES.\n"
                     "DON'T FORGET TO GIVE ME CREDIT!\n" + ResetColor)

print("Now I ask you some questions to guess all possible password that is easy for the victim to remember. "
      "Simply press ENTER to skip a question if:\n"
      "- Don't know the answer...\n"
      "- Is inappropriate or not relevant\n"
      "\n"
      "NOTE! Less input is equal to shorter length of the guessed password.")

fileName = input("Enter the dictionary name to create:\n")
if fileName == "" or fileName == " ":
    fileName = "dictionary"


def build(list, w, i, length):
    f = open(fileName + ".txt", "a")
    if w == 0:
        # print(i)
        f.write(i+"\n")
        return
    for j in range(0, length):
        concatenate = i + list[j]
        build(list, w - 1, concatenate, length)
    return


def conjecture(list, length):
    print("\nPlease wait...")
    for w in range(1, length + 1):
        build(list, w, "", length)
        sys.stdout.write(".")
        sys.stdout.flush()
    sys.stdout.write("\nDone!\nDictionary is created!\n") # this ends the progress bar


def validator(answer):
    if answer == 'Y' or answer == 'y' or answer == 'yes' or answer == 'YES' or answer == 'Yes':
        return True
    else:
        return False


print("QUESTIONS ABOUT THE VICTIM...\n")
questions = ['Victim name:', 'Victim endearment name:', 'Victim family name:', 'Victim birth year:',
             'Victim birth month:', 'Victim birth day:']

HasPet = input("Does the victim has pet?(Y/N)\n")
if validator(HasPet):
    questions.extend(['Victim pet name:'])

HasPartner = input("Does the victim has partner or spouse?(Y/N)\n")
if validator(HasPartner):
    questions.extend(['Victim partner or spouse name:', 'Victim partner endearment name', 'Victim endearment name?'
                      'Victim partner birth month:', 'Victim partner birth day:'])

raw_details = []
for question in questions:
    raw_details.append(input(question+"\n"))

details = []
for value in raw_details:
    if value != "":
        details.append(value)

length = len(details)
conjecture(details, length)
