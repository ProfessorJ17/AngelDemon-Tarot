import random

# Define the data as a Python dictionary
data = {
    "Angels": {
        "1": {
                    "Name": "Bael",
        "Choir": "King",
        "Angel Ruled Over": "Vehuiah",
        "Role": "Provides leadership, guidance, and protection in times of adversity"
    },
    "2": {
        "Name": "Agares",
        "Choir": "Duke",
        "Angel Ruled Over": "Ieliel",
        "Role": "Teaches languages, protects against deceit, and helps in finding lost objects"
    },
    "3": {
        "Name": "Vassago",
        "Choir": "Prince",
        "Angel Ruled Over": "Sitael",
        "Role": "Reveals hidden knowledge, aids in divination, and assists in discovering lost or hidden treasures"
    },
    "4": {
        "Name": "Samigina",
        "Choir": "Marquis",
        "Angel Ruled Over": "Elemiah",
        "Role": "Instructs in sciences and mechanical arts, offers guidance in craftsmanship, and bestows familiar spirits"
    },
    "5": {
        "Name": "Marbas",
        "Choir": "President",
        "Angel Ruled Over": "Mahasiah",
        "Role": "Heals physical ailments, provides knowledge of herbal medicine, and reveals hidden truths"
    },
    "6": {
        "Name": "Valefor",
        "Choir": "Duke",
        "Angel Ruled Over": "Iehahel",
        "Role": "Aids in finding treasures, promotes exploration, and imparts knowledge of natural treasures"
    },
    "7": {
        "Name": "Amon",
        "Choir": "Marquis",
        "Angel Ruled Over": "Achaiah",
        "Role": "Bestows wisdom in arts and sciences, imparts knowledge of divine mysteries, and reveals secrets"
    },
    "8": {
        "Name": "Barbatos",
        "Choir": "Duke",
        "Angel Ruled Over": "Cahethel",
        "Role": "Understands the language of animals, provides guidance in agriculture, and aids in communication with nature spirits"
    },
    "9": {
        "Name": "Paimon",
        "Choir": "King",
        "Angel Ruled Over": "Haziel",
        "Role": "Bestows honors and dignities, imparts knowledge of the arts and sciences, and reveals hidden truths"
    },
    "10": {
        "Name": "Buer",
        "Choir": "President",
        "Angel Ruled Over": "Aladiah",
        "Role": "Teaches philosophy and logic, fosters goodwill among allies and adversaries, and aids in decision-making"
    },
    "11": {
        "Name": "Guison",
        "Choir": "Duke",
        "Angel Ruled Over": "Laviah",
        "Role": "Brings harmony to relationships, assists in uncovering buried treasures, and reveals divine insights"
    },
    "12": {
        "Name": "Sitri",
        "Choir": "Prince",
        "Angel Ruled Over": "Hahaiah",
        "Role": "Influences love and passion, fosters romantic connections, and facilitates romantic encounters"
    },
    "13": {
        "Name": "Beleth",
        "Choir": "King",
        "Angel Ruled Over": "Iezalel",
        "Role": "Stimulates desire and passion, inspires love, and fosters romantic relationships"
    },
    "14": {
        "Name": "Leraje",
        "Choir": "Marquis",
        "Angel Ruled Over": "Mebahel",
        "Role": "Aids in archery, promotes skill in warfare, and offers guidance in strategy"
    },
    "15": {
        "Name": "Eligos",
        "Choir": "Duke",
        "Angel Ruled Over": "Hariel",
        "Role": "Reveals hidden truths, imparts knowledge of war strategy, and assists in military matters"
    },
    "16": {
        "Name": "Zepar",
        "Choir": "Duke",
        "Angel Ruled Over": "Hakamiah",
        "Role": "Fosters love and passion, facilitates romantic encounters, and enhances sexual attraction"
    },
    "17": {
        "Name": "Botis",
        "Choir": "Count or President",
        "Angel Ruled Over": "Loviah",
        "Role": "Reveals hidden truths, predicts the future, and assists in resolving disputes"
    },
    "18": {
        "Name": "Bathin",
        "Choir": "Duke",
        "Angel Ruled Over": "Caliel",
        "Role": "Facilitates astral travel, aids in divination, and provides guidance in exploring the subconscious"
    },
    "19": {
        "Name": "Sallos",
        "Choir": "Duke",
        "Angel Ruled Over": "Levuiah",
        "Role": "Promotes love and attraction, fosters harmonious relationships, and enhances emotional connections"
    },
    "20": {
        "Name": "Purson",
        "Choir": "King",
        "Angel Ruled Over": "Pahaliah",
        "Role": "Reveals hidden knowledge, imparts wisdom, and assists in discovering hidden treasures"
    },
    "21": {
        "Name": "Marax",
        "Choir": "Count or President",
        "Angel Ruled Over": "Nelchael",
        "Role": "Teaches craftsmanship, imparts knowledge of herbalism, and aids in spellcasting"
    },
    "22": {
        "Name": "Ipos",
        "Choir": "Count or Prince",
        "Angel Ruled Over": "Ieiaiel",
        "Role": "Reveals hidden knowledge, imparts wisdom, and assists in divination"
    },
    "23": {
        "Name": "Aim",
        "Choir": "Duke",
        "Angel Ruled Over": "Melahel",
        "Role": "Facilitates communication with spirits, aids in divination, and enhances psychic abilities"
    },
    "24": {
        "Name": "Naberius",
        "Choir": "Marquis",
        "Angel Ruled Over": "Hahuiah",
        "Role": "Teaches arts and sciences, imparts knowledge of philosophy, and enhances intellectual abilities"
    },
    "25": {
        "Name": "Glasya-Labolas",
        "Choir": "Count or President",
        "Angel Ruled Over": "Nithhaiah",
        "Role": "Imparts knowledge of warfare, promotes skill in combat, and aids in strategic planning"
    },
    "26": {
        "Name": "Bune",
        "Choir": "Duke",
        "Angel Ruled Over": "Haaiah",
        "Role": "Brings wealth and prosperity, reveals hidden treasures, and assists in financial matters"
    },
    "27": {
        "Name": "Ronove",
        "Choir": "Count or Marquis",
        "Angel Ruled Over": "Ierathel",
        "Role": "Imparts knowledge of the arts and sciences, fosters creativity, and aids in artistic endeavors"
    },
    "28": {
        "Name": "Berith",
        "Choir": "Duke",
        "Angel Ruled Over": "Seehiah",
        "Role": "Grants knowledge of the occult, imparts wisdom, and aids in communication with spirits"
    },
    "29": {
        "Name": "Astaroth",
        "Choir": "Duke",
        "Angel Ruled Over": "Reiaiel",
        "Role": "Teaches the liberal arts, imparts knowledge of sciences, and aids in achieving personal goals"
    },
    "30": {
        "Name": "Forneus",
        "Choir": "Marquis",
        "Angel Ruled Over": "Omael",
        "Role": "Teaches language and rhetoric, imparts knowledge of philosophy, and aids in diplomacy"
    },
    "31": {
        "Name": "Foras",
        "Choir": "President",
        "Angel Ruled Over": "Lecabel",
        "Role": "Imparts knowledge of languages, reveals hidden truths, and assists in understanding foreign cultures"
    },
    "32": {
        "Name": "Asmoday",
        "Choir": "King",
        "Angel Ruled Over": "Vasariah",
        "Role": "Imparts knowledge of the arts and sciences, aids in discovering hidden truths, and reveals secrets"
    },
    "33": {
        "Name": "Gaap",
        "Choir": "Prince or President",
        "Angel Ruled Over": "Iehuiah",
        "Role": "Reveals hidden knowledge, imparts wisdom, and aids in divination"
    },
    "34": {
        "Name": "Furfur",
        "Choir": "Count",
        "Angel Ruled Over": "Lehahiah",
        "Role": "Promotes love and passion, fosters harmonious relationships, and enhances emotional connections"
    },
    "35": {
        "Name": "Marchosias",
        "Choir": "Marquis",
        "Angel Ruled Over": "Chauakiah",
        "Role": "Imparts knowledge of warfare, enhances leadership abilities, and aids in strategic planning"
    },
    "36": {
        "Name": "Stolas",
        "Choir": "Prince",
        "Angel Ruled Over": "Manadel",
        "Role": "Teaches astronomy and astrology, imparts knowledge of the stars, and aids in divination"
    },
    "37": {
        "Name": "Phenex",
        "Choir": "Marquis",
        "Angel Ruled Over": "Aniel",
        "Role": "Inspires creativity, fosters artistic talent, and aids in artistic expression"
    },
    "38": {
        "Name": "Halphas",
        "Choir": "Count",
        "Angel Ruled Over": "Haamiah",
        "Role": "Promotes skill in warfare, aids in military strategy, and enhances leadership abilities"
    },
    "39": {
        "Name": "Malphas",
        "Choir": "President",
        "Angel Ruled Over": "Rehael",
        "Role": "Builds structures and fortifications, imparts knowledge of architecture, and aids in construction"
    },
    "40": {
        "Name": "Raum",
        "Choir": "Count",
        "Angel Ruled Over": "Ieiazel",
        "Role": "Reveals hidden treasures, imparts knowledge of natural treasures, and aids in their discovery"
    },
    "41": {
        "Name": "Focalor",
        "Choir": "Duke",
        "Angel Ruled Over": "Hahahel",
        "Role": "Controls the winds and seas, protects sailors, and aids in navigation"
    },
    "42": {
        "Name": "Vepar",
        "Choir": "Duke",
        "Angel Ruled Over": "Mikael",
        "Role": "Controls the waters and ships, protects against naval attacks, and aids in maritime endeavors"
    },
    "43": {
        "Name": "Sabnock",
        "Choir": "Marquis",
        "Angel Ruled Over": "Veualiah",
        "Role": "Builds and fortifies structures, protects against enemies, and aids in defense"
    },
    "44": {
        "Name": "Shax",
        "Choir": "Marquis",
        "Angel Ruled Over": "Ielahiah",
        "Role": "Teaches craftsmanship, imparts knowledge of mechanical arts, and aids in artistic expression"
    },
    "45": {
        "Name": "Vine",
        "Choir": "Count or King",
        "Angel Ruled Over": "Sealiah",
        "Role": "Reveals hidden truths, imparts knowledge of natural phenomena, and aids in understanding the mysteries of the universe"
    },
    "46": {
        "Name": "Bifrons",
        "Choir": "Count",
        "Angel Ruled Over": "Ariel",
        "Role": "Reveals hidden knowledge, imparts wisdom, and aids in divination"
    },
    "47": {
        "Name": "Vual",
        "Choir": "Duke",
        "Angel Ruled Over": "Asaliah",
        "Role": "Imparts knowledge of the natural world, aids in understanding animals, and facilitates communication with them"
    },
    "48": {
        "Name": "Haagenti",
        "Choir": "President",
        "Angel Ruled Over": "Mihael",
        "Role": "Provides abundance and prosperity, imparts knowledge of alchemy, and aids in transmutation"
    },
    "49": {
        "Name": "Crocell",
        "Choir": "Duke",
        "Angel Ruled Over": "Vehuel",
        "Role": "Teaches the liberal arts, imparts knowledge of music, and aids in artistic expression"
    },
    "50": {
        "Name": "Furcas",
        "Choir": "Knight",
        "Angel Ruled Over": "Daniel",
        "Role": "Imparts knowledge of the natural world, aids in understanding animals, and facilitates communication with them"
    },
    "51": {
        "Name": "Balam",
        "Choir": "King",
        "Angel Ruled Over": "Hahasiah",
        "Role": "Reveals hidden knowledge, imparts wisdom, and aids in divination"
    },
    "52": {
        "Name": "Alloces",
        "Choir": "Duke",
        "Angel Ruled Over": "Imamiah",
        "Role": "Teaches the occult sciences, imparts knowledge of astrology, and aids in understanding cosmic forces"
    },
    "53": {
        "Name": "Caim",
        "Choir": "President",
        "Angel Ruled Over": "Nanael",
        "Role": "Reveals hidden knowledge, imparts wisdom, and aids in divination"
    },
    "54": {
        "Name": "Murmur",
        "Choir": "Count or Duke",
        "Angel Ruled Over": "Nithael",
        "Role": "Inspires music and art, imparts knowledge of the creative process, and aids in artistic expression"
    },
    "55": {
        "Name": "Orobas",
        "Choir": "Prince",
        "Angel Ruled Over": "Mebahiah",
        "Role": "Reveals hidden knowledge, imparts wisdom, and aids in divination"
    },
    "56": {
        "Name": "Gremory",
        "Choir": "Duke",
        "Angel Ruled Over": "Poiel",
        "Role": "Reveals hidden knowledge, imparts wisdom, and aids in divination"
    },
    "57": {
        "Name": "Ose",
        "Choir": "President",
        "Angel Ruled Over": "Nemamiah",
        "Role": "Teaches the liberal arts, imparts knowledge of the sciences, and aids in intellectual pursuits"
    },
    "58": {
        "Name": "Amy",
        "Choir": "President",
        "Angel Ruled Over": "Ieialel",
        "Role": "Reveals hidden knowledge, imparts wisdom, and aids in divination"
    },
    "59": {
        "Name": "Orias",
        "Choir": "Marquis",
        "Angel Ruled Over": "Harahel",
        "Role": "Aids in divination, reveals hidden knowledge, and imparts wisdom"
    },
    "60": {
        "Name": "Vapula",
        "Choir": "Duke",
        "Angel Ruled Over": "Mizrael",
        "Role": "Teaches the arts and sciences, imparts knowledge of technology, and aids in innovation"
    },
    "61": {
        "Name": "Zagan",
        "Choir": "King or President",
        "Angel Ruled Over": "Umabel",
        "Role": "Teaches the occult sciences, imparts knowledge of demonology, and aids in summoning spirits"
    },
    "62": {
        "Name": "Valac",
        "Choir": "President",
        "Angel Ruled Over": "Iahhel",
        "Role": "Reveals hidden knowledge, imparts wisdom, and aids in divination"
    },
    "63": {
        "Name": "Andras",
        "Choir": "Marquis",
        "Angel Ruled Over": "Anauel",
        "Role": "Imparts knowledge of warfare, enhances leadership abilities, and aids in strategic planning"
    },
    "64": {
        "Name": "Haures",
        "Choir": "Duke",
        "Angel Ruled Over": "Mehiel",
        "Role": "Reveals hidden knowledge, imparts wisdom, and aids in divination"
    },
    "65": {
        "Name": "Andrealphus",
        "Choir": "Marquis",
        "Angel Ruled Over": "Damabiah",
        "Role": "Promotes love and passion, fosters harmonious relationships, and enhances emotional connections"
    },
    "66": {
        "Name": "Cimeies",
        "Choir": "Marquis",
        "Angel Ruled Over": "Manakel",
        "Role": "Reveals hidden knowledge, imparts wisdom, and aids in divination"
    },
    "67": {
        "Name": "Amdusias",
        "Choir": "Duke",
        "Angel Ruled Over": "Eiael",
        "Role": "Teaches the arts and sciences, imparts knowledge of music, and aids in artistic expression"
    },
    "68": {
        "Name": "Belial",
        "Choir": "King",
        "Angel Ruled Over": "Habuhiah",
        "Role": "Promotes independence, fosters self-determination, and aids in achieving personal goals"
    },
    "69": {
        "Name": "Decarabia",
        "Choir": "Marquis",
        "Angel Ruled Over": "Rochel",
        "Role": "Imparts knowledge of herbalism, promotes understanding of plant spirits, and aids in plant magic"
    },
    "70": {
        "Name": "Seere",
        "Choir": "Prince",
        "Angel Ruled Over": "Iabamiah",
        "Role": "Reveals hidden knowledge, imparts wisdom, and aids in divination"
    },
    "71": {
        "Name": "Dantalion",
        "Choir": "Duke",
        "Angel Ruled Over": "Haiaiel",
        "Role": "Reveals hidden knowledge, imparts wisdom, and aids in divination"
    },
    "72": {
        "Name": "Andromalius",
        "Choir": "Count",
        "Angel Ruled Over": "Mumiah",
        "Role": "Aids in detecting theft and deceit, reveals hidden truths, and brings justice to wrongdoing"
    }
    }
}
# Correctly flatten the data into a list of angel dictionaries
angels = list(data['Angels'].values())

# Randomly select 72 angels without replacement
selected_angels = random.sample(angels, 72)

# Print the selected angels one by one, waiting for the user to press Enter
for angel in selected_angels:
    for key, value in angel.items():
        print(f"{key}: {value}")
    input("Press Enter to see the next demon...")
