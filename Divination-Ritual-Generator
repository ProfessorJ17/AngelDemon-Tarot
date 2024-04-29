import random

# Define the rituals for each type
purification_rituals = [
    "Take a cleansing bath with sea salt and lavender to purify your energy.",
    "Burn sage or palo santo to clear negative energies from your space.",
    "Recite a purification mantra while visualizing white light cleansing your aura.",
    "Practice breathwork exercises to release stagnant energy from your body.",
    "Meditate by a flowing river or waterfall to cleanse your mind and spirit.",
    "Perform a grounding ritual by walking barefoot on the earth to release excess energy.",
    "Engage in a digital detox by spending a day without electronic devices.",
    "Smudge your home with sacred herbs to purify the energy of your living space.",
    "Purify your sacred objects and crystals by placing them under the light of the full moon.",
    "Reflect on past experiences and forgive yourself and others for any perceived wrongdoings."
]

intent_rituals = [
    "Write a letter to your guardian angel expressing your heartfelt intentions.",
    "Create a vision board illustrating your spiritual goals and aspirations.",
    "Recite a personalized prayer affirming your intention to connect with the divine.",
    "Light a candle and focus your intention on receiving guidance and clarity.",
    "Meditate on a specific question or issue you seek insight on, holding a clear intention.",
    "Dedicate a sacred space in your home for meditation and reflection on your intentions.",
    "Wear a piece of jewelry or carry a talisman symbolizing your intention throughout the day.",
    "Visualize your intention as already manifested, feeling the emotions associated with its fulfillment.",
    "Draw a sigil representing your intention and meditate on it daily.",
    "Write down your intentions and place them in a sacred box or jar, allowing them to manifest in divine timing."
]

invocation_rituals = [
    "Call upon the angelic realm using traditional invocations and sacred names.",
    "Create an altar dedicated to the angels, adorned with candles and offerings.",
    "Recite prayers or mantras invoking the presence of specific angels for guidance.",
    "Use sacred symbols or sigils associated with the angels to amplify your invocation.",
    "Practice chanting or toning sacred sounds to raise your vibration and connect with the angels.",
    "Visualize a beam of light connecting you to the angelic realm, inviting their presence.",
    "Offer prayers of gratitude and devotion to the angels, inviting them to communicate with you.",
    "Write a letter to the angels expressing your intentions and asking for their assistance.",
    "Light a special incense or resin associated with angelic communication during your invocation.",
    "Sit in silent meditation and open your heart to receive messages and guidance from the angels."
]

alignment_rituals = [
    "Align your chakras through a guided meditation, visualizing each energy center glowing with vibrant colors.",
    "Connect with the elements of earth, air, fire, and water, invoking their energies to harmonize with the angelic realm.",
    "Practice yoga or qigong to balance your energy meridians and align your physical and spiritual bodies.",
    "Work with crystals such as selenite or clear quartz to attune your vibration to the frequency of the angels.",
    "Perform a ritualistic dance or movement meditation to align your body with the rhythms of the cosmos.",
    "Spend time in nature, observing the cycles of life and aligning yourself with the natural flow of energy.",
    "Use aromatherapy oils such as frankincense or myrrh to elevate your consciousness and align with the angelic realm.",
    "Reflect on your core values and beliefs, aligning your actions with your highest ideals and aspirations.",
    "Engage in acts of service and compassion, aligning yourself with the divine principle of love and unity.",
    "Invoke the archangels of the four directions—Michael, Gabriel, Uriel, and Raphael—to align yourself with the cosmic forces of protection, communication, illumination, and healing."
]

stillness_rituals = [
    "Practice mindfulness meditation, focusing on your breath and observing your thoughts without judgment.",
    "Spend time in silent contemplation, allowing the stillness to reveal deeper insights and inner wisdom.",
    "Disconnect from technology and external distractions, creating a space for inner peace and quiet.",
    "Listen to calming music or nature sounds to induce a state of relaxation and tranquility.",
    "Engage in gentle movement practices such as tai chi or qigong to cultivate inner stillness.",
    "Sit in nature and observe the sights and sounds around you, becoming fully present in the moment.",
    "Practice deep breathing exercises to quiet the mind and soothe the nervous system.",
    "Create a sacred space for meditation and contemplation, free from clutter and distractions.",
    "Spend time in solitude, allowing yourself to rest and recharge in the embrace of silence.",
    "Reflect on the beauty of existence and the miracle of life, finding peace in the simple moments of being."
]

