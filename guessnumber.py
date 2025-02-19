import random

def guess_the_number():
    print("🎯 Welcome to Guess The Number Game!")
    print("I have chosen a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)  # Generate a random number
    attempts = 7  # Number of allowed attempts

    while attempts > 0:
        try:
            guess = int(input(f"\nYou have {attempts} attempts left. Enter your guess: "))

            if guess < 1 or guess > 100:
                print("⚠️ Please enter a number between 1 and 100.")
                continue

            if guess < secret_number:
                print("📉 Too low! Try again.")
            elif guess > secret_number:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number {secret_number} correctly! 🎊")
                return

            attempts -= 1  # Reduce attempts after each incorrect guess

        except ValueError:
            print("❌ Invalid input! Please enter a numeric value.")

    print(f"😢 Game over! The correct number was {secret_number}.")

if __name__ == "__main__":
    guess_the_number()
