class Node :
    def __init__(self, values, address = None) -> None:
        self.values = values
        self.address = address

class SinglyLinkedList :
    def __init__(self, head : object) -> None:
        self.head = head

    def add_tail_node(self, values) :
        node = Node(values)
        next_node = self.head
        while next_node.address is not None :
            next_node = next_node.address
        next_node.address = node

    def add_mid_node(self, index, values) :
        node = Node(values)
        next_node = self.head

        for _ in range(index) :
            next_node = next_node.address

        temp_addr = next_node.address
        next_node.address = node
        node.address = temp_addr

    def add_head_node(self, values) :
        node = Node(values)
        node.address = self.head
        self.head = node

    def delete_head_node(self) :
        node = self.head.address
        del self.head
        self.head = node

    def delete_tail_node(self) :
        next_node = self.head
        while next_node.address is not None:
            next_node = next_node.address
        

    def print(self) :
        next_node = self.head
        print(next_node.values)
        while next_node.address is not None:
            next_node = next_node.address
            print(next_node.values)

if __name__ == "__main__" :
    head = Node(1)
    linked = SinglyLinkedList(head)
    for i in range(2,10) :
        linked.add_tail_node(i)
    linked.add_mid_node(5,11)
    linked.add_head_node(1.1)
    linked.delete_head_node()
    linked.print()