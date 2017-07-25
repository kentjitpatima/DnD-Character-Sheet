BARBARIAN = {
"Description" : "A fierce warrior of primitive background who can enter a BATTLE RAGE",
"Hit Die" : "Uses a -d12- per lvl for HIT DIE",
"Primary Ability" : "Uses primarily STRENGTH",
"Saving Throw" : "Strength and Constitution for SAVING THROW",
"PROFICIENCIES" : "Light and medium armor, shields,simple and martial weapons",
}
FIGHTER = {
"Description" : "A master of martial combat, skilled with a variety of weapons and armor",
"Hit Die" : "Uses a -d10- per lvl for HIT DIE",
"Primary Ability" : "Uses primarily STRENGTH or DEXETERITY",
"Saving Throw" : "Strength and Constitution for SAVING THROW",
"PROFICIENCIES" : "All armor, shields, simple and martial weapons",
}

PALADIN = {
"Description" : "A holy warrior bound to a sacred oath",
"Hit Die" : "Uses a -d10-per level for HIT DIE",
"Primary Ability" : "Uses primarily STRENGTH and CHARISMA",
"Saving Throw" : "WISDOM and CHARISMA for SAVING THROW",
"PROFICIENCIES" : "All armor, shields, simple and martial weapons",
}

RANGER = {
"Description" : "A warrior who uses martial prowess and nature magic to combat threats on the edges of civilization",
"Hit Die" : "Uses a -d10-per level for HIT DIE",
"Primary Ability" : "Uses primarily DEXETERITY and WISDOM",
"Saving Throw" : "Strength and Constitution for SAVING THROW",
"PROFICIENCIES" : "All armor, shields, simple and martial weapons",
}

ROGUE = {
"Description" : "A scoundrel who uses stealth andtrickery to overcome obstacles and enemies",
"Hit Die" : "Uses a -d8- per lvl for HIT DIE",
"Primary Ability" : "Uses primarily DEXETERITY",
"Saving Throw" : "Saving throw with DEXETERITY and INTELLIGENCE",
"PROFICIENCIES" : "Light armor, simple weapons, handcrossbows, longswords, rapiers, shortswords"
}

player_class= []


print "In addition to your race you may choose your class in DND. Each class has its own unqiue skillsets and moves!"
print "\n" + "If you wish to see more information of the classes, add a (?) to the end of the background. For example, \'Barbarian?\'" + "\n"

def choose_class():
    class_input = raw_input("Choose a class: ").upper()
    if class_input == "BARBARIAN?" or class_input == "FIGHTER?" or class_input == "PALADIN?" or class_input == "RANGER?" or class_input == "ROGUE?":
        z = class_input.replace("?","")
        print z + " : "
        print (eval(z)["Description"]) + '\n' + (eval(z)["Hit Die"]) + '\n' + (eval(z)["Primary Ability"]) + '\n' + (eval(z)["Saving Throw"]) + '\n' + (eval(z)["PROFICIENCIES"]) + '\n'
        choose_class()
    elif class_input == "BARBARIAN" or class_input == "FIGHTER" or class_input == "PALADIN" or class_input == "RANGER" or class_input == "ROGUE":
        player_class.append(class_input)
        print "\n\nSo you have decided %s to be your background!\n\n" % player_class[0]
    else:
        print "Invalid input try again! "
        choose_class()
choose_class()
