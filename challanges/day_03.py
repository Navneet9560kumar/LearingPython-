def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number.")

# Get number of people
num_people = int(input("How many people are there in the group? "))
names = []

# Collect names
for i in range(num_people):
    person_name = input(f"Enter the name of person #{i+1}: ").strip()
    names.append(person_name)

# Get bill amount
total_bill = get_float("Enter the total bill amount (numbers only): ")

# Calculate per-person share
share = round(total_bill / num_people, 2)

# Output
print("\n" + "*" * 40)
print(f"Total Bill: ₹{total_bill}")
print(f"Each person owes: ₹{share}")
print("-" * 40)

for name in names:
    print(f"{name} owes ₹{share}")

print("*" * 40)
