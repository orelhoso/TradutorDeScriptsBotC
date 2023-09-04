import re
f = open("ptbr/all.json", encoding="utf-8")
todos = f.read()
f.close()
noite1 = ["Travellers",
		"Philosopher",
		"Alchemist",
		"Poppy Grower",
		"Magician",
		"MINION",
		"Snitch",
		"Lunatic",
		"DEMON",
		"King",
		"Sailor",
		"Marionette",
		"Engineer",
		"Preacher",
		"Lil Monsta",
		"Lleech",
		"Poisoner",
		"Widow",
		"Courtier",
		"Snake Charmer",
		"Godfather",
		"Devils Advocate",
		"Evil Twin",
		"Witch",
		"Cerenovus",
		"Fearmonger",
		"Harpy",
		"Mezepheles",
		"Pukka",
		"Pixie",		
		"Huntsman",
		"Damsel",
		"Amnesiac",
		"Washerwoman",
		"Librarian",
		"Investigator",
		"Chef",
		"Empath",
		"Fortune Teller",
		"Butler",
		"Grandmother",
		"Clockmaker",
		"Dreamer",
		"Seamstress",
		"Steward",
		"Knight",
		"Noble",
		"Balloonist",
		"Bounty Hunter",
		"Nightwatchman",
		"Cult Leader",
		"Spy",
		"High Priestess",
		"General",
		"Chambermaid",
		"Mathematician",
		"DAWN",
		"Leviathan",
		"Vizier"]
noites = ["Travellers",
		"Philosopher",		
		"Poppy Grower",
		"Sailor",
		"Engineer",
		"Preacher",
		"Poisoner",
		"Courtier",
		"Innkeeper",
		"Gambler",
		"Snake Charmer",
		"Monk",
		"Devils Advocate",
		"Witch",
		"Cerenovus",
		"Pit-Hag",
		"Fearmonger",
		"Harpy",
		"Mezepheles",
		"Scarlet Woman",
		"Lunatic",
		"Exorcist",
		"Lycanthrope",
		"Legion",
		"Imp",
		"Zombuul",
		"Pukka",
		"Shabaloth",
		"Po",
		"Fang Gu",
		"No Dashii",
		"Vortox",
		"Vigormortis",
		"Al-Hadikhia",
		"Lleech",
		"Lil Monsta",
		"Assassin",
		"Godfather",
		"Gossip",
		"Acrobat",
		"Barber",
		"Sweetheart",		
		"Sage",
		"Professor",
		"Choirboy",
		"Huntsman",
		"Damsel",		
		"Amnesiac",
		"Farmer",
		"Tinker",
		"Moonchild",
		"Grandmother",
		"Ravenkeeper",
		"Empath",
		"Fortune Teller",
		"Undertaker",
		"Dreamer",
		"Flowergirl",
		"Town Crier",
		"Oracle",
		"Seamstress",
		"Juggler",
		"Balloonist",
		"King",
		"Bounty Hunter",
		"Nightwatchman",
		"Cult Leader",
		"Butler",
		"Spy",
		"High Priestess",
		"General",
		"Chambermaid",
		"Mathematician",
		"DAWN",
		"Leviathan"]
i = 0
for role in noite1:
	i += 1
	idrole = todos.find('"id": "'+ role.lower().replace(" ", "_")+"_br")
	idnoite1 = todos.find('"firstNight": ', idrole)
	if idrole != -1:
		novonumero = str(i)
		if i < 10: novonumero = " "+novonumero
		todos = todos[:idnoite1+14] + novonumero + todos[idnoite1+16:]
i = 0
for role in noites:
	i += 1
	idrole = todos.find('"id": "'+ role.lower().replace(" ", "_")+"_br")
	idnoites = todos.find('"otherNight": ', idrole)
	if idrole != -1:
		novonumero = str(i)
		if i < 10: novonumero = " "+novonumero
		todos = todos[:idnoites+14] + novonumero + todos[idnoites+16:]
f = open("ptbr/all.json", "w", encoding="utf-8")
f.write(todos)
f.close()


