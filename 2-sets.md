# Sets
A set is a built-in data structure in Python that can be implemented using the `set()` function or by enclosing elements within curly braces `{}`. Unlike lists, sets do not maintain a specific order for their elements. This means that the items in a set can appear in a random order. Additionally, sets do not allow duplicate elements, making them highly efficient for checking membership or determining unique values within a collection.

Consider the following example:

```Python
# Creating a set
set_of_numbers = {10, 20, 30, 30, 40, 50}

print(set_of_numbers)
```

Output:
```Python
{10, 20, 30, 40, 50}
```

In the example above, we create a set called `set_of_numbers` using curly braces and assign it a collection of elements, including duplicates. However, when we print the set, we observe that the duplicate elements have been automatically removed, resulting in a set with unique values.

Sets provide useful operations such as checking membership, performing set operations (union, intersection, difference), and testing for subsets and supersets. They are particularly effective when there is a need to quickly determine whether an item exists in a collection without concern for order or duplicates.


## Sets in Python
In Python, we can work with sets to perform various operations. Sets allow us to add elements, remove elements, and check for membership. Additionally, sets support other mathematical operations such as intersection, union, and set difference.

| Common Set Operation | Description                           | Python Code               | Performance                                                |
|----------------------|---------------------------------------|---------------------------|------------------------------------------------------------|
| add(value)           | Adds "value" to the set               | `my_set.add(value)`       | O(1) - Performance of hashing the value (assuming good conflict resolution) |
| remove(value)        | Removes the "value" from the set       | `my_set.remove(value)`    | O(1) - Performance of hashing the value (assuming good conflict resolution) |
| member(value)        | Determines if "value" is in the set    | `if value in my_set:`     | O(1) - Performance of hashing the value (assuming good conflict resolution) |
| size()               | Returns the number of items in the set | `length = len(my_set)`    | O(1) - Performance of returning the size of the set         |


## Basic Mathematical Operations on Sets

Let's imagine you're working in a school district and you need to perform some statistics about the school teachers who are married and are younger than 30 years old. You have two sets where you can find this data.

```python
married_teachers = {"Cherryl Turner", "Tyson Tripp", "Julitta Reid", "Aura Myrtie", "Frank Lavern"}

younger_than_30_teachers = {"Aura Myrtie", "Frank Lavern", "Carolyn Macy", "Roy Dashiell", "Peter Antony"}
```

### **Intersection: Teachers who are Married and Younger than 30**

To find the teachers who are both married and younger than 30, you can use the intersection operation. This will give you a new set containing only the elements that are present in both sets.

```python
# Intersection using the "intersection" method
intersection_set_1 = married_teachers.intersection(younger_than_30_teachers)

# Alternative way using the built-in "intersection" function
intersection_set_2 = intersection(married_teachers, younger_than_30_teachers)

print("Teachers who are married and younger than 30 (Method 1):", intersection_set_1)
print("Teachers who are married and younger than 30 (Method 2):", intersection_set_2)
# Expected output: Teachers who are married and younger than 30 (Method 1): {'Frank Lavern', 'Aura Myrtie'}
#                  Teachers who are married and younger than 30 (Method 2): {'Frank Lavern', 'Aura Myrtie'}
```

In the example above, we first use the `intersection` method on the `married_teachers` set, passing `younger_than_30_teachers` as the argument. This gives us `intersection_set_1`. We then use the alternative method by directly calling the `intersection` function, passing the two sets as arguments, which gives us `intersection_set_2`. Both sets contain the teachers who satisfy both conditions.

### **Union: Combined Set of Teachers**

To create a set that combines both groups of teachers, including any duplicates, you can use the union operation. This operation will give you a new set containing all the unique elements from both sets.

```python
# Union using the "union" method
union_set_1 = married_teachers.union(younger_than_30_teachers)

# Alternative way using the built-in "|" operator
union_set_2 = married_teachers | younger_than_30_teachers

print("Combined set of teachers (Method 1):", union_set_1)
print("Combined set of teachers (Method 2):", union_set_2)
# Expected output: Combined set of teachers (Method 1): {'Roy Dashiell', 'Julitta Reid', 'Peter Antony', 'Cherryl Turner', 'Frank Lavern', 'Aura Myrtie', 'Tyson Tripp', 'Carolyn Macy'}
# Expected output: Combined set of teachers (Method 2): {'Roy Dashiell', 'Julitta Reid', 'Peter Antony', 'Cherryl Turner', 'Frank Lavern', 'Aura Myrtie', 'Tyson Tripp', 'Carolyn Macy'}
```
In the example above, we first use the `union` method on the `married_teachers set`, passing `younger_than_30_teachers` as the argument. This gives us `union_set_1`. We then use the alternative method by using the `|` operator between the two sets, which gives us `union_set_2`. Both sets contain all the teachers from both sets without any duplicates.

### **Difference: Teachers who are Married but Not Younger than 30**

To find the teachers who are married but not younger than 30, you can use the difference operation. This will give you a new set containing the elements that are present in the first set but not in the second set.

```python
# Difference using the "difference" method
difference_set = married_teachers.difference(younger_than_30_teachers)

print("Teachers who are married but not younger than 30:", difference_set)
# Expected output: Teachers who are married but not younger than 30: {'Cherryl Turner', 'Tyson Tripp', 'Julitta Reid'}
```
In the example above, we use the `difference` method on the `married_teachers` set, passing `younger_than_30_teachers` as the argument. The resulting set contains the teachers who are married but not younger than 30.

## Problem to Solve: Browser Tab Tracker
Complete the Browser Tab Tracker and write two test scenarios.

The program should support the following operations:

* **Open a New Tab:** Add a new tab to the stack of browser tabs.
* **Close the Current Tab:** Remove and display the URL of the current tab from the stack.
* **View the Current Tab:** Display the URL of the current tab without removing it from the stack.
* **Check if Tabs are Open:** Check if there are any tabs open in the stack.
* **View All Tabs:** Display all the URLs of the tabs in the stack without removing them.

The program should use the following stack operations:

* **Push:** Add an item to the top of the stack.
* **Pop:** Remove and retrieve the item from the top of the stack.
* **Peek:** Retrieve the item from the top of the stack without removing it.
* **isEmpty:** Check if the stack is empty.


### Tasks
* Fix the `open_tab` function
* Implement the `view_all_tabs` function

``` python

```

### Test 1:
* 
* 
* 
* 

### Test 2:
* 
* 
* 
* 

You can check your code with the solution here: [Solution](sets.py)