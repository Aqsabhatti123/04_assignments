# Rock, paper, scissors Python Project

import random

def play():
    while True:
        user = input("Whats your choice? 'r' for rock, 'p' for paper, 's' for scissors \n ").lower()
        if user not in ["r", "p", "s"]:
            print("⚠️ Invalid choice! Please choose 'r', 'p', or 's'.")
            continue

        computer = random.choice(["r","p","s"])
        print(f"🤖 Computer chose: {computer.upper()}")
        if user == computer:
            print("😐 It's a tie! Try again.")
            continue  # Phir se game start hoga

        
        if is_win(user, computer):
            print("🎉 You Won!")
        else:
            print("💀 You Lose!")
            
        again = input("\n🔄 Play again? (y/n): ").lower()
        if again != "y":
            print("👋 Thanks for playing! Goodbye.")
            break

def is_win(player, opponent):
    # r > s, s > p, p > r
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True
    
if __name__ == "__main__":
     play()