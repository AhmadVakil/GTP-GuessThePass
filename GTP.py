# Get as much as info as possible
# Save to txt file
# Additionally add to chosen dictionary for brute force attacks

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

print(RedTextColor + "NOTE THAT THIS SCRIPT IS ONLY MADE FOR EDUCATIONAL PURPOSES!"
                     "\nDO NOT USE THIS SCRIPT FOR NASTY PURPOSES.\n"
                     "DON'T FORGET TO GIVE ME CREDIT!\n" + ResetColor)

print("Now I ask you many questions to guess all possible password that is easy for the victim to remember. "
      "Simply press ENTER to skip a question if:\n"
      "- Don't know the answer...\n"
      "- Is inappropriate or not relevant\n"
      "\n"
      "NOTE!")


def build(list, w, i, length):
    if w == 0:
        print(i)
        return
    for j in range(0, length):
        concatenate = i + list[j]
        build(list, w - 1, concatenate, length)
    return


def conjecture(list, length):
    for w in range(1, length + 1):
        build(list, w, "", length)


def validator(answer):
    if answer == 'Y' or answer == 'y' or answer == 'yes' or answer == 'YES' or answer == 'Yes':
        return True
    else:
        return False


details = []
print("QUESTIONS ABOUT THE VICTIM...\n")
details.append(input("Victim name:\n"))
details.append(input("Victim endearment name?\n"))
details.append(input("Victim family name:\n"))
details.append(input("Victim birth year:\n"))
details.append(input("Victim birth month:\n"))
details.append(input("Victim birth day:\n"))

HasPet = input("Does the victim has pet?(Y/N)\n")
if validator(HasPet):
    details.append(input(" the victim pet name:\n"))

HasPartner = input("Does the victim has partner or spouse?(Y/N)\n")
if validator(HasPartner):
    details.append(input("Victim partner or spouse name:\n"))
    details.append(input("Victim endearment name?"))
    details.append(input("Victim partner birth year:\n"))
    details.append(input("Victim partner birth month:\n"))
    details.append(input("Victim partner birth day:\n"))

for value in details:
    if value == "":
        print("Skipped")
    else:
        print(value)

length = len(details)
conjecture(details, length)
