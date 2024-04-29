import random

# Define the Metatron grids with associated geometric shapes and descriptions
metatron_grids = {
    1: {"shape": "Cube (3D)", "description": "9 points (8 vertices + 1 center)", "meaning": "Grounding, stability, and foundation."},
    2: {"shape": "Octahedron (4D)", "description": "17 points (16 vertices + 1 center)", "meaning": "Balance, harmony, and integration of polarities."},
    3: {"shape": "Dodecahedron (5D)", "description": "26 points (20 vertices + 1 center)", "meaning": "Divine wisdom, cosmic consciousness, and spiritual enlightenment."},
    4: {"shape": "Icosahedron (6D)", "description": "37 points (30 vertices + 1 center)", "meaning": "Flow, movement, and adaptability."},
    5: {"shape": "Tetrahedron (3D)", "description": "4 points (4 vertices)", "meaning": "Manifestation, creation, and transformation."},
    6: {"shape": "Star Tetrahedron (4D)", "description": "13 points (12 vertices + 1 center)", "meaning": "Merkaba activation, spiritual protection, and ascension."},
    7: {"shape": "Star Octahedron (5D)", "description": "22 points (20 vertices + 1 center + 1 center of the inner octahedron)", "meaning": "Higher-dimensional awareness, connection with celestial realms."},
    8: {"shape": "Star Dodecahedron (6D)", "description": "31 points (30 vertices + 1 center)", "meaning": "Divine inspiration, creativity, and exploration of higher realms."},
    9: {"shape": "Star Icosahedron (7D)", "description": "40 points (30 vertices + 6 centers of the inner tetrahedra + 4 centers of the inner triangles)", "meaning": "Emotional healing, inner balance, and fluidity of emotions."},
    10: {"shape": "Star Tetra-Octahedron (8D)", "description": "49 points (40 vertices + 1 center of the inner octahedron + 8 centers of the inner tetrahedra)", "meaning": "Integration of higher and lower aspects of self, bridging spiritual and physical realms."},
    11: {"shape": "Star Tetra-Dodecahedron (9D)", "description": "58 points (50 vertices + 1 center of the inner dodecahedron + 6 centers of the inner pentagons + 1 center of the inner pentagon)", "meaning": "Alignment with cosmic frequencies, attunement to universal energies."},
    12: {"shape": "Star Tetra-Icosahedron (10D)", "description": "67 points (60 vertices + 1 center of the inner icosahedron + 6 centers of the inner triangles)", "meaning": "Spiritual expansion, multidimensional awareness, and accessing higher states of consciousness."},
    13: {"shape": "Super Star Tetrahedron (4D)", "description": "13 points (12 vertices + 1 center)", "meaning": "Accelerated spiritual growth, rapid transformation, and evolution."},
    14: {"shape": "Super Star Octahedron (5D)", "description": "22 points (20 vertices + 1 center + 1 center of the inner octahedron)", "meaning": "Amplification of spiritual energies, purification, and alignment with divine will."},
    15: {"shape": "Super Star Dodecahedron (6D)", "description": "31 points (30 vertices + 1 center)", "meaning": "Activation of higher chakras, connection with angelic realms, and divine guidance."},
    16: {"shape": "Super Star Icosahedron (7D)", "description": "40 points (30 vertices + 6 centers of the inner tetrahedra + 4 centers of the inner triangles)", "meaning": "Enhanced intuition, psychic abilities, and spiritual discernment."},
    17: {"shape": "Super Super Star Tetrahedron (8D)", "description": "49 points (40 vertices + 1 center of the inner octahedron + 8 centers of the inner tetrahedra)", "meaning": "Transcendence of limitations, liberation from karmic cycles, and spiritual liberation."},
    18: {"shape": "Super Super Star Octahedron (9D)", "description": "58 points (50 vertices + 1 center of the inner dodecahedron + 6 centers of the inner pentagons + 1 center of the inner pentagon)", "meaning": "Enlightenment, cosmic unity, and oneness with the universe."},
    19: {"shape": "Super Super Star Dodecahedron (10D)", "description": "67 points (60 vertices + 1 center of the inner icosahedron + 6 centers of the inner triangles)", "meaning": "Divine alignment, soul integration, and realization of higher purpose."},
    20: {"shape": "Super Super Star Icosahedron (11D)", "description": "76 points (70 vertices + 6 centers of the inner tetrahedra)", "meaning": "Ascended mastery, divine embodiment, and co-creation with the universe."},
    21: {"shape": "Super Super Super Star Tetrahedron (12D)", "description": "85 points (80 vertices + 1 center of the inner octahedron + 4 centers of the inner tetrahedra)", "meaning": "Cosmic consciousness, universal love, and transcendence of duality."},
    22: {"shape": "Super Super Super Star Octahedron (13D)", "description": "94 points (90 vertices + 1 center of the inner dodecahedron + 3 centers of the inner octahedra)", "meaning": "Unity consciousness, cosmic harmony, and collective evolution."},
    23: {"shape": "Super Super Super Star Dodecahedron (14D)", "description": "103 points (100 vertices + 1 center of the inner icosahedron + 2 centers of the inner dodecahedra)", "meaning": "Divine blueprint activation, spiritual awakening, and cosmic reintegration."},
    24: {"shape": "Super Super Super Star Icosahedron (15D)", "description": "112 points (110 vertices + 1 center of the inner icosahedron + 1 center of the inner dodecahedron)", "meaning": "Divine revelation, cosmic revelation, and alignment with the divine plan."},
    25: {"shape": "Super Super Super Super Star Tetrahedron (16D)", "description": "Unknown", "meaning": "Unknown"},
    26: {"shape": "Super Super Super Super Star Octahedron (17D)", "description": "Unknown", "meaning": "Unknown"},
    27: {"shape": "Super Super Super Super Star Dodecahedron (18D)", "description": "Unknown", "meaning": "Unknown"},
    28: {"shape": "Super Super Super Super Star Icosahedron (19D)", "description": "Unknown", "meaning": "Unknown"}
}

# Create a list to keep track of chosen grids
chosen_grids = []

# Function to shuffle the grids
def shuffle_grids():
    random.shuffle(chosen_grids)

# Function to pick a random grid
def pick_grid():
    # Check if all grids have been chosen
    if len(chosen_grids) == len(metatron_grids):
        # Reshuffle the grids
        shuffle_grids()
    
    # Pick a random grid that hasn't been chosen yet
    while True:
        grid = random.randint(1, len(metatron_grids))
        if grid not in chosen_grids:
            chosen_grids.append(grid)
            return grid

# Main loop to pick grids
while True:
    # Prompt the user to press Enter or type 'exit'
    choice = input("Press Enter to pick a random Metatron grid or type 'exit' to quit: ").strip().lower()
    
    # Check if the user wants to exit
    if choice == "exit":
        break
    
    # Pick a random grid
    random_grid = pick_grid()
    
    # Print the chosen grid and its associated shape, description, and meaning
    print(f"Chosen Metatron Grid {random_grid}:")
    print(f"- Shape: {metatron_grids[random_grid]['shape']}")
    print(f"- Description: {metatron_grids[random_grid]['description']}")
    print(f"- Meaning: {metatron_grids[random_grid]['meaning']}\n")

# Reshuffle the grids before exiting
shuffle_grids()
print("All Metatron grids have been chosen and reshuffled.")
