#!/bin/python3

class LinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class DoublyLinkedListNode(LinkedListNode):
    def __init__(self, node_data):
        super().__init__(node_data)
        self.prev = None


class LinkedList:
    node_class = LinkedListNode

    def __init__(self):
        self.head = None
        self.tail = None

    def _insert_tail_node(self, node):
        self.tail.next = node

    def insert_node(self, node_data):
        node = self.node_class(node_data)

        if not self.head:
            self.head = node
        else:
            self._insert_tail_node(node)

        self.tail = node

    def to_list(self):
        node = self.head
        result = []
        while node is not None:
            result.append(node.data)
            node = node.next
        return result

    def __str__(self):
        return " ".join(str(data) for data in self.to_list())


class DoublyLinkedList(LinkedList):
    node_class = DoublyLinkedListNode

    def _insert_tail_node(self, node):
        self.tail.next = node
        node.prev = self.tail



def reverse_single(linked_list: LinkedList) -> LinkedList:
    """Reverse a singly linked list in place.
    """
    current = linked_list.head
    linked_list.head = linked_list.tail
    linked_list.tail = current


    # 1 -> 2 -> 3 -> None
    # 1    2 -> 3 -> None
    # 1 <- 2    3 -> None
    # 1 <- 2 <- 3 
    prev = None
    while current is not None:
        next_ = current.next
        current.next = prev
        prev = current
        current = next_

    return linked_list


def reverse_double(linked_list: DoublyLinkedList) -> DoublyLinkedList:
    """Reverse a doubly linked list in place.
    """
    current = linked_list.head
    linked_list.head = linked_list.tail
    linked_list.tail = current

    while current is not None:
        next_ = current.next
        current.next = current.prev
        current.prev = next_
        current = next_
    
    return linked_list

def reverse_array(array: list) -> list:
    """Reverse an array in place.
    """
    def swap(arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    i = 0
    j = len(array) - 1
    while i < j:
        swap(array, i, j)
        i += 1
        j -= 1


    return array


if __name__ == '__main__':

    linked_list = DoublyLinkedList()
    linked_list.insert_node(1)
    linked_list.insert_node(2)
    linked_list.insert_node(3)

    print(linked_list)
    print(reverse_single(linked_list))
    print(reverse_single(linked_list))
    print(reverse_double(linked_list))

    print([1,2,3], reverse_array([1,2,3]))
    print([1], reverse_array([1]))
    print([], reverse_array([]))


