"""
D&D Name Generation
Author(s): Niklaas Cotta
Created: 01/13/22
"""

import random

races = ["aarakocra", "dragonborn", "dwarf", "elf", "genasi", "gnome",
         "goliath", "half-elf", "halfling", "half-orc", "human", "orc", "tiefling"]

aarakocraFirst = ["Karr", "Qrirr", "Zullec", "Clakkes", "Guie", "Eg", "Kraiakaa", "Haellahk"]

dragonbornFirst = ["Kruziikrel Vyuziros", "Mirmulnir Jinrash", "Naaslaarum Wraseth",
                   "Nahagliiv Zrakris", "Sahloknir Worbor", "Voslaarum Thagil", "Elkethir Smaug"]

dwarfFirst = ["Gundrin Rockseeker", "Dolnik Goldfound", "Thalrak Helbron", "Bharmund Ballohock",
              "Gimli Broadhand", "Jennia Thunderhorn", "Rynlin Greatmask", "Dimnar Rahirahr"]

elfFirst = ["Qinren Moonpride", "Naemenor Yldrinthre", "Adzumin Crimsonseeker",
            "Farnorin Osennenthrenn", "Legolas Farstrider", "Thranduil Goldbloom", "Earendil Moonsoak"]

genasiFirst = ["Fume", "Dewdrop", "Gust", "Spring", "Pyre", "Gale", "Celeste",
               "Jade", "Flute", "Rubble", "Crystal", "Limestone"]

gnomeFirst = ["Sinpip Gobbleriver", "Hiszu Truebranch", "Briros Lighstone", "Yobi Finebraid",
              "Weylore Pebblestand", "Valyur Wildstitch", "Hiscryn Billowbranch", "Manrick Luckyfront"]

goliathFirst = ["Krathag Woundhand Mindtanner", "Kavamul Lumbereye Kolae-Gupine", "Ilalig Rainweaver Vunakulane", "Maavea Foodheart Apunakukena",
                "Gelvu Bearweaver Ganu-Tholake", "Laghan Wisewalker Thenaamino", "Panihl Fearwalker Egena-Vanathi", "Nalthe Strongworker Nugala-Gigane"]

halfElfFirst = ["Wilvalor", "Meicraes", "Bynbwynn", "Elianalore", "Tyllynn", "Quoovar", "Vicneiros",
                "Krifyr", "Fallaninn", "Hoseris", "Urianys", "Ileona", "Panstaer"]

halfOrcFirst = ["Trukorash", "Kraedak", "Turg", "Durodim", "Shayome", "Urash", "Kutiazur", "Zunorel", "Maruruk",
                "Ogguumir", "Bradim", "Therograr", "Shegume", "Kerigh", "Gynagri", "Vaninur", "Meritah", "Rekirsh"]



firstNames = ["Stephanie", "Zuul", "Balfred", "Schnabs", "Beeyorn", "Daved", "Jeel", "Tomey"]
lastNames = ["Windstrider", "Stoneseeker", "Smith", "Hightower", "Ramshorn"]
"Auric"


def generator(race):
    return random.choice(firstNames) + " " + random.choice(lastNames)
