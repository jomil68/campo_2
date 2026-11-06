"""
Assessment 3.2 - Linear Data Structure: QUEUE (FIFO)
Author: Jomil Campo
Dynamic version of the Assessment 3.1 queue algorithm.
ENQUEUE every letter of the entered name, then DEQUEUE until the queue is empty.
"""


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)          # add at the rear

    def dequeue(self):
        return self.items.pop(0)         # remove from the front

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return "front [" + ", ".join(self.items) + "] rear"


def run_queue(name):
    Q = Queue()

    print("\n--- ADD (ENQUEUE) ---")
    for letter in name:
        Q.enqueue(letter)
        print(f"Enqueued '{letter}'  ->  {Q}")

    print("\n--- REMOVE (DEQUEUE) ---")
    while not Q.is_empty():
        removed = Q.dequeue()
        print(f"Dequeued: {removed}  ->  {Q}")

    print("\nQueue is empty")


def main():
    print("=== QUEUE (FIFO) ===")
    while True:
        name = input("\nEnter a name (or 'q' to quit): ").replace(" ", "")
        if name.lower() == "q":
            print("Goodbye!")
            break
        if not name:
            print("Please enter at least one letter.")
            continue
        run_queue(name.upper())


if __name__ == "__main__":
    main()
