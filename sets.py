fruits = {"apple", "lemon", "orange", "grape", "mango", "tomato"}
vegetables = {"carrot", "tomato", "broccoli", "potato", "cabbage", "lemon"}

# Test Scenario 1: Add a new fruit
fruits.add("strawberry")
print("Test #1")
print("Fruits (after adding strawberry):", fruits) # Expected output: Fruits (after adding strawberry): {'grape', 'orange', 'apple', 'tomato', 'mango', 'lemon', 'strawberry'}

# Test Scenario 2: Delete a vegetable
vegetables.remove("broccoli")
print("Test #2")
print("Vegetables (after removing broccoli):", vegetables)  # Expected output: Vegetables (after removing broccoli): {'carrot', 'tomato', 'potato', 'cabbage', 'lemon'}

# Test Scenario 3: Update a fruit
fruits.remove("grape")
fruits.add("pineapple")
print("Test #3")
print("Fruits (after updating grape to pineapple):", fruits)  # Expected output: Fruits (after updating grape to pineapple): {'apple', 'orange', 'mango', 'tomato', 'pineapple', 'lemon', 'strawberry'}

# Test Scenario 4: Union of fruits and vegetables
combined_set = fruits.union(vegetables)
print("Test #4")
print("Combined Set (union of fruits and vegetables):", combined_set)  # Expected output: Combined Set (union of fruits and vegetables): {'apple', 'orange', 'mango', 'carrot', 'cabbage', 'strawberry', 'tomato', 'lemon', 'potato'}

# Test Scenario 5: Difference between fruits and vegetables
fruits_only = fruits.difference(vegetables)
print("Test #5")
print("Fruits Only (difference between fruits and vegetables):", fruits_only)  # Expected output: Fruits Only (difference between fruits and vegetables): {'orange', 'mango', 'strawberry', 'pineapple'}

# Test Scenario 6: Intersection of fruits and vegetables
common_items = fruits.intersection(vegetables)
print("Test #6")
print("Common Items (intersection of fruits and vegetables):", common_items)  # Expected output: Common Items (intersection of fruits and vegetables): {'lemon', 'tomato'}

# Test Scenario 7: Check if a specific fruit is present
is_mango_present = "mango" in fruits
print("Test #7")
print("Is Mango Present in Fruits:", is_mango_present)  # Expected output: Is Mango Present in Fruits: True
