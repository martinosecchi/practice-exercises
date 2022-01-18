"""
Write a program to sort a stack in ascending order.
You should not make any assumptions about how the stack is implemented.
The following are the only functions that should be used to write this program:
push, pop, peek, isEmpty
"""

class Stack:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.top = None

    def __repr__(self):
        string = ""
        curr = self.top
        while curr is not None:
            string += "{} ".format(curr.value)
            curr = curr.next
        string += "]"
        return string

    def push(self, value):
        node = self.Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top:
            value = self.top.value
            self.top = self.top.next
            return value
        return None

    def peek(self):
        if self.top:
            return self.top.value
        return None

    def isEmpty(self):
        return self.top is None


def sort(stack):
    sorted = Stack()
    while not stack.isEmpty():
        curr = stack.pop()
        if sorted.isEmpty() or curr < sorted.peek():
            sorted.push(curr)
        else:
            # find right spot to insert in sorted
            i = 0
            while not sorted.isEmpty():
                v = sorted.peek()
                if v < curr:
                    stack.push(sorted.pop())
                    i += 1
                else:
                    break
            # insert
            sorted.push(curr)
            # put back sorted ones
            while i > 0:
                sorted.push(stack.pop())
                i -= 1       
    return sorted

def sortsimple(stack):
    sorted = Stack()
    while not stack.isEmpty():
        curr = stack.pop()
        while not sorted.isEmpty() and sorted.peek() < curr:
            stack.push(sorted.pop())
        sorted.push(curr)
    return sorted

stack = Stack()
stack.push(2)
stack.push(6)
stack.push(3)
stack.push(5)
stack.push(8)
stack.push(4)
stack.push(7)
stack.push(1)

print(stack)
# stack = sort(stack)
stack = sortsimple(stack)
print(stack)

assert repr(stack) == "1 2 3 4 5 6 7 8 ]"


