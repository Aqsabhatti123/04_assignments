# PROJECT 4 ASSIGNMENTS 

# AUTHOR : Aqsa Vhatti

# ASSIGNMENTS 01

# 02_intermediate

# Control Flow for Console

# PROBLEM STATEMENT

# High Low

# We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

# Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!

# You make a guess, saying your number is either higher than or lower than the computer's number

# If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!

# These steps make up one round of the game. The game is over after all rounds have been played.

# We've provided a sample run below.

# SOLUTION :

import random

NUM_ROUNDS = 5  # Number of rounds to play

def game():
    """
    🎮 A fun High-Low game where players guess if their random number is 
    higher or lower than the computer's number.
    """
    SCORE = 0  # Initialize score

    print(f"\n 🎉 Welcome to the High-Low Game! 🌟")
    print(f"\n 🤔 Can you guess if your number is higher or lower than mine? Let's find out! 🚀")
    print(f'\n -----------------------------------')

    # Play multiple rounds
    for round_num in range(NUM_ROUNDS):
        # Generate random numbers
        computer = random.randint(0, 99)
        user = random.randint(0, 99)

        # Announce the round
        print(f"\n🌟 Round {round_num + 1}!")
        print(f"\n 🤖 Your random number is: {user}")

        # Get user's guess
        user_input = input(f"\n 💬 Do you think your number is higher or lower than the computer's? (Type 'higher' or 'lower'): ").lower().strip()

        # Evaluate the guess
        if user_input == "higher":
            if user > computer:
                print(f"\n ✅ You were right! 🎯 The computer's number was {computer}.")
                SCORE += 1  # Increase score
            else:
                print(f"\n ❌ Aww, that's incorrect. The computer's number was {computer}.")
        elif user_input == "lower":
            if user < computer:
                print(f"\n ✅ You were right! 🎯 The computer's number was {computer}.")
                SCORE += 1  # Increase score
            else:
                print(f"\n ❌ Aww, that's incorrect. The computer's number was {computer}.")
        else:
            print(f"\n ⚠️ Invalid input! Please enter 'higher' or 'lower'. No points this round. 😅")

        print(f"\n 📊 Your current score is: {SCORE}")

    # Game over and final score
    print(f"\n🎮 Game over! Your total score is: 🎉", SCORE)

    # Conditional ending messages based on performance
    if SCORE == 3:
        print(f"🌟 Wow! You played perfectly! 🏆")
    elif SCORE == 2:
        print(f"\n 👏 Good job! You played really well!")
    else:
        print(f"\n 👍 Better luck next time! Keep practicing! 🌈")

if __name__ == "__main__":
    game()

# --------------------- END OF CODE ---------------------
