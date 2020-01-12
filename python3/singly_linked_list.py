from print_after_done import print_after_done


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    head = None


    @print_after_done
    def add_element(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    @print_after_done
    def remove_element(self, data):
        current_node = self.head
        if self.head == None:
            return
        if self.head.data == data:
            self.head = self.head.next
        next_node = current_node.next
        while next_node:
            if next_node.data == data:
                current_node.next = next_node.next
                return
            current_node = current_node.next
            next_node = current_node.next

    def __str__(self):
        if not self.head:
            return 'Empty List!'
        string = ''
        current_node = self.head
        while current_node.next:
            string += str(current_node.data) + ' => '
            current_node = current_node.next
        string += str(current_node.data)
        return string


l = LinkedList()
l.add_element(1)
l.add_element(2)
l.add_element(3)
l.add_element(4)
l.add_element(5)
l.remove_element(1)
l.remove_element(5)
l.remove_element(3)
l.remove_element(4)
l.remove_element(2)
