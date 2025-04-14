import random

print("🔐 Welcome to the Random Password Generator")

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"

try:
    num_passwords = int(input("📌 Enter the number of passwords to generate: "))
    password_length = int(input("📏 Enter the length of each password: "))

    print("\nHere are your secure passwords:\n")

    for _ in range(num_passwords):
        password = ''.join(random.choice(chars) for _ in range(password_length))
        print(f"🔑 {password}")

except ValueError:
    print("❌ Please enter valid numeric values for amount and length.")