import random

def roll_dice(num_dice, num_sides):
    """Simulate rolling dice and return the results as a list"""
    return [random.randint(1, num_sides) for _ in range(num_dice)]

def main():
    print("🎲 Welcome to the Dice Roll Simulator!")

    # Get user input
    num_dice = int(input("Enter the number of dice: "))
    num_sides = int(input("Enter the number of sides per dice (e.g., 6 for standard dice): "))

    # Validate input
    if num_dice <= 0 or num_sides <= 0:
        print("❌ Invalid input! Number of dice and sides must be greater than 0.")
        return

    # Roll the dice
    results = roll_dice(num_dice, num_sides)

    # Display results
    print(f"\n🎲 You rolled {num_dice} dice with {num_sides} sides each!")
    print("Results:", results)
    print(f"Total Sum: {sum(results)}")

    # Ask user if they want to roll again
    while input("\nRoll again? (yes/no): ").strip().lower() == "yes":
        results = roll_dice(num_dice, num_sides)
        print("\nNew Roll:", results)
        print(f"Total Sum: {sum(results)}")

if __name__ == "__main__":
    main()
