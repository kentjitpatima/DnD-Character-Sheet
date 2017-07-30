BARBARIAN = {
"Description" : "A fierce warrior of primitive background who can enter a BATTLE RAGE",
"Hit Die" : "Hit Points at 1st level : 12 + Constitution modifier",
"Primary Ability" : "Primary Ability: Strength",
"Saving Throw" : "Saving Throw: Strength and Constitution ",
"Proficiencies" : "Proficiencies: Light and medium armor, shields, simple and martial weapons",
"Skills" : "Skills: Choose two from Animal Handling, Atletics, Intimidation, Nature, Perception, and Survival."
,
}

BARD = {
"Description" : "An inspring magician whose power echoes the music of creation",
"Hit Die" : "Hit Points at 1st Level: 8 + your Constitution modifier",
"Primary Ability" : "Primary Ability: Charisma",
"Saving Throw" : "Saving Throw: Dexeterity and Charisma for SAVING THROW",
"Proficiencies" : "Proficiencies: Light armor, simple weapons, hand crossbows, long swords, rapiers, shortswords, and three musical instruments or your choice",
"Skills" : "Skills: Choose any three"
}

CLERIC = {
"Description" : "A priestly champion who wields divine magic in service of a higher power",
"Hit Die" : "Hit Points at 1st Level: 8 + your Constitution modifier",
"Primary Ability" : "Primary Ability: Wisdom",
"Saving Throw" : "Saving Throws: Wisdom and Charisma",
"Proficiencies" : "Proficiencies: Light armor, simple weapons",
"Skills" : "Skills: Choose two from History, Insight, Medicine, Persuasion, and Religion"
}

DRUID = {
"Description" : "A priest of the Old Faith, wielding the powers of nature moonlight and plant growth, fire and lightning and adopting animal forms",
"Hit Die" : "Hit Points at 1st Level: 8 + your Constitution modifier",
"Primary Ability" : "Primary Ability: Wisdom",
"Saving Throw" : "Saving Throws: Wisdom and Intelligence",
"Proficiencies" : "Proficiencies: Light and medium armor(non-metal), shields(non-metal), clubs, daggers, darts, javelins, maces, quarterstaffs, scimitars, sickles, slings, spears, and Herbalism kits",
"Skills" : "Skills: Choose two from Arcana, Animal Handling, Insight, Medicine, Nature, Perception, Religion, and Survival"
}
# do fighting styles later on also
FIGHTER = {
"Description" : "A master of martial combat, skilled with a variety of weapons and armor",
"Hit Die" : "Hit Points at 1st Level: 10 + your Constitution modifier",
"Primary Ability" : "Primary Ability: STRENGTH or DEXETERITY",
"Saving Throw" : "Saving Throw: Strength and Constitution",
"Proficiencies" : "All armor, shields, simple and martial weapons",
"Skills" : "Choose two skills from Acrobatics, Animal Handling, Athletics, History, Insight, Intimidation, Perception, and Survival"

}

PALADIN = {
"Description" : "A holy warrior bound to a sacred oath",
"Hit Die" : "Hit Points at 1st Level: 10 + your Constitution modifier",
"Primary Ability" : "Primary Ability: STRENGTH or CHARISMA",
"Saving Throw" : "Saving Throw: WISDOM and CHARISMA",
"Proficiencies" : "Proficiencies: All armor, shields, simple and martial weapons",
"Skills" : "Skills: Choose two from Athletics, Insight, Intimidation, Medicine, Persuasion, and Religion"
}

RANGER = {
"Description" : "A warrior who uses martial prowess and nature magic to combat threats on the edges of civilization",
"Hit Die" : "Hit points AT 1st level: 10 + your Constitution modifier",
"Primary Ability" : "Primary Ability: DEXETERITY and WISDOM",
"Saving Throw" : "Saving Throw: STRENGTH and CONSTITUTION",
"Proficiencies" : "Proficiencies: All armor, shields, simple and martial weapons",
"Skills" : "Skills: Choose three from Animal Handling, Athletics, Insight, Investigation, Nature, Perception, Stealth, and Survival"
}

ROGUE = {
"Description" : "A scoundrel who uses stealth andtrickery to overcome obstacles and enemies",
"Hit Die" : "Hit points AT 1st level: 8 + your Constitution modifier",
"Primary Ability" : "Primary Ability: DEXETERITY",
"Saving Throw" : "Saving Throw: DEXETERITY and INTELLIGENCE",
"Proficiencies" : "Proficiencies: Light armor, simple weapons, handcrossbows, longswords, rapiers, shortswords",
"Skills" : "Skills: Choose four from Acrobatics, Athletics, Deception, Insight, Intimidation, Investigation, Perception, Performance. Persuasion, Sleight of Hand, and Stealth"
}

player_class= []


print "In addition to your race you may choose your class in DND. Each class has its own unqiue skillsets and moves!"
print "You may choose to be a Barbarian, Bard, Cleric, Druid, Fighter, Paladin, Ranger, or Rogue."
print "\n" + "If you wish to see more information of the classes, add a (?) to the end of the background. For example, \'Barbarian?\'" + "\n"

def choose_class():
    class_input = raw_input("Choose a class: ").upper()
    if class_input == "BARBARIAN?" or class_input == "FIGHTER?" or class_input == "PALADIN?" or class_input == "RANGER?" or class_input == "ROGUE?" or class_input == "BARD?" or class_input == "CLERIC?" or class_input == "DRUID?":
        z = class_input.replace("?","")
        print z
        print (eval(z)["Description"]) + '\n' + (eval(z)["Hit Die"]) + '\n' + (eval(z)["Primary Ability"]) + '\n' + (eval(z)["Saving Throw"]) + '\n' + (eval(z)["Proficiencies"])+'\n' + (eval(z)["Skills"]) + '\n'
        choose_class()
    elif class_input == "BARBARIAN" or class_input == "FIGHTER" or class_input == "PALADIN" or class_input == "RANGER" or class_input == "ROGUE" or class_input == "BARD" or class_input == "CLERIC" or class_input == "DRUID" :
        player_class.append(class_input)
        print "\n\nSo you have decided %s to be your background!\n\n" % player_class[0]
    else:
        print "Invalid input try again!"
        choose_class()
choose_class()
