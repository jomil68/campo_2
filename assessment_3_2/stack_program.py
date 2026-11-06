"""
Assessment 3.2 - Linear Data Structure: STACK (LIFO)
Author: Jomil Campo
Dynamic version of the Assessment 3.1 stack algorithm.
PUSH every letter of the entered name, then POP until the stack is empty.
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return "[" + ", ".join(self.items) + "]  (top is right)"


def run_stack(name):
    S = Stack()

    print("\n--- ADD (PUSH) ---")
    for letter in name:
        S.push(letter)
        print(f"Pushed '{letter}'  ->  {S}")

    print("\n--- REMOVE (POP) ---")
    while not S.is_empty():
        popped = S.pop()
        print(f"Popped: {popped}  ->  {S}")

    print("\nStack is empty")


def main():
    print("=== STACK (LIFO) ===")
    while True:
        name = input("\nEnter a name (or 'q' to quit): ").replace(" ", "")
        if name.lower() == "q":
            print("Goodbye!")
            break
        if not name:
            print("Please enter at least one letter.")
            continue
        run_stack(name.upper())


if __name__ == "__main__":
    main()
