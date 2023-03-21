import tkinter as tk
from tkinter import Canvas

class Node:
    def __init__(self, data):
        self.previous = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def length(self):
        temp = self.head
        count = 0
        while temp is not None:
            temp = temp.next
            count += 1
        return count

    def search(self, value):
        temp = self.head
        is_found = False
        while temp is not None:
            if temp.data == value:
                is_found = True
                break
            temp = temp.next
        return is_found

    def push_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.head is not None:
            self.head.previous = new_node
            self.head = new_node
            new_node.previous = None
        else:
            self.head = new_node
            self.tail = new_node

    def push_back(self, value):
        new_node = Node(value)
        new_node.previous = self.tail
        if self.tail is not None:
            self.tail.next = new_node
            new_node.next = None
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def peek_front(self):
        if self.head is None:
            return None
        return self.head.data

    def peek_back(self):
        if self.tail is None:
            return None
        return self.tail.data

    def pop_front(self):
        if self.head is None:
            return None
        temp = self.head
        if temp.next is not None:
            self.head = temp.next
            self.head.previous = None
        else:
            self.head = None
            self.tail = None
        return temp.data

    def pop_back(self):
        if self.tail is None:
            return None
        temp = self.tail
        if temp.previous is not None:
            self.tail = temp.previous
            self.tail.next = None
        else:
            self.head = None
            self.tail = None
        return temp.data

    def insert_after(self, node, value):
        if node is None:
            return
        new_node = Node(value)
        new_node.next = node.next
        new_node.previous = node
        node.next = new_node
        if new_node.next is not None:
            new_node.next.previous = new_node
        if node == self.tail:
            self.tail = new_node

    def insert_before(self, node, value):
        if node is None:
            return
        new_node = Node(value)
        new_node.previous = node.previous
        new_node.next = node
        node.previous = new_node
        if new_node.previous is not None:
            new_node.previous.next = new_node
        if node == self.head:
            self.head = new_node

    def update_element(self, old_value, new_value):
        temp = self.head
        is_updated = False
        while temp is not None:
            if temp.data == old_value:
                temp.data = new_value
                is_updated = True
            temp = temp.next
        if is_updated:
            print("Value Updated in the linked list")
        else:
            print("Value not Updated in the linked list")

    def update_at_position(self, value, position):
        temp = self.head
        count
        count = 0
        while temp is not None:
            if count == position:
                break
            count += 1
            temp = temp.next
        if temp is None:
            print("Less than {} elements in the linked list. Cannot update.".format(position))
        else:
            temp.data = value
            print("Value updated at position {}".format(position))



    def delete_from_position(self, position):
        if self.is_empty():
            print("Linked List is empty. Cannot delete elements.")
        elif position == 0:
            self.delete_from_beginning()
        else:
            temp = self.head
            count = 0
            while temp is not None:
                if count == position:
                    break
                count += 1
                temp = temp.next
            if temp is None:
                print("There are less than {} elements in linked list. Cannot delete element.".format(position))
            elif temp.next is None:
                self.delete_from_last()
            else:
                temp.previous.next = temp.next
                temp.next.previous = temp.previous

    def print_linked_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=", ")
            temp = temp.next
        print()

    def reverse(self):
        temp = None
        current = self.head
        while current is not None:
            temp = current.previous
            current.previous = current.next
            current.next = temp
            current = current.previous
        if temp is not None:
            self.head = temp.previous

    def sort(self):
        if self.head is None:
            return
        current = self.head
        while current.next is not None:
            index = current.next
            while index is not None:
                if current.data > index.data:
                    temp = current.data
                    current.data = index.data
                    index.data = temp
                index = index.next
            current = current.next
    
    def index(self, value):
        temp = self.head
        index = 0
        while temp is not None:
            if temp.data == value:
                return index
            index += 1
            temp = temp.next
        raise ValueError("Value not found in the list.")


    def copy(self):
        copied_list = DoublyLinkedList()
        temp = self.head
        while temp is not None:
            copied_list.push_back(temp.data)
            temp = temp.next
        return copied_list


    def count(self, value):
        temp = self.head
        count = 0
        while temp is not None:
            if temp.data == value:
                count += 1
            temp = temp.next
        return count

def draw_linked_list(linked_list):
    root = tk.Tk()
    canvas = Canvas(root, width=800, height=200)
    canvas.pack()

    current = linked_list.head
    x = 50
    y = 100
    node_width = 50
    node_height = 25

    while current:
        canvas.create_rectangle(x, y, x + node_width, y + node_height)
        canvas.create_text(x + node_width / 2, y + node_height / 2, text=str(current.data))
        if current.next:
            canvas.create_line(x + node_width, y + node_height / 2, x + node_width + 20, y + node_height / 2, arrow=tk.LAST)
            canvas.create_line(x + node_width + 20, y + node_height / 2, x + node_width, y + node_height / 2, arrow=tk.FIRST)
        if current.previous:  
            canvas.create_line(x, y + node_height / 2, x - 20, y + node_height / 2, arrow=tk.FIRST)
            canvas.create_line(x - 20, y + node_height / 2, x, y + node_height / 2, arrow=tk.FIRST)
        current = current.next
        x += node_width + 20

    root.mainloop()

def main():
    dll = DoublyLinkedList()
    dll.push_back(1)
    dll.push_back(2)
    dll.push_back(3)
    dll.push_front(0)
    dll.push_back(4)
    draw_linked_list(dll)

    
    dll.insert_before(dll.head.next, -1)
    dll.insert_after(dll.tail.previous, 5)
    draw_linked_list(dll)

    
    print("Length:", dll.length())
    print("Search 2:", dll.search(2))
    print("Search 10:", dll.search(10))
    
    print("Pop front:", dll.pop_front())
    draw_linked_list(dll)

    
    print("Pop back:", dll.pop_back())
    draw_linked_list(dll)

    
    dll.reverse()
    draw_linked_list(dll)

    
    dll.sort()
    draw_linked_list(dll)

    
    print("Index of 3:", dll.index(3))
    
    copied_list = dll.copy()
    copied_list.print_linked_list()
    
    print("Count of 1:", dll.count(1))

if __name__ == "__main__":
    main()