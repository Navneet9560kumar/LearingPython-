# Mutable 

ingredients = ["water","Milk","black tea"]

ingredients.append("sugar")
print(f"Ingredients are : {ingredients}")
ingredients.remove("water")

print(f"Ingredients are : {ingredients}")

spice_options = ["ginger","cardamom"]
chai_ingredients = ["water","milke"]

print(f"chai:{chai_ingredients}")



# 1. Basic Adding/Modifying Methods
# append(x) → Add single element x at the end

# extend(iterable) → Add all elements from another iterable (list, tuple, etc.)

# insert(i, x) → Insert element x at index i


# 📌 2. Removing Elements
# remove(x) → Remove first occurrence of element x

# pop([i]) → Remove and return element at index i (default: last)

# clear() → Remove all elements from list

# 📌 3. Searching/Counting
# index(x[, start[, end]]) → Return index of first occurrence of x

# count(x) → Return number of times x appears in the list

# 📌 4. Sorting and Reversing
# sort() → Sort the list in ascending order
# (use sort(reverse=True) for descending)

# reverse() → Reverse the order of elements in the list

# 📌 5. Copying
# copy() → Returns a shallow copy of the list


#  Built-in Functions & Operators with Lists
# len(lst) → Returns number of elements

# max(lst) / min(lst) → Return largest/smallest value

# sum(lst) → Sum of numeric values

# sorted(lst) → Return new sorted list (original list unchanged)

# list(iterable) → Convert iterable to list

# x in lst → Check if x exists in list

# lst1 + lst2 → Concatenate two lists

# lst * 3 → Repeat list 3 times

# lst[start:stop:step] → Slicing