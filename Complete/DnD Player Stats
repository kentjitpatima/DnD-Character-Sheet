#Player Stats : Strength, Dexterity, Constitution, Intelligence, Stealth, and Charisma.
# LAST UPDATED : 7/24/17 by Ryan Luu
#############################################################################
rng_choice = []
##############################################################################
player_strength = []
player_dexterity = []
player_constitution = []
player_intelligence = []
player_wisdom = []
player_charisma = []
###############################################################################

import random

###start RNG  Attribute SCore list###########################################################################

stats = [
    sum(sorted(random.randint(1,6) for _ in range (4))[1:])
    for _ in range(7)
]
stats.remove(min(stats))

#end of rng code########################################################################
#start of standard_array list##############################################################

standard_array = [15, 14, 13, 12, 10 , 8]

##end of standard_array code list #################################################################

attribute_dictionary = {
    "strength_info" : "Strength measures natrual athleticism, bodily power. \nIncrease damage for melee weapons. \nImportant for: Barbarian, fighter, paladin.   " ,
    "dexterity_info" : "Dexterity measures physical agility, reflexes, balance, poise. \nIncrease damage for range and finesse weapons. \nImportant for: Monk, ranger, rogue." ,
    "constitution_info" : "Constitution meausures health, stamina, vital force. \nImportant for: Everyone" ,
    "intelligence_info" : "Intelligence measures: Mental acuity, information recall, analytical skill. \nIncrease damage for Wizard spellcasting.\nImportant for: Wizard." ,
    "wisdom_info" : "Wisdom measures awareness, intuition, insight. \nImportant for: Cleric, Druid." ,
    "charisma_info" : "Charisma measures confidence, eloquence, leadership. \nImportant for: Bard, sorcerer, warlock. "
}

##end of attribute dictionary############################################################################
##printing begins here ############################################################################

print "There are six basic attribute: Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma. "

def intro():
    boob = raw_input("Do you need help with how the attributes work? (Y/N)").lower()
    if boob == "n" or boob == "no":
        print
        print

    elif boob == "y" or boob == "yes":
        print
        print attribute_dictionary["strength_info"]
        print
        print attribute_dictionary["dexterity_info"]
        print
        print attribute_dictionary["constitution_info"]
        print
        print attribute_dictionary["intelligence_info"]
        print
        print attribute_dictionary["wisdom_info"]
        print
        print attribute_dictionary["charisma_info"]
        print
        intro()

    else:
        print "Invalid. "
        intro()

intro()

print "You can use the Standard Array method (you will be given 15, 14, 13, 12, 10 , 8 to assign) or we can randomize them. "

def stat_assignment():
    penis = raw_input("\nWould you like your attributes randomized? (Y/N)").lower()
    if penis == "y" or penis == "yes":
        rng_choice.append(penis)
        print "\nYour stats are " + str(stats)

    elif penis == "n" or penis == "no":
        rng_choice.append(penis)
        print "\nThese are your stats: " + str(standard_array)
        print "Now, we will begin assigning your stats."

    else:
        print "Invalid. "
        stat_assignment()

stat_assignment()

#############random array###########################################################################################

def rng_strength():
    if rng_choice == ["y"] or rng_choice == ["yes"]:
        print "\nWhich number would you like to assign to your character\'s strength?"
        x = raw_input("")
        if int(x) == stats[0] or int(x) == stats[1] or int(x) == stats[2] or int(x) == stats[3] or int(x) == stats[4] or int(x) == stats[5]:
            stats.remove(int(x))
            player_strength.append(int(x))

        else:
            print "Try again!"
            rng_strength()

rng_strength()

def rng_dexterity():
    if rng_choice == ["y"] or rng_choice == ["yes"]:
        print "\nYou have 5 attribute scores left. Here are your remaining scores: " + str(stats)
        print "\nWhich number would you like to assign to your character\'s dexterity?"
        x = raw_input("")
        if int(x) == stats[0] or int(x) == stats[1] or int(x) == stats[2] or int(x) == stats[3] or int(x) == stats[4]:
            stats.remove(int(x))
            player_dexterity.append(int(x))

        else:
            print "Try again!"
            rng_dexterity()

rng_dexterity()

def rng_constitution():
    if rng_choice == ["y"] or rng_choice == ["yes"]:
        print "\nYou have 4 attribute scores left. Here are your remaining scores: " + str(stats)
        print "\nWhich number would you like to assign to your character\'s constitution?"
        x = raw_input("")
        if int(x) == stats[0] or int(x) == stats[1] or int(x) == stats[2] or int(x) == stats[3]:
            stats.remove(int(x))
            player_constitution.append(int(x))

        else:
            print "Try again!"
            rng_constitution()

rng_constitution()

