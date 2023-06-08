class Node:
    def __init__(self, value):
        """
        Initialize a new Node object.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        """
        Initialize a new Stack object.
        """
        self.top = None

    def push(self, value):
        """
        Push a value onto the stack.

        Args:
            value: The value to be pushed onto the stack.
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """
        Pop the top value from the stack and return it.

        Returns:
            The value that was popped from the stack.

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
        Get the value at the top of the stack without removing it.

        Returns:
            The value at the top of the stack.

        Raises:
            Exception: If the stack is empty.
        """
        if self.top is None:
            raise Exception("empty stack")
        else:
            return self.top.value

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        if self.top is None:
            return True
        else:
            return False


def validate_brackets(string):
    """
    Validate if a string contains balanced brackets.

    Args:
        string: The string to be validated.

    Returns:
        True if the string has balanced brackets, False otherwise.
    """
    stack = Stack()
    brackets = {"(": ")", "{": "}", "[": "]"}

    for char in string:
        if char in brackets.keys():
            stack.push(char)
        elif char in brackets.values():
            if not stack:
                return False
            if char != brackets[stack.pop()]:
                return False

    return True if stack.is_empty() else False

str1 = "{}(){}"  
print(validate_brackets(str1))  

str2 = "{}{Code}[Fellows](())" 
print(validate_brackets(str2))  

str3 = "{(})"  
print(validate_brackets(str3))  

str4 = "[{[(]"
print(validate_brackets(str4))  
