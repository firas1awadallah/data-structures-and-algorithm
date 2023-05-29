class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty.")

    def is_empty(self):
        return len(self.items) == 0


class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def print_stack1(self):
        elements = "->".join(str(item) for item in self.stack1.items[::-1])
        print("Stack1:", elements)

    def enqueue(self, value):
        # Push the value into stack1
        self.stack1.push(value)

    def dequeue(self):
        if self.stack1.is_empty() and self.stack2.is_empty():
            raise IndexError("PseudoQueue is empty.")

        if self.stack2.is_empty():
            # Move all elements from stack1 to stack2
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

        # Pop the top element from stack2
        self.stack2.pop()

        # Move all elements from stack2 to stack1
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())

        return self.stack1



queue = PseudoQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.print_stack1() 
queue.enqueue(3)
queue.print_stack1() 
queue.enqueue(4)
queue.print_stack1() 
queue.dequeue()
queue.print_stack1()  
queue.dequeue()
queue.print_stack1() 




