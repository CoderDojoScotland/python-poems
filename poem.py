import pronouncing
import random

line = "When chapman billies leave the street"
line2 = "And drouthy neibors, neibors meet"
line3 = "As market days are wearing late"
line4 = "An'folk begin to tak the gate"
line5 = "While we sit bousing at the nappy"
line6 = "And gettingfou and unco happy"
line7 = "We think na on the lang scots miles"
line8 = "The mosses, waters, slaps, and styles"
line9 = "That lie between us and our hame"
line10 = "Where sits our sulky sullen dame"
line11 = "Gathering her brows like gathering storm"
line12 = "Nursing her wrath to keep it warm"
line13 = "This truth fand honest Tam o' Shanter"
line14 = "As he frae Ayr ae night did canter"
line15 = "Auld Ayr, Wham ne'er a town surpasses"
line16 = "For honest men and bonie lasses"
line17 = "O Tam! had'st thou but been sae wise,"
line18 = "As ta'em thy ain wife Kate's advice!"
line19 = "She tauld thee weel thou was a skellum"
line20 = "A blethering, blustering, drunken blellum;"
line21 = "That frae November till October,"
line22 = "Ae market-day thou was nae sober,"
line23 = "That ilka melder, wi' the miller"

lines = [line, line2, line3, line4,
         line5, line6, line7, line8,
         line9, line10, line11, line12,
         line13, line14, line15, line16,
         line17, line18, line19, line20,
         line21, line22, line23]

for line in lines:
    words = line.split(" ")
    r_words = pronouncing.rhymes(words[-1])

    if (r_words):
        new_word = random.choice(r_words)
        words[-1] = new_word

    space = " "
    changed_line = space.join(words)
    print(changed_line)
