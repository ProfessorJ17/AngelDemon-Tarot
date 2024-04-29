import random

# Dictionary of frequencies with descriptions
frequencies = {
    "174 Hz": "Known as the healing frequency, 174 Hz has been found to have the greatest potential effect on the physical body when compared to the other frequencies. This low frequency could alleviate pain and stress, improve concentration, and give the organs in the body a sense of security. The frequency may also relax muscles and lessen tension in the body, making it particularly beneficial for those experiencing migraines or pain in the lower back, feet, legs, and more.",
    "285 Hz": "This frequency has the potential to heal and restore tissue. It could support the immune system, balance your energy, and increase feelings of security and safety.",
    "396 Hz": "396 Hz could aid in the elimination of guilt, subconscious fears, negative beliefs, and grief, providing a sense of security. Because the frequency generates uplifting energy, it may be effective as motivational music.",
    "417 Hz": "The frequency may aid in the healing of trauma. It’s said to help clear negative energy from your body and space, as well as negative thoughts and behaviors. 417 Hz could help you find the motivation to embrace change while also promoting restful sleep.",
    "528 Hz": "This is considered one of the most potent frequencies, with a higher potential impact on sleep and wellness. Also known as the ‘love frequency,’ ‘miracle tone,’ and ‘frequency of transformation,’ 528 Hz could stimulate imagination, intention, and intuition. Moreover, the frequency has been shown to support cortisol reduction (the stress hormone), lifting your mood and putting you in a state of serenity and relaxation, all of which can improve sleep quality.",
    "639 Hz": "639 Hz may aid in achieving mental balance. It can foster harmonious relationships between loved ones and the community in which you live, plus it promotes comprehension, communication, and tolerance.",
    "741 Hz": "By potentially stimulating the mind, promoting creativity and self-expression, and providing mental clarity, this frequency could help with intellectual work and problem-solving. It can also support decision making, which can lead to a healthier and more fulfilling life. Known as a “detoxifying frequency,” 741 Hz could be used to help those suffering from chronic pain.",
    "852 Hz": "This frequency can aid in the replacement of negative thoughts with positive ones, making it helpful for relieving nervousness or anxiety.",
    "963 Hz": "963 Hz is associated with activating your pineal gland, raising consciousness, and awakening intuition. The frequency is also believed to increase positive energy and provide clarity."
}

# List of 88 constellations
constellations = [
    "Andromeda", "Antlia", "Apus", "Aquarius", "Aquila", "Ara", "Aries", "Auriga", "Boötes", "Caelum",
    "Camelopardalis", "Cancer", "Canes Venatici", "Canis Major", "Canis Minor", "Capricornus", "Carina", "Cassiopeia", "Centaurus", "Cepheus",
    "Cetus", "Chamaeleon", "Circinus", "Columba", "Coma Berenices", "Corona Australis", "Corona Borealis", "Corvus", "Crater", "Crux",
    "Cygnus", "Delphinus", "Dorado", "Draco", "Equuleus", "Eridanus", "Fornax", "Gemini", "Grus", "Hercules",
    "Horologium", "Hydra", "Hydrus", "Indus", "Lacerta", "Leo", "Leo Minor", "Lepus", "Libra", "Lupus",
    "Lynx", "Lyra", "Mensa", "Microscopium", "Monoceros", "Musca", "Norma", "Octans", "Ophiuchus", "Orion",
    "Pavo", "Pegasus", "Perseus", "Phoenix", "Pictor", "Pisces", "Piscis Austrinus", "Puppis", "Pyxis", "Reticulum",
    "Sagitta", "Sagittarius", "Scorpius", "Sculptor", "Scutum", "Serpens", "Sextans", "Taurus", "Telescopium", "Triangulum",
    "Triangulum Australe", "Tucana", "Ursa Major", "Ursa Minor", "Vela", "Virgo", "Volans", "Vulpecula"
]

# List of planets
planets = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]

# List to keep track of previous combinations
previous_combinations = []

# Function to generate a new combination
def generate_combination():
    # Choose a random frequency
    random_frequency, description = random.choice(list(frequencies.items()))
    
    # Choose a random constellation
    random_constellation = random.choice(constellations)
    
    # Choose a random planet
    random_planet = random.choice(planets)
    
    # Choose random portal open and portal close time
    portal_open_time = generate_random_time()
    portal_close_time = generate_random_time()
    
    return random_frequency, description, random_constellation, random_planet, portal_open_time, portal_close_time

# Function to generate random time within 24 hours
def generate_random_time():
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    millisecond = random.randint(0, 999)
    return hour, minute, second, millisecond

# Main loop to generate combinations
while True:
    # Generate a new combination
    random_frequency, description, random_constellation, random_planet, portal_open_time, portal_close_time = generate_combination()
    
    # Check if the combination has not been used in the previous 72 readings
    if (random_frequency, random_constellation, random_planet) not in previous_combinations:
        # Add the combination to the list of previous combinations
        previous_combinations.append((random_frequency, random_constellation, random_planet))
        
        # If the number of previous combinations exceeds 72, remove the oldest combination
        if len(previous_combinations) > 72:
            previous_combinations.pop(0)
        
        # Print the chosen frequency, description, constellation, planet, portal open time, and portal close time
        print(f"Chosen Frequency: {random_frequency}")
        print("Description:")
        print(description)
        print(f"\nChosen Constellation: {random_constellation}")
        print(f"Chosen Planet: {random_planet}")
        print(f"Portal Open Time: {portal_open_time[0]}:{portal_open_time[1]}:{portal_open_time[2]}.{portal_open_time[3]}")
        print(f"Portal Close Time: {portal_close_time[0]}:{portal_close_time[1]}:{portal_close_time[2]}.{portal_close_time[3]}")
        
        # Break the loop after generating a valid combination
        break
