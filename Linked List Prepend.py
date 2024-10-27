# Linked List Prepend

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
            new_node.next = self.head     ## Points the new node to the previous head
            self.head = new_node          ## Makes the new node as the new head
        self.length += 1
        return True         

my_linked_list = LinkedList(5)
my_linked_list.prepend(2)
my_linked_list.prepend(9)
my_linked_list.print_list()