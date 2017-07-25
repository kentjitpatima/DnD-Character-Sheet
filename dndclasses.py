"""This is our dictionary inputs for character melee charcter classes of Barbarian, Fighter, Paladin, Ranger, Rogue."""

print "In addition to your race you may choose your class in DND. Each class has its own unqiue skillsets and moves!"
print "Here are some melee classes in DND!"
print
print
print

BARBARIAN = {"Description" : "A fierce warrior of primitive background who can enter a BATTLE RAGE",
"Hit Die" : "Uses a -d12- per lvl for HIT DIE",
1 : "Uses primarily STRENGTH",
"Saving Throw" : "Strength and Constitution for SAVING THROW",
"PROFICIENCIES" : "Light and medium armor, shields,simple and martial weapons",
}
FIGHTER = {"Description" : "A master of martial combat, skilled with a variety of weapons and armor",
"Hit Die" : "Uses a -d10- per lvl for HIT DIE",
"Primary Ability" : "Uses primarily STRENGTH or DEXETERITY",
"Saving Throw" : "Strength and Constitution for SAVING THROW",
"PROFICIENCIES" : "All armor, shields, simple and martial weapons",
}

PALADIN = {"Description" : "A holy warrior bound to a sacred oath",
"Hit Die" : "Uses a -d10-per level for HIT DIE",
"Primary Ability" : "Uses primarily STRENGTH and CHARISMA",
"Saving Throw" : "WISDOM and CHARISMA for SAVING THROW",
"PROFICIENCIES" : "All armor, shields, simple and martial weapons",
}

RANGER = {"Description" : "A warrior who uses martial prowess andnature magic to combat threats on the edges of civilization",
"Hit Die" : "Uses a -d10-per level for HIT DIE",
"Primary Ability" : "Uses primarily DEXETERITY and WISDOM",
"Saving Throw" : "Strength and Constitution for SAVING THROW",
"PROFICIENCIES" : "All armor, shields, simple and martial weapons",
}

ROGUE = {"Description" : " A scoundrel who uses stealth andtrickery to overcome obstacles and enemies",
"Hit Die" : "Uses a -d8- for HIT DIE",
"Primary Ability" : "Uses primarily DEXETERITY",
"Saving Throw" : "Strength and Constitution for DEXETERITY and INTELLIGENCE",
"PROFICIENCIES" : "Light armor, simple weapons, handcrossbows, longswords, rapiers, shortswords"
}

print "BARBARIAN: "
print BARBARIAN["Description"]
print BARBARIAN["Hit Die"]
print BARBARIAN[1]
print BARBARIAN["Saving Throw"]
print BARBARIAN["PROFICIENCIES"]
print
print

print "FIGHTER: "
print FIGHTER["Description"]
print FIGHTER["Hit Die"]
print FIGHTER["Primary Ability"]
print FIGHTER["Saving Throw"]
print FIGHTER["PROFICIENCIES"]
print
print

print "PALADIN: "
print PALADIN["Description"]
print PALADIN["Hit Die"]
print PALADIN["Primary Ability"]
print PALADIN["Saving Throw"]
print PALADIN["PROFICIENCIES"]
print
print

print "RANGER: "
print RANGER["Description"]
print RANGER["Hit Die"]
print RANGER["Primary Ability"]
print RANGER["Saving Throw"]
print RANGER["PROFICIENCIES"]
print
print

print "ROGUE: "
print ROGUE["Description"]
print ROGUE["Hit Die"]
print ROGUE["Primary Ability"]
print ROGUE["Saving Throw"]
print ROGUE["PROFICIENCIES"]
print
print



player_class = []

def choose_class():
    class_input = raw_input("Would you like to be a BARBARIAN, FIGHTER, PALADIN, RANGER, ROGUE?: ").upper()
    if class_input == "BARBARIAN" or class_input == "FIGHTER" or class_input  =="PALADIN" or class_input =="RANGER" or class_input =="ROGUE":
        player_class.append(class_input)
        print "You have chosen to be a %s!" % player_class[0]

    else:
        print "That is not a valid class, try again!"
        choose_class()
choose_class()

dick = raw_input("Enter any key to end ")
