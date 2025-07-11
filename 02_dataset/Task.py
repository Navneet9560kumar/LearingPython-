# Create a grocery list
my_cart = ["apples", "bananas", "milk"]

# Print the grocery list
print("Initial cart:", my_cart)

# Add "bread" to the end of the list
my_cart.append("bread")
print("After adding bread:", my_cart)

# Insert "ketchup" at the beginning
my_cart.insert(0, "ketchup")
print("After inserting ketchup at beginning:", my_cart)

# Remove "bananas" from the list
my_cart.remove("bananas")
print("After removing bananas:", my_cart)

# Remove the last item and store in variable
removed_item = my_cart.pop()
print("Removed item:", removed_item)

# Extend the list with "rice" and "butter"
my_cart.extend(["rice", "butter"])
print("After extending with rice and butter:", my_cart)

# Sort the grocery list alphabetically
my_cart.sort()
print("After sorting:", my_cart)

# Reverse the order of the list
my_cart.reverse()
print("After reversing:", my_cart)

# Concatenate with another list ["juice", "jam"]
new_cart = my_cart + ["juice", "jam"]
print("After concatenating juice and jam:", new_cart)

# Duplicate the grocery list twice
duplicated_cart = my_cart * 2
print("Duplicated cart:", duplicated_cart)

# Convert string "tomato cucumber spinach" into list
veggies_str = "tomato cucumber spinach"
veggies_list = veggies_str.split()
print("Converted veggie list:", veggies_list)
