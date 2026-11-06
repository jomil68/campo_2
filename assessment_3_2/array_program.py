"""
Assessment 3.2 - Linear Data Structure: ARRAY
Author: Jomil Campo
Dynamic version of the Assessment 3.1 array algorithm.
Adds every letter of the entered name, then removes them from the last index.
"""


def run_array(name):
    A = [None] * len(name)          # Create array A of size = length of name
    size = 0

    print("\n--- ADD ---")
    for i in range(len(name)):
        A[i] = name[i]
        size += 1
        print(f"Added '{name[i]}' at index {i}  ->  {A}")

    print("\n--- REMOVE ---")
    while size > 0:
        removed = A[size - 1]
        A[size - 1] = None
        size -= 1
        print(f"Removed: {removed}  ->  {A}")

    print("\nArray is empty")


def main():
    print("=== ARRAY ===")
    while True:
        name = input("\nEnter a name (or 'q' to quit): ").replace(" ", "")
        if name.lower() == "q":
            print("Goodbye!")
            break
        if not name:
            print("Please enter at least one letter.")
            continue
        run_array(name.upper())


if __name__ == "__main__":
    main()
