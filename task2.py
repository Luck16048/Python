class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self):
        if self.head:
            self.head = self.head.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def count(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

def main():
    ll = LinkedList()
    ll.add(10)
    ll.add(20)
    ll.add(30)
    print("Elementy listy:")
    ll.display()
    print(f'Liczba elementów: {ll.count()}')
    ll.remove()
    print("Po usunięciu elementu z początku:")
    ll.display()

if __name__ == "__main__":
    main()
