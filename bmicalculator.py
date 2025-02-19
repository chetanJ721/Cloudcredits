def calculate_bmi(weight, height):
    """Calculate BMI using the formula: BMI = weight / height²"""
    return weight / (height ** 2)

def get_bmi_category(bmi):
    """Determine the BMI category based on BMI value"""
    if bmi < 18.5:
        return "Underweight 😕"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight ✅"
    elif 25 <= bmi < 29.9:
        return "Overweight ⚠️"
    else:
        return "Obese ❌"

def main():
    print("⚖️ Welcome to the BMI Calculator!")

    # Get weight input
    weight = float(input("Enter your weight (in kg): "))

    # Get height input
    height_unit = input("Are you entering height in meters (m) or feet (ft)? ").strip().lower()
    
    if height_unit == "m":
        height = float(input("Enter your height in meters: "))
    elif height_unit == "ft":
        feet = int(input("Enter feet: "))
        inches = int(input("Enter inches: "))
        height = (feet * 0.3048) + (inches * 0.0254)  # Convert feet/inches to meters
    else:
        print("❌ Invalid height unit! Please enter 'm' for meters or 'ft' for feet.")
        return

    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    # Display results
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()
