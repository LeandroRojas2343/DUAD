# Node class template 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Define the Stack structure 
class Stack: 
    def __init__(self):
        self.head = None  
        self.size = 0     


    # Method to push an element onto the stack
    def push(self, value): 
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node 
        self.size += 1 


    # Method to remove a node from the top of the stack
    def pop(self):
        if self.head is None: 
            raise IndexError("The stack is empty")  
        else: 
            removed_node = self.head 
            value = removed_node.value 
            self.head = removed_node.next 
            removed_node.next = None   
            self.size -= 1 
            return value


    # Method to print the stack structure
    def print_stack(self):
        current = self.head 
        while current is not None: 
            print(current.value, end=" -> ")
            current = current.next
        print("None")


# Test 

first_stack = Stack()
first_stack.push(10)
first_stack.push(20)
first_stack.push(30)
first_stack.push(40)
first_stack.push(50)

first_stack.print_stack()

print("Example of pop usage")
removed_value = first_stack.pop()
print("Removed:", removed_value)

first_stack.print_stack()