# Pop first element from a Linked List

class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self,value) -> None:
        new_node  = Node(value)
        self.value = new_node
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head     
            self.head = new_node     
        self.length += 1
        return True    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None

linked_list = LinkedList(7)
linked_list.prepend(3)
linked_list.pop()
linked_list.print_list()