visualization_rituals = [
    "Create a vision board depicting your dreams and goals, visualizing them as already achieved.",
    "Practice guided imagery meditation, visualizing yourself in a peaceful and serene environment.",
    "Use creative visualization techniques to manifest your desires and attract positive outcomes into your life.",
    "Visualize a protective bubble of light surrounding you, shielding you from negative energies.",
    "Imagine yourself bathed in the healing light of the angels, receiving their love and guidance.",
    "Visualize your body filled with radiant energy, vibrating at the frequency of divine love and harmony.",
    "Picture yourself accomplishing your goals and fulfilling your life's purpose with ease and grace.",
    "Visualize a cord of light connecting you to the angelic realm, facilitating clear communication and guidance.",
    "Envision yourself surrounded by a circle of angels, receiving their blessings and support.",
    "Visualize a golden pathway unfolding before you, leading you toward your highest destiny and spiritual fulfillment."
]

heart_centeredness_rituals = [
    "Practice loving-kindness meditation, cultivating feelings of compassion and empathy for yourself and others.",
    "Perform acts of kindness and generosity, expressing the love and light within your heart.",
    "Engage in heart-centered activities such as journaling, painting, or singing, expressing your emotions and creativity.",
    "Connect with loved ones and community members, nurturing meaningful relationships based on mutual respect and understanding.",
    "Practice forgiveness and letting go of resentment, allowing your heart to heal and open to new possibilities.",
    "Spend time in nature, experiencing the beauty and wonder of the natural world and connecting with the heart of the earth.",
    "Offer prayers of gratitude and thanksgiving, acknowledging the blessings in your life and expressing appreciation for all that you have.",
    "Cultivate a daily gratitude practice, focusing on the abundance and blessings present in each moment.",
    "Practice self-love and self-care, honoring your needs and nurturing your physical, emotional, and spiritual well-being.",
    "Open your heart to receive love and blessings from the universe, trusting in the divine plan and surrendering to the flow of grace."
]

# Create a list of all ritual types
ritual_types = [
    ("Purification", purification_rituals),
    ("Intent", intent_rituals),
    ("Invocation", invocation_rituals),
    ("Alignment", alignment_rituals),
    ("Stillness", stillness_rituals),
    ("Visualization", visualization_rituals),
    ("Heart-Centeredness", heart_centeredness_rituals)
]

# Initialize an empty list to store used combinations
used_combinations = []

# Initialize a counter for reshuffling
reshuffle_counter = 0

# Loop to generate random rituals until the user decides to stop
while True:
    # Increment the reshuffle counter
    reshuffle_counter += 1
    
    # Check if it's time to reshuffle
    if reshuffle_counter > 70:
        # Reshuffle the used combinations
        random.shuffle(used_combinations)
        # Reset the reshuffle counter
        reshuffle_counter = 0
    
    # Initialize a flag for checking if the combination is new
    new_combination = False
    
    # Keep generating random combinations until a new one is found
    while not new_combination:
        # Generate a random ritual for each type
        random_rituals = [(ritual_type[0], random.choice(ritual_type[1])) for ritual_type in ritual_types]
        
        # Check if the combination is new
        if random_rituals not in used_combinations:
            # Add the new combination to the list of used combinations
            used_combinations.append(random_rituals)
            new_combination = True

    # Print the type of ritual
    print("\nDivinity Ritual:")
    # Print the random ritual for each type
    for ritual_type, ritual in random_rituals:
        print(f"{ritual_type}: {ritual}")
    
    # Ask the user if they want to generate more rituals
    if input("\nPress Enter to generate more rituals or type 'exit' to quit: ").lower() == "exit":
        break
