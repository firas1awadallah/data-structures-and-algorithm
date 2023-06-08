class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        """
        Adds a new element to the top of the stack.

        Args:
            value: The value to be pushed onto the stack.
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """
        Removes and returns the element from the top of the stack.

        Returns:
            The value of the popped element.
        
        Raises:
            Exception: If the stack is empty.
        """
        if self.top is None:
            raise Exception("empty stack")
        else:
            temp = self.top.value
            self.top = self.top.next
            return temp
        
    def peek(self):
        """
        Returns the value of the element at the top of the stack without removing it.

        Returns:
            The value of the top element.
        
        Raises:
            Exception: If the stack is empty.
        """
        if self.top is None:
            raise Exception("empty stack")
        else:
            return self.top.value

    def getMax(self):
        stack1 = stack()
        biggest = None
        while self.top is not None:
            if biggest is None or self.top.value > biggest:
                biggest = self.top.value
            stack1.push(self.pop())
        while stack1.top :
            self.push(stack1.pop())
        print(self)
        return biggest
    

    def __str__(self):
        current= self.top
        stack = ""
        while current:
            stack += f"{current.value} -> "
            current = current.next
        return stack + "None"

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        if self.top is None:
            return True
        else:
            return False
        
    
if __name__ == "__main__":
    s = stack()
    s.push(111)
    s.push(22)
    s.push(6)
    print(s)
    # print(s.peek())
    # print(s.pop())
    # print(s.pop())
    # print(s.pop())
    # print(s.is_empty())
    print(s.getMax())
    


        # python Stack/stack/stack.py
        # pytest Stack/tests/test_stack.py