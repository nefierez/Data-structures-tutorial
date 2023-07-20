# Stacks
A stack is a data structure that can be implemented using lists. It serves various purposes and operates based on a specific order for adding and removing elements. This order is commonly referred to as "Last In, First Out" (LIFO), which means that the last item or element added to the stack will be the first one to be removed.

## Stacks in Python
In Python, we can represent a stack using a list. To add an item to the top of the stack, we can use the append() function on the list. Similarly, to remove items from the top of the stack, we can use the pop() function, which not only removes the item but also deletes it from the list. The size of the stack can be determined by using the len() function on the list. It's important to note that the performance of the stack implemented with a Python list relies on the performance of the underlying dynamic array.

It is important to remember that the front of the stack is where the first item of the stack is found, typically located at index 0     of a dynamic array. The back of the stack refers to the end of the dynamic array, where push and pop operations occur.

| Common Stack Operation | Description | Python Code | Performance |
|-----------------------|-------------|-------------|-------------|
| push(value)           | Adds "value" to the back of the stack. | `my_stack.append(value)` | O(1) - Performance of adding to the end of a dynamic array |
| pop()                 | Removes and returns the item from the back of the stack. | `value = my_stack.pop()` | O(1) - Performance of removing from the end of a dynamic array |
| size()                | Return the size of the stack. | `length = len(my_stack)` | O(1) - Performance of returning the size of the dynamic array |
| empty()               | Returns true if the length of the stack is zero. | `if len(my_stack) == 0:` | O(1) - Performance of checking the size of the dynamic array |


## Basic Operations on Stacks

### 1. The Stack of Books on a Desk
If you were to ask your friends and family to borrow their favorite books, you would probably receive a couple of books to read. Imagine that every time a friend or family member gives you a book, you put it on your desk, creating a stack of books. The last book handed to you is placed on the top of the pile, making it the first book ready to be grabbed. When you add a book to the stack, you use the `push` operation, as we would say in programming. The `push` operation adds the item to the back of the stack and makes it the first book you can take or remove from the stack using the `pop` operation. The `pop` operation not only removes the last item from the stack, but also returns its value if you need to store it.

![Stack of Books](Stacks.jpg)

To illustrate this, we have created a class called **Stack_of_Books**. The class creates an empty array and includes three functions: *push, pop, and is_empty.*

```python
class Stack_of_Books:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0
```

### Push Operations
To add items (books) to the stack of books, we use the push operation.

```python

# Example usage
stack = Stack_of_Books()
stack.push("Don Quixote")
stack.push("One Hundred Years of Solitude")
stack.push("Invisible Man")
stack.push("Beloved")
stack.push("A Passage to India")

# Print the current stack
print("Current stack:", stack.stack)
# Expected output: Current stack: ['Don Quixote', 'One Hundred Years of Solitude', 'Invisible Man', 'Beloved', 'A Passage to India']
```

In the example above, we create a new instance of the `Stack_of_Books` class called `stack`. We then use the push method to add multiple books to the stack. Finally, we print the current contents of the stack using `stack.stack` to display the updated stack.


### Pop Operations
To remove items (books) from the stack of books, we use the `pop` operation.


```python
# Example usage
print("Removed book:", stack.pop())
# Expected output: Removed book: Beloved

print("Removed book:", stack.pop())
# Expected output: Removed book: Invisible Man

print("Removed book:", stack.pop())
# Expected output: Removed book: One Hundred Years of Solitude

# Print the updated stack
print("Updated stack:", stack.stack)
# Expected output: Updated stack: ['Don Quixote']
```

In this version, the print statements directly use `stack.pop()` to both remove the book from the stack and print it in the same line. Each line performs the removal and prints the removed book individually. Finally, we print the updated contents of the stack using `stack.stack`, which should now only contain the book "Don Quixote".


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
class BrowserTabTracker:
    def __init__(self):
        self.tab_stack = []

    def open_tab(self, url):
        self.tab_stack.push(url)

    def close_tab(self):
        if not self.is_empty():
            return self.tab_stack.pop()
        else:
            return "No tabs to close"

    def view_current_tab(self):
        if not self.is_empty():
            return self.tab_stack[-1]
        else:
            return "No tabs to view"

    def check_if_tabs_open(self):
        return not self.is_empty()

    def view_all_tabs(self):
        pass

    def is_empty(self):
        return len(self.tab_stack) == 0
```

### Test 1:
* Open three tabs
* View the current tab
* Close the current tab
* Check if tabs are open

### Test 2:
* Open two tabs
* View all tabs
* Close the current tab
* Check if tabs are open

You can check your code with the solution here: [Solution](stacks.py)