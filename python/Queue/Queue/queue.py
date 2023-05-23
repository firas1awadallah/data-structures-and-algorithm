class Node:
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self,front=None,back=None):
        self.front = front # first node in th queue
        self.back = back    # last node in queue
    def enqueue(self,value) :
        """
        Adds a new element to the back of the queue.

        Args:
            value: The value to be enqueued.
        """
        node = Node(value)
        #check if queue is empty:
        if self.front == None:
            self.front = node
            self.back = node
        else:
            self.back.next = node
            self.back = node
      
    def dequeue(self):
        """
        Removes and returns the front element from the queue.

        Returns:
            The value of the dequeued element.
        
        Raises:
            Exception: If the queue is empty.
        """
        if self.front == None:
            raise Exception('Empty Queue')
        else:
            temp = self.front
            self.front = self.front.next
            return temp.value
        
    def peek(self):
        """
        Returns the value of the front element without removing it.

        Returns:
            The value of the front element.
        
        Raises:
            Exception: If the queue is empty.
        """
        if self.front == None:
            raise Exception('Empty Queue')
        
        else:
            return self.front.value
        
    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        if self.front == None:
            return True
        else:
            return False

    def __str__(self):
        """
        Returns a string representation of the queue.

        Returns:
            A string representing the elements of the queue.
        """
        current=self.front
        string=""
        while current:
            string+=f"{current.value}"
            string+=" -> "
            current=current.next
        return string + "None"
    
if __name__ == "__main__":
    q=Queue()
    q.enqueue("hi")
    q.enqueue("welcome")
    q.enqueue("bye")
    print(q)
    print(q.front.value)
    print(q.back.value)
    print("deleted element is ",q.dequeue())#deleted node value
    print(q)

    # python Queue/Queue/queue.py
    # pytest Queue/tests/test_queue.py 