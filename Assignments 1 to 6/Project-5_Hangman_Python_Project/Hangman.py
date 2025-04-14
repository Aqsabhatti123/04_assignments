# Project 05 : Hangman Game in Python

# Instructor : Aqsa Bhatti

# Import the random module

import random

# Words categorized by themes
categories = {
    "Science": {
        "photosynthesis": "🌿 Process plants use to convert sunlight into energy.",
        "cryptography": "🔐 The study of secure communication techniques."
    },
    "Culture": {
        "architecture": "🏛️ The art and science of designing buildings.",
        "philosophy": "🤔 The study of fundamental questions about existence and knowledge."
    },
    "Books": {
        "encyclopedia": "📚 A book or resource with detailed information on many topics."
    }
}

def print_hangman(attempts):
    """Display hangman status based on remaining attempts using emojis."""
    stages = {
        6: "\n 😁 (All good!)",
        5: "\n 🙂 (Keep it up!)",
        4: "\n 😐 (Stay focused!)",
        3: "\n 😟 (Be cautious!)",
        2: "\n 😰 (Almost out!)",
        1: "\n 😨 (Last chance!)",
        0: "\n 💀 (Game Over!)"
    }
    print(f"\n Status: {stages[attempts]}")

# Let the player choose a category
print("\n 🎮 Hangman Challenge: Choose your category!")
print("\n 📂 Categories: " + ", ".join(categories.keys()))
selected_category = input("\n 🔤 Enter a category: ").strip().capitalize()

# Validate category
if selected_category not in categories:
    print(f"\n ⚠️ Invalid category. Defaulting to 'Science'.")
    selected_category = "Science"

# Select random word and hint from the chosen category
word, hint = random.choice(list(categories[selected_category].items()))
guessed = []  # Letters that have been guessed
attempts = 6  # Total attempts

# Intro message
print(f"\n🎯 Category: {selected_category}")
print(f"\n💡 Hint: {hint}")
print("\n Word: " + " ".join("_" for _ in word))
print_hangman(attempts)
print("\n Guessed letters: None\n")

# Main game loop
while attempts > 0:
    guess = input("\n🔤 Enter a letter: ").lower()

    if guess in guessed or len(guess) != 1 or not guess.isalpha():
        print("\n⚠️ Invalid or repeated guess. Try a different letter.\n")
        continue

    guessed.append(guess)

    if guess not in word:
        attempts -= 1
        print(f"\n❌ Oops! '{guess}' is not in the word. Attempts left: {attempts}\n")
    else:
        print(f"\n✅ Good job! '{guess}' is in the word!\n")

    # Update display with guessed letters
    display = " ".join([letter if letter in guessed else "_" for letter in word])
    print("\n Word: " + display)
    print_hangman(attempts)
    print("\n Guessed letters: " + ", ".join(guessed) + "\n")

    # Check if the word is completely guessed
    if "_" not in display.replace(" ", ""):
        print(f"\n🏆 Congrats! You guessed the word '{word}' correctly! 🎉")
        break

# If attempts run out
if "_" in display.replace(" ", ""):
    print(f"\n💀 Game over! The word was '{word}'. Better luck next time! 🔄")

# End message
print("\n👋 Thanks for playing Hangman 💖 See you next time! 😊\n")

# --------------  FINALLY GAME OVER  --------------
# --------------  THANK YOU  --------------