def rng_intelligence():
    if rng_choice == ["y"] or rng_choice == ["yes"]:
        print "\nYou have 3 attribute scores left. Here are your remaining scores: " + str(stats)
        print "\nWhich number would you like to assign to your character\'s intelligence?"
        x = raw_input("")
        if int(x) == stats[0] or int(x) == stats[1] or int(x) == stats[2]:
            stats.remove(int(x))
            player_intelligence.append(int(x))

        else:
            print "Try again!"
            rng_intelligence()

rng_intelligence()

def rng_wisdom():
    if rng_choice == ["y"] or rng_choice == ["yes"]:
        print "\nYou have 2 attribute scores left. Here are your remaining scores: " + str(stats)
        print "\nWhich number would you like to assign to your character\'s wisdom?"
        x = raw_input("")
        if int(x) == stats[0] or int(x) == stats[1]:
            stats.remove(int(x))
            player_wisdom.append(int(x))

        else:
            print "Try again!"
            rng_wisdom()

rng_wisdom()

def rng_charisma():
    if rng_choice == ["y"] or rng_choice == ["yes"]:
        player_charisma.append(stats[0])
        print "\nThe remaining attribute score " + str(stats[0]) + " will be assigned to your charisma. "

rng_charisma()

################end of random array#######################################################################

###############start of standard_array####################################################################

def norng_strength():
    if rng_choice == ["n"] or rng_choice == ["no"]:
        print "\nWhich number would you like to assign to your character\'s strength?"
        x = raw_input("")
        if int(x) == standard_array[0] or int(x) == standard_array[1] or int(x) == standard_array[2] or int(x) == standard_array[3] or int(x) == standard_array[4] or int(x) == standard_array[5]:
            standard_array.remove(int(x))
            player_strength.append(int(x))

        else:
            print "Try again!"
            norng_strength()

norng_strength()

def norng_dexterity():
    if rng_choice == ["n"] or rng_choice == ["no"]:
        print "\nYou have 5 attribute scores left. Here are your remaining scores: " + str(standard_array)
        print "\nWhich number would you like to assign to your character\'s dexterity?"
        x = raw_input("")
        if int(x) == standard_array[0] or int(x) == standard_array[1] or int(x) == standard_array[2] or int(x) == standard_array[3] or int(x) == standard_array[4]:
            standard_array.remove(int(x))
            player_dexterity.append(int(x))

        else:
            print "Try again!"
            norng_dexterity()

norng_dexterity()

def norng_constitution():
    if rng_choice == ["n"] or rng_choice == ["no"]:
        print "\nYou have 4 attribute scores left. Here are your remaining scores: " + str(standard_array)
        print "\nWhich number would you like to assign to your character\'s constitution?"
        x = raw_input("")
        if int(x) == standard_array[0] or int(x) == standard_array[1] or int(x) == standard_array[2] or int(x) == standard_array[3]:
            standard_array.remove(int(x))
            player_constitution.append(int(x))

        else:
            print "Try again!"
            norng_constitution()

norng_constitution()

def norng_intelligence():
    if rng_choice == ["n"] or rng_choice == ["no"]:
        print "\nYou have 3 attribute scores left. Here are your remaining scores: " + str(standard_array)
        print "\nWhich number would you like to assign to your character\'s intelligence?"
        x = raw_input("")
        if int(x) == standard_array[0] or int(x) == standard_array[1] or int(x) == standard_array[2]:
            standard_array.remove(int(x))
            player_intelligence.append(int(x))

        else:
            print "Try again!"
            norng_intelligence()

norng_intelligence()

def norng_wisdom():
    if rng_choice == ["n"] or rng_choice == ["no"]:
        print "\nYou have 2 attribute scores left. Here are your remaining scores: " + str(standard_array)
        print "\nWhich number would you like to assign to your character\'s wisdom?"
        x = raw_input("")
        if int(x) == standard_array[0] or int(x) == standard_array[1]:
            standard_array.remove(int(x))
            player_wisdom.append(int(x))

        else:
            print "Try again!"
            norng_wisdom()

norng_wisdom()

def norng_charisma():
    if rng_choice == ["n"] or rng_choice == ["no"]:
        player_charisma.append(standard_array[0])
        print "\nThe remaining attribute score " + str(standard_array[0]) + " will be assigned to your charisma."

norng_charisma()

close = raw_input("\nPress enter to view your character\'s attribute overview.")

##################end of standard_array###########################################################

print "\nThis is a summary of your character\'s attribute."
print "Strength: " + str(player_strength)
print "Dexterity: " + str(player_dexterity)
print "Constitution: " + str(player_constitution)
print "Intelligence: " + str(player_intelligence)
print "Wisdom: " + str(player_wisdom)
print "Charisma: " + str(player_charisma)

titties = raw_input("\nYou have finished your Player Stats Distribution.")
