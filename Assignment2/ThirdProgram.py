# Nested Interactive Loop
def convert_heights_nested(heights_inches):
    heights_centimeters = []
    for height in heights_inches:
        centimeters = height * 2.54
        heights_centimeters.append(round(centimeters, 2))
    return heights_centimeters

# List Comprehension
def convert_heights_list_comprehension(heights_inches):
    return [round(height * 2.54, 2) for height in heights_inches]

def main():
    # Input heights in inches from the user
    heights_inches = []
    num_customers = int(input("Enter the number of customers: "))

    for i in range(num_customers):
        height = float(input(f"Enter height (in inches) for customer {i + 1}: "))
        heights_inches.append(height)

    # Convert heights using nested interactive loop
    heights_cm_nested = convert_heights_nested(heights_inches)

    # Convert heights using list comprehension
    heights_cm_comprehension = convert_heights_list_comprehension(heights_inches)

    # Display the results
    print("Input Heights (in inches):", heights_inches)
    print("Heights Converted using Nested Loop:", heights_cm_nested)
    print("Heights Converted using List Comprehension:", heights_cm_comprehension)

if __name__ == "__main__":
    main()
