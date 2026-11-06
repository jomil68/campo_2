"""
Assessment 3.2 - Linear Data Structure: LINKED LIST (Singly)
Author: Jomil Campo
Dynamic version of the Assessment 3.1 linked list algorithm.
Inserts every letter of the entered name at the tail, then deletes the head
node until the list is empty.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def show(head):
    parts = []
    temp = head
    while temp is not None:
        parts.append(temp.data)
        temp = temp.next
    parts.append("NULL")
    return " -> ".join(parts)


def run_linked_list(name):
    head = None

    print("\n--- ADD (insert at tail) ---")
    for letter in name:
        new_node = Node(letter)
        if head is None:
            head = new_node
        else:
            temp = head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        print(f"Inserted '{letter}'  ->  {show(head)}")

    print("\n--- REMOVE (delete head) ---")
    while head is not None:
        deleted = head.data
        head = head.next
        print(f"Deleted: {deleted}  ->  {show(head)}")

    print("\nLinked list is empty")


def main():
    print("=== LINKED LIST ===")
    while True:
        name = input("\nEnter a name (or 'q' to quit): ").replace(" ", "")
        if name.lower() == "q":
            print("Goodbye!")
            break
        if not name:
            print("Please enter at least one letter.")
            continue
        run_linked_list(name.upper())


if __name__ == "__main__":
    main()
