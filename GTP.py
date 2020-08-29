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
      "- Is inappropriate or not relevant\n")

print("QUESTIONS ABOUT THE VICTIM\n")
Name = input("Please enter the victim name:\n")
FamilyName = input("Please enter the victim family name:\n")
BirthYear = input("Please enter the victim birth year:\n")
BirthMonth = input("Please enter the victim birth month:\n")
BirthDay = input("Please enter the victim birth day:\n")

HasPet = input("Does the victim has pet?(Y/N)\n")
#if
PetName = input("Please enter the victim pet name:\n")

HasPartner = input("Does the victim has partner or spouse?(Y/N)\n")
#if
PartnerName = input("Please enter the victim's partner or spouse name:\n")
PartnerBirthYear = input("Please enter the victim partner birth year:\n")
PartnerBirthMonth = input("Please enter the victim partner birth month:\n")
PartnerBirthDay = input("Please enter the victim partner birth day:\n")

