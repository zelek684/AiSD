from typing import Any


class Node:
    value = Any
    next = None

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    head = None
    tail = None

    def node(self, at: int) -> Node:
        try:
            node = self.head
            for i in range(at):
                node = node.next
            return node
        except AttributeError:
            return None

    def push(self, value: Any) -> None:
        new_node = Node(value, self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node

    def insert(self, value: Any, after: Node) -> None:
        new_node = Node(value)
        new_node.next = after.next
        after.next = new_node

    def pop(self) -> Any:
        poped = self.head
        self.head = poped.next
        return poped.value

    def remove_last(self) -> Any:
        try:
            last_value = self.tail.value
            node = self.head
            while node.next.next is not None:
                node = node.next
            node.next = None
            self.tail = node
            return last_value
        except AttributeError:
            return None

    def remove(self, after: Node):
        wartosc = after.next.next
        after.next = wartosc

    def __len__(self) -> int:
        try:
            node = self.head
            counter = 0
            while node is not None:
                counter += 1
                node = node.next
            return counter
        except AttributeError:
            return 0

    def __repr__(self):
        node = self.head
        text = ""
        while node is not None:
            text += str(node.value)
            if node.next is not None:
                text += " -> "
            node = node.next
        return text
class Stack:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def __len__(self):
        return len(self._storage)

    def __repr__(self):
        node = self._storage.head
        text = ""
        while node is not None:
            text += str(node.value) +"\n"
            node = node.next
        return text

    def push(self, element: Any):
        self._storage.push(element)

    def pop(self):
        return self._storage.pop()

class Queue:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def __len__(self):
        return len(self._storage)

    def __repr__(self):
        node = self._storage.head
        text = ""
        while node is not None:
            text += str(node.value)
            if node.next is not None:
                 text += ", "
            node = node.next
        return text

    def peek(self) -> Any:
        return self._storage.head.value

    def enqueue(self, element: Any) -> None:
        self._storage.append(element)

    def dequeue(self) -> Any:
        return self._storage.pop()

    
