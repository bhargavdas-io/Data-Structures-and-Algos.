## LinkedList SET method

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp 
    
    def set_value(self, index:int, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
        
linked_list = LinkedList(0)
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.set_value(1, 2)
linked_list.print_list()

