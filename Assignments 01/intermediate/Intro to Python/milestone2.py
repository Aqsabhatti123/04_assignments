# PROJECT 4 ASSIGNMENTS 

# AUTHOR : Aqsa Bhatti

# ASSIGNMENTS 01

# 02_intermediate

# Intro to Python

# milestone2.py

# PROBLEM STATEMENT


# Milestone #2: Adding in All Planets
# Mars is not the only planet in our solar system with its own unique gravity. In fact, each planet has a different gravitational constant, which affects how much an object would weigh on that planet. Below is a list of the constants for each planet compared to Earth's gravity:

# Mercury: 37.6%

# Venus: 88.9%

# Mars: 37.8%

# Jupiter: 236.0%

# Saturn: 108.1%

# Uranus: 81.5%

# Neptune: 114.0%

# Write a Python program that prompts an Earthling to enter their weight on Earth and then to enter the name of a planet in our solar system. The program should print the equivalent weight on that planet rounded to 2 decimal places if necessary.

# You can assume that the user will always type in a planet with the first letter capitalized and you do not need to worry about the case where they type in something other than one of the above planets.

# SOLUTION :

# Constants 

# for gravity factors of planets compared to Earth
# (Earth's gravity is 1.0)

GRAVITY_FACTORS = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Earth": 1.0,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def main():
    """
    ✨ Calculates your weight on different planets based on Earth's gravity. ✨
    """
    print(f"\n 👋 Welcome to the Interplanetary Weight Calculator! 🌟")
    print(f"\n 🌌 Curious to know your weight on another planet? Let's find out! 🚀\n")

    # Collect Earth weight and planet name
    earth_weight = float(input("\n 💬 Enter your weight on Earth (in kg): "))
    planet = input(f"\n 🪐 Enter the name of a planet: ").capitalize().strip()

    # Check if the planet is valid and calculate weight
    if planet in GRAVITY_FACTORS:
        planet_weight = round(earth_weight * GRAVITY_FACTORS[planet], 2)
        print(f"\n🌍 Your weight on {planet} would be: ✨ {planet_weight} kg ✨")
    else:
        print("\n⚠️ Invalid input! Please run the program again and enter a valid planet name. 🌠")

    print("\n🎉 Thanks for exploring your interplanetary weight! Keep dreaming big! 🌈")

if __name__ == "__main__":
    main()

# --------------------- END OF CODE ---------------------