class BrowserTabTracker:
    def __init__(self):
        self.tab_stack = []

    def open_tab(self, url):
        self.tab_stack.append(url)

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
        return self.tab_stack

    def is_empty(self):
        return len(self.tab_stack) == 0


# Example usage
tracker = BrowserTabTracker()

# Test 1
print("Test 1")
tracker.open_tab("https://www.gmail.com")
tracker.open_tab("https://www.facebook.com")
tracker.open_tab("https://www.byui.edu")
print("Current tab:", tracker.view_current_tab())  # Expected output: Current tab: https://www.byui.edu
print("Closed tab:", tracker.close_tab())  # Expected output: Closed tab: https://www.byui.edu
print("Tabs open?", tracker.check_if_tabs_open())  # Expected output: Tabs open? True

# Test 2
print("Test 2")
tracker.open_tab("https://www.amazon.com")
tracker.open_tab("https://www.github.com")
print("All tabs:", tracker.view_all_tabs())  # Expected output: All tabs: ['https://www.gmail.com', 'https://www.facebook.com', 'https://www.amazon.com', 'https://www.github.com']
print("Closed tab:", tracker.close_tab())  # Expected output: Closed tab: https://www.github.com
