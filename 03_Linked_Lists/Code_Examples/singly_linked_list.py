# Singly Linked List Examples

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("NULL")


# Example usage
ll = SinglyLinkedList()
ll.insert_at_head(3)
ll.insert_at_head(2)
ll.insert_at_head(1)
ll.traverse()

# Output:
# 1 -> 2 -> 3 -> NULL
