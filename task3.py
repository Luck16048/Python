class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, customer):
        self.queue.append(customer)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)

    def display(self):
        print("Aktualna zawartość kolejki:", self.queue)

def main():
    queue = Queue()
    queue.enqueue('Klient 1')
    queue.enqueue('Klient 2')
    queue.enqueue('Klient 3')
    queue.display()
    queue.dequeue()
    print("Po obsłużeniu klienta:")
    queue.display()

if __name__ == "__main__":
    main()
