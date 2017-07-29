#Race Dictionary
#LAST UPDATED 7/25/2017 by Ryan Luu
#CHANGELOG : Added line 96 - end.
#Needs fixing : When recalling player_race_bonus, you see the \n's in the summary.  Might need to recode the whole thing and make separate dictionaries for each race. 




race_dictionary = {

    "dwarf_info" : "\nAbility Score Increase: Constitution +2. \nSize: Dwarves stand between 4 and 5 feet tall and average about 150 pounds. Your size is medium. \nSpeed: Your base walking speed is 25 feet. Your speed is not reduced by wearing heavy armour. \nPassives: Dark Vision -  You can see in dim light within 60 feet of you as if it were bright light. You can't discern color in darkness, only shades of grey. \nDwarven Resilience - You have advantage on saving throws against poison, and you have resistance against posion damage. \nDwarven Combat Training - You have proficiency with the battleaxe, handaxe, throwing hammer, and warhammer. \nLanguage - You can speak, read, and write Common and Dwarvish.\n " ,

    "elf_info" : "\nAbility Score Increase: Dexterity + 2. \nSize: Elves rnage from under 5 to over 6 feet tall and ahve slender builds. Your size is Medium. \nSpeed. Your base walking speed is 30 feet. \nPassives: Dark Vision - You can see in dim light wihtin 60 feet of you as if it were bright light. You can't descern color in darkness, only shades of gray. \nKeen Senses - You have proficiency in the Perception Skill. \nFey Ancestry - You have advantage on saving throws against being charmed, and magic can't put you to sleep. \nTrance - Elves don't need to sleep. Instead, they meditate deeply for 4 hours. It is the equivalent of 8 hours of rest. \nLanguage- You can speak, read, and write Common and Elvish. \n " ,

    "halfling_info" : "\nAbility Score Increase: Dexterity + 2. \nSize: Halflings average about 3 feet tall and weigh about 40 pounds . Your size is Small. Speed: Your base walking speed is 25 feet. Passives: Lucky - When you roll a 1 on an attack roll, ability check, or saving throw, you can reroll the die and must use the new roll. Brave - You have advantage on saving throws against being frightened. Halfling Nimble - You can move through the space of any creature that is a size larger than yours. Languages - You can speak, read, and write Common and Halfling. \n" ,

    "human_info" : "\nAbility Score Increase: All Stats + 1. \nSize: Humans vary widely in height and build from barely 5 feet to well over 6 feet tall. Regardless of your position in that range, your size is Medium. \nSpeed: Your base walking speed is 30 feet. \nLanguages: You can speak read, and write Common and one extra language of your choice. \n" ,

    "dragonborn_info" : "\nAbility Score Increase: Strenght +2. \nSize: Dragonborn are taller and heavier than humans, standing well over 6 feet tall and averaging almost 250 pounds. \nSpeed: Your base walking speed is 30 feet. \nPassives: Dragonic Ancestry - Choose one type of dragon from Draconic Ancestry table. Your breath weapon and damage resistance are determined by your dragon type. \nDamage Resistance - You have resistance to the damage type associated with your draconic ancestry. \nLanguages - You can, read, and write Common and Draconic. \n",

    "gnome_info" : "\nAbility Score Increase: Your intelligence score increases by 2. \nSize: Gnomes are between 3 and 4 feet tall and average about 40 pounds. Your size is Small. Speed: Your base walking speed is 25 feet. \nPassives: Dark Vision - You cna see in dim light within 60 feet of you as if it were bright light. You can't discern color in darkness, only shades of gray. \nGnome Cunning - You have advantage on all Intelligence, Wisdom, and Charism saving throws against magic.\nLanguage - You can speak, read, and wrtie Common and Gnomish.\n ",

    "half-elf_info" : "\nAbility Score Increase: Charsima +2. Two other ability scores of your choice increase by 1. \nSize: Half-Elves are about the same size as humans, ranging form 5 to 6 feet tall. Your size is Medium. Speed: Your base walking speed is 30 feet. \nPassives: Darkvision - You can see in dim light within 60 feet of you as if it were bright light. \nFey Ancestry - You have advantage on saving throws against being charmed, and magic can't put you to sleep. \nSkill Versatility - You gain proficiency in two skills of your choice. \nLanguage - You can speak, read, and write, Common, Elvish, and one extra language of your choice. \n" ,

    "half-orc_info" : "\nAbility Score Increase: Strength + 2 and Constitution + 1. \nSize: Half-orcs are somewhat larger and bulkier than humans, and they range from 5 to well over 6 feet tall. Your size is Medium. \nSpeed: Your base walking speed is 30 feet. \nPassives: Dark Vision - You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray. \nMenacing - You gain proficiency in Intimidation Skill. \nRelentless Endurance - When you are reduced to 0 hp, you drop to 1 hp instead. You can't use this feature until a long rest. \nSavage Attack - If critical hit with melee weapon, roll weapon dice one additional time and addon to damage. \nLanguage - You can speak, read, and write Common and Orc. \n" ,

    "tiefling_info" : "\nAbility Score Increase: Intelligence +1, Charisma + 2. \nSize: Tieflings are about the same size and build as humans. Your size is Medium. \nSpeed: your base walking speed is 30 feet. \nPassives: Darkvision - You can see in dim light within 60 feet of you as if it were bright light. You can't discern color in darkness, only shades of gray. \nHellish Resistance - You have resistance to fire damage. Languages - You can speak, read, and write Common and Infernal. \n"

}

