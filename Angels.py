import random

# Define the data as a Python dictionary
data = {
    "Angels": {
        "1": {
            "Name": "Vehuiah",
            "Choir": "Seraphim",
            "Verse": "Psalms 3:3",
            "Demon Ruled Over": "Bael",
            "Role": "Provides courage, strength, and determination to overcome obstacles"
        },
        "2": {
            "Name": "Jeliel",
            "Choir": "Seraphim",
            "Verse": "Psalms 36:6",
            "Demon Ruled Over": "Purson",
            "Role": "Inspires love, compassion, and harmony"
        },
        "3": {
            "Name": "Sitael",
            "Choir": "Seraphim",
            "Verse": "Psalms 100:3",
            "Demon Ruled Over": "Seere",
            "Role": "Assists in spiritual healing and transformation"
        },
        "4": {
            "Name": "Elemiah",
            "Choir": "Seraphim",
            "Verse": "Psalms 5:8",
            "Demon Ruled Over": "Vepar",
            "Role": "Brings divine guidance and protection"
        },
        "5": {
            "Name": "Mahasiah",
            "Choir": "Seraphim",
            "Verse": "Psalms 119:76",
            "Demon Ruled Over": "Andras",
            "Role": "Fosters spiritual growth and enlightenment"
        },
        "6": {
            "Name": "Lelahel",
            "Choir": "Seraphim",
            "Verse": "Psalms 105:8",
            "Demon Ruled Over": "Purson",
            "Role": "Promotes wisdom and insight"
        },
        "7": {
            "Name": "Achaiah",
            "Choir": "Seraphim",
            "Verse": "Psalms 83:18",
            "Demon Ruled Over": "Morax",
            "Role": "Guides in spiritual evolution and development"
        },
        "8": {
            "Name": "Cahetel",
            "Choir": "Seraphim",
            "Verse": "Psalms 36:6",
            "Demon Ruled Over": "Purson",
            "Role": "Facilitates emotional healing and transformation"
        },
        "9": {
            "Name": "Haziel",
            "Choir": "Seraphim",
            "Verse": "Psalms 119:76",
            "Demon Ruled Over": "Andras",
            "Role": "Strengthens connection with divine guidance"
        },
        "10": {
            "Name": "Aladiah",
            "Choir": "Cherubim",
            "Verse": "Psalms 105:8",
            "Demon Ruled Over": "Purson",
            "Role": "Brings harmony and balance"
        },
        "11": {
            "Name": "Lauviah",
            "Choir": "Cherubim",
            "Verse": "Psalms 83:18",
            "Demon Ruled Over": "Morax",
            "Role": "Assists in manifestation of desires"
        },
        "12": {
            "Name": "Hahaiah",
            "Choir": "Cherubim",
            "Verse": "Psalms 36:6",
            "Demon Ruled Over": "Purson",
            "Role": "Fosters creativity and inspiration"
        },
        "13": {
            "Name": "Yezalel",
            "Choir": "Cherubim",
            "Verse": "Psalms 119:76",
            "Demon Ruled Over": "Andras",
            "Role": "Promotes harmony and cooperation"
        },
        "14": {
            "Name": "Mebahel",
            "Choir": "Cherubim",
            "Verse": "Psalms 105:8",
            "Demon Ruled Over": "Purson",
            "Role": "Assists in overcoming challenges"
        },
        "15": {
            "Name": "Hariel",
            "Choir": "Cherubim",
            "Verse": "Psalms 83:18",
            "Demon Ruled Over": "Morax",
            "Role": "Guides in spiritual growth and development"
        },
        "16": {
            "Name": "Hekamiah",
            "Choir": "Cherubim",
            "Verse": "Psalms 36:6",
            "Demon Ruled Over": "Purson",
            "Role": "Strengthens intuition and inner guidance"
        },
        "17": {
            "Name": "Lauviah",
            "Choir": "Cherubim",
            "Verse": "Psalms 119:76",
            "Demon Ruled Over": "Andras",
            "Role": "Brings clarity and insight"
        },
        "18": {
            "Name": "Caliel",
            "Choir": "Cherubim",
            "Verse": "Psalms 105:8",
            "Demon Ruled Over": "Purson",
            "Role": "Assists in decision-making and discernment"
        },
        "19": {
            "Name": "Leuviah",
            "Choir": "Thrones",
            "Verse": "Psalms 83:18",
            "Demon Ruled Over": "Morax",
            "Role": "Empowers in leadership and authority"
        },
        "20": {
            "Name": "Pahaliah",
            "Choir": "Thrones",
            "Verse": "Psalms 105:8",
            "Demon Ruled Over": "Purson",
            "Role": "Promotes wisdom and knowledge"
        },
        "21": {
            "Name": "Nelchael",
            "Choir": "Thrones",
            "Verse": "Psalms 83:18",
            "Demon Ruled Over": "Morax",
            "Role": "Assists in spiritual transformation"
        },
        "22": {
            "Name": "Yeiayel",
            "Choir": "Thrones",
            "Verse": "Psalms 104:4",
            "Demon Ruled Over": "Ipos",
            "Role": "Brings inner peace and tranquility"
        },
        "23": {
            "Name": "Melahel",
            "Choir": "Thrones",
            "Verse": "Psalms 36:6",
            "Demon Ruled Over": "Purson",
            "Role": "Provides healing and protection"
        },
        "24": {
            "Name": "Haheuiah",
            "Choir": "Dominions",
            "Verse": "Psalms 119:76",
            "Demon Ruled Over": "Andras",
            "Role": "Brings divine inspiration and creativity"
        },
        "25": {
            "Name": "Nith-Haiah",
            "Choir": "Dominions",
            "Verse": "Psalms 105:8",
            "Demon Ruled Over": "Purson",
            "Role": "Assists in spiritual healing"
        },
        "26": {
            "Name": "Haaiah",
            "Choir": "Dominions",
            "Verse": "Psalms 83:18",
            "Demon Ruled Over": "Morax",
            "Role": "Fosters spiritual growth and evolution"
        },
        "27": {
            "Name": "Jerathel",
            "Choir": "Dominions",
            "Verse": "Psalms 36:6",
            "Demon Ruled Over": "Purson",
            "Role": "Promotes divine wisdom and understanding"
        },
        "28": {
            "Name": "Seheiah",
            "Choir": "Virtues",
            "Verse": "Psalms 119:76",
            "Demon Ruled Over": "Andras",
            "Role": "Brings divine inspiration and creativity"
        },
        "29": {
            "Name": "Reyiel",
            "Choir": "Virtues",
            "Verse": "Psalms 105:8",
            "Demon Ruled Over": "Purson",
            "Role": "Assists in spiritual growth and enlightenment"
        },
        "30": {
            "Name": "Omael",
            "Choir": "Virtues",
            "Verse": "Psalms 83:18",
            "Demon Ruled Over": "Morax",
            "Role": "Guides in spiritual evolution"
        },
        "31": {
            "Name": "Lecabel",
            "Choir": "Virtues",
            "Verse": "Psalms 36:6",
            "Demon Ruled Over": "Purson",
            "Role": "Fosters inner strength and resilience"
        },
        "32": {
            "Name": "Vasariah",
            "Choir": "Virtues",
            "Verse": "Psalms 119:76",
            "Demon Ruled Over": "Andras",
            "Role": "Promotes spiritual healing and transformation"
        },
        "33": {
            "Name": "Yehuiah",
            "Choir": "Virtues",
            "Verse": "Psalms 105:8",
            "Demon Ruled Over": "Purson",
            "Role": "Brings divine protection and guidance"
        },
        "34": {
            "Name": "Lehahiah",
            "Choir": "Virtues",
            "Verse": "Psalms 83:18",
            "Demon Ruled Over": "Morax",
            "Role": "Assists in manifestation of desires"
        },
        "35": {
            "Name": "Chavakiah",
            "Choir": "Powers",
            "Verse": "Psalms 36:6",
            "Demon Ruled Over": "Purson",
            "Role": "Strengthens connection with divine will"
        },
        "36": {
            "Name": "Menadel",
            "Choir": "Powers",
            "Verse": "Psalms 119:76",
            "Demon Ruled Over": "Andras",
            "Role": "Assists in overcoming obstacles and challenges"
        },
        "37": {
            "Name": "Aniel",
            "Choir": "Powers",
            "Verse": "Psalms 105:8",
            "Demon Ruled Over": "Purson",
            "Role": "Promotes spiritual growth and evolution"
        },
        "38": {
            "Name": "Haamiah",
            "Choir": "Powers",
            "Verse": "Psalms 83:18",
            "Demon Ruled Over": "Morax",
            "Role": "Fosters inner strength and determination"
        },
        "39": {
            "Name": "Rehael",
            "Choir": "Virtues",
            "Verse": "Psalms 5:8",
            "Demon Ruled Over": "Vepar",
            "Role": "Brings divine guidance and protection"
        },
        "40": {
            "Name": "Ieiazel",
            "Choir": "Principalities",
            "Verse": "Psalms 25:10",
            "Demon Ruled Over": "Sabnock",
            "Role": "Promotes spiritual growth and evolution"
        },
        "41": {
            "Name": "Hahahel",
            "Choir": "Principalities",
            "Verse": "Psalms 104:4",
            "Demon Ruled Over": "Ipos",
            "Role": "Brings divine grace and blessings"
        },
        "42": {
            "Name": "Mikhael",
            "Choir": "Principalities",
            "Verse": "Psalms 119:76",
            "Demon Ruled Over": "Andras",
            "Role": "Assists in spiritual transformation"
        },
        "43": {
            "Name": "Veuliah",
            "Choir": "Principalities",
            "Verse": "Psalms 105:8",
            "Demon Ruled Over": "Purson",
            "Role": "Provides healing and protection"
        },
        "44": {
            "Name": "Yelahiah",
            "Choir": "Principalities",
            "Verse": "Psalms 83:18",
            "Demon Ruled Over": "Morax",
            "Role": "Promotes wisdom and knowledge"
        },
        "45": {
            "Name": "Sitaell",
            "Choir": "Principalities",
            "Verse": "Psalms 36:6",
            "Demon Ruled Over": "Purson",
            "Role": "Empowers in leadership and authority"
        },
        "46": {
            "Name": "Venuseh",
            "Choir": "Powers",
            "Verse": "Psalms 105:8",
            "Demon Ruled Over": "Purson",
            "Role": "Guides in spiritual evolution and development"
        },
        "47": {
            "Name": "Vasiah",
            "Choir": "Powers",
            "Verse": "Psalms 83:18",
            "Demon Ruled Over": "Morax",
            "Role": "Facilitates emotional healing and transformation"
        },
        "48": {
            "Name": "Acaniel",
            "Choir": "Powers",
            "Verse": "Psalms 36:6",
            "Demon Ruled Over": "Purson",
            "Role": "Strengthens connection with divine guidance"
        },
        "49": {
            "Name": "Kamael",
            "Choir": "Powers",
            "Verse": "Psalms 119:76",
            "Demon Ruled Over": "Andras",
            "Role": "Brings harmony and balance"
        },
        "50": {
            "Name": "Umabel",
            "Choir": "Virtues",
            "Verse": "Psalms 105:8",
            "Demon Ruled Over": "Purson",
            "Role": "Assists in manifestation of desires"
        },
        "51": {
            "Name": "Iahhel",
            "Choir": "Virtues",
            "Verse": "Psalms 83:18",
            "Demon Ruled Over": "Morax",
            "Role": "Fosters creativity and inspiration"
        },
        "52": {
            "Name": "Anauel",
            "Choir": "Virtues",
            "Verse": "Psalms 36:6",
            "Demon Ruled Over": "Purson",
            "Role": "Promotes harmony and cooperation"
        },
        "53": {
            "Name": "Mehiel",
            "Choir": "Virtues",
            "Verse": "Psalms 119:76",
            "Demon Ruled Over": "Andras",
            "Role": "Assists in overcoming challenges"
        },
        "54": {
            "Name": "Damabiah",
            "Choir": "Virtues",
            "Verse": "Psalms 105:8",
            "Demon Ruled Over": "Purson",
            "Role": "Guides in spiritual growth and development"
        },
        "55": {
            "Name": "Manakel",
            "Choir": "Virtues",
            "Verse": "Psalms 83:18",
            "Demon Ruled Over": "Morax",
            "Role": "Strengthens intuition and inner guidance"
        },
        "56": {
            "Name": "Eyael",
            "Choir": "Dominions",
            "Verse": "Psalms 36:6",
            "Demon Ruled Over": "Purson",
            "Role": "Brings clarity and insight"
        },
        "57": {
            "Name": "Habuiah",
            "Choir": "Dominions",
            "Verse": "Psalms 119:76",
            "Demon Ruled Over": "Andras",
            "Role": "Assists in decision-making and discernment"
        },
        "58": {
            "Name": "Rochel",
            "Choir": "Dominions",
            "Verse": "Psalms 105:8",
            "Demon Ruled Over": "Purson",
            "Role": "Empowers in leadership and authority"
        },
        "59": {
            "Name": "Jabamiah",
            "Choir": "Dominions",
            "Verse": "Psalms 83:18",
            "Demon Ruled Over": "Morax",
            "Role": "Promotes wisdom and knowledge"
        },
        "60": {
            "Name": "Haiaiel",
            "Choir": "Dominions",
            "Verse": "Psalms 36:6",
            "Demon Ruled Over": "Purson",
            "Role": "Provides healing and protection"
        },
        "61": {
            "Name": "Mumiah",
            "Choir": "Thrones",
            "Verse": "Psalms 119:76",
            "Demon Ruled Over": "Andras",
            "Role": "Brings divine inspiration and creativity"
        },
        "62": {
            "Name": "Vehuel",
            "Choir": "Thrones",
            "Verse": "Psalms 105:8",
            "Demon Ruled Over": "Purson",
            "Role": "Assists in spiritual healing"
        },
        "63": {
            "Name": "Yezalel",
            "Choir": "Thrones",
            "Verse": "Psalms 83:18",
            "Demon Ruled Over": "Morax",
            "Role": "Fosters spiritual growth and evolution"
        },
        "64": {
            "Name": "Sitaell",
            "Choir": "Thrones",
            "Verse": "Psalms 36:6",
            "Demon Ruled Over": "Purson",
            "Role": "Promotes divine wisdom and understanding"
        },
        "65": {
            "Name": "Elemiah",
            "Choir": "Cherubim",
            "Verse": "Psalms 119:76",
            "Demon Ruled Over": "Andras",
            "Role": "Brings divine inspiration and creativity"
        },
        "66": {
            "Name": "Mahasiah",
            "Choir": "Cherubim",
            "Verse": "Psalms 105:8",
            "Demon Ruled Over": "Purson",
            "Role": "Assists in spiritual growth and enlightenment"
        },
        "67": {
            "Name": "Lelahel",
            "Choir": "Cherubim",
            "Verse": "Psalms 83:18",
            "Demon Ruled Over": "Morax",
            "Role": "Guides in spiritual evolution"
        },
        "68": {
            "Name": "Achaiah",
            "Choir": "Cherubim",
            "Verse": "Psalms 36:6",
            "Demon Ruled Over": "Purson",
            "Role": "Fosters inner strength and resilience"
        },
        "69": {
            "Name": "Cahetel",
            "Choir": "Cherubim",
            "Verse": "Psalms 119:76",
            "Demon Ruled Over": "Andras",
            "Role": "Promotes spiritual healing and transformation"
        },
        "70": {
            "Name": "Haziel",
            "Choir": "Cherubim",
            "Verse": "Psalms 105:8",
            "Demon Ruled Over": "Purson",
            "Role": "Brings divine protection and guidance"
        },
        "71": {
            "Name": "Aladiah",
            "Choir": "Cherubim",
            "Verse": "Psalms 83:18",
            "Demon Ruled Over": "Morax",
            "Role": "Assists in manifestation of desires"
        },
        "72": {
            "Name": "Lauviah",
            "Choir": "Cherubim",
            "Verse": "Psalms 36:6",
            "Demon Ruled Over": "Purson",
            "Role": "Strengthens connection with divine will"
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
    input("Press Enter to see the next angel...")
