# Get as much as info as possible
# Keep in array or db
# Iterate and do string concatenation, all possibilities
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

print("QUESTIONS ABOUT THE VICTIM\n")
Name = input(" the victim name:\n")
Endearment = input("Victim endearment name?")
FamilyName = input("Victim family name:\n")
BirthYear = input("Victim birth year:\n")
BirthMonth = input("Victim birth month:\n")
BirthDay = input("Victim birth day:\n")

HasPet = input("Does the victim has pet?(Y/N)\n")
#if
PetName = input(" the victim pet name:\n")

HasPartner = input("Does the victim has partner or spouse?(Y/N)\n")
#if
PartnerName = input("Victim partner or spouse name:\n")
PartnerEndearment = input("Victim endearment name?")
PartnerBirthYear = input("Victim partner birth year:\n")
PartnerBirthMonth = input("Victim partner birth month:\n")
PartnerBirthDay = input("Victim partner birth day:\n")

def build(list, w, l, length):
    if w == 0:
        print(l)
        return
    for j in range(0, length):
        concatenate = l + list[j]
        build(list, w - 1, concatenate, length)
    return


def conjecture(list, length):
    for w in range(1, length + 1):
        build(list, w, "", length)


list = ['george', '25', 'dude']
length = len(list)
conjecture(list, length)