player_race = []
player_race_bonus = []


print "There are many races in the world of DnD. The race you select will alter your character's stats. \n\nRace: \nDwarf \nElf\nHalfling \nHuman \nDragonborn \nGnome\nHalf-Elf\nHalf-Orc\nTiefling\n \nIf you wish to request information from a particular class, add a ? to the end of the race. \nExamples: human? "

def character_race():
    race_input = raw_input("\nWhich race would you like to select?  ").lower()
    if race_input == "dwarf" or race_input == "elf" or race_input == "halfling" or race_input == "human" or race_input == "dragonborn" or race_input == "gnome" or race_input == "half-elf" or race_input == "half-orc" or race_input == "tiefling":
        player_race.append(race_input)
        player_race[0] = player_race[0].upper()
        print "\nYou are a %s!!!!" % player_race

        def player_bonus():
            if race_input == "dwarf":
                player_race_bonus.append(race_dictionary["dwarf_info"])
            elif race_input == "elf":
                player_race_bonus.append(race_dictionary["elf_info"])
            elif race_input == "halfling":
                player_race_bonus.append(race_dictionary["halfling_info"])
            elif race_input == "human":
                player_race_bonus.append(race_dictionary["human_info"])
            elif race_input == "dragonborn":
                player_race_bonus.append(race_dictionary["dragonborn_info"])
            elif race_input == "gnome":
                player_race_bonus.append(race_dictionary["gnome_info"])
            elif race_input == "half elf" or race_input == "half-elf":
                player_race_bonus.append(race_dictionary["half-elf_info"])
            elif race_input == "half orc" or race_input == "half-orc":
                player_race_bonus.append(race_dictionary["half-orc_info"])
            elif race_input == "tiefling":
                player_race_bonus.append(race_dictionary["tiefling_info"])
        player_bonus()

    elif race_input == "dwarf?":
        print race_dictionary["dwarf_info"]
        character_race()
    elif race_input == "elf?":
        print race_dictionary["elf_info"]
        character_race()
    elif race_input == "halfling?":
        print race_dictionary["halfling_info"]
        character_race()
    elif race_input == "human?":
        print race_dictionary["human_info"]
        character_race()
    elif race_input == "dragonborn?":
        print race_dictionary["dragonborn_info"]
        character_race()
    elif race_input == "gnome?":
        print race_dictionary["gnome_info"]
        character_race()
    elif race_input == "half-elf?" or race_input == "half elf?":
        print race_dictionary["half-elf_info"]
        character_race()
    elif race_input == "half-orc?" or race_input == "half orc?":
        print race_dictionary["half-orc_info"]
        character_race()
    elif race_input == "tiefling?":
        print race_dictionary["tiefling_info"]
        character_race()
    else:
        print "You didn't pick one of the following races. Please try again. "
        character_race()

character_race()

print "Congragualations, you have selected " + str(player_race) + " as your race. "
print
print "If you ever need to recall your character\'s race bonus, just type \"my race bonus\""
print "Give it a try! "

def see_bonus():
    bonus = raw_input("Type \"my race bonus\" or you can press anything to skip this step. \n\n").lower()
    if bonus == "my race bonus":
        print
        print "Here is your character\'s race bonus: " + str(player_race_bonus)

    else:
        pass
see_bonus()

dick = raw_input("\nPress anything to exit\n")
