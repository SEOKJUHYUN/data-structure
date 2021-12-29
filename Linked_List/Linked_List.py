class Node :
    def __init__(self, values, address = None) -> None:
        self.values = values
        self.address = address

class SinglyLinkedList :
    def __init__(self, head : object) -> None:
        self.head = head

    def add_tail_node(self, values) :
        new_node = Node(values)
        next_node = self.head
        while next_node.address is not None :
            next_node = next_node.address
        next_node.address = new_node

    def add_mid_node(self, index, values) :
        new_node = Node(values)
        next_node = self.head

        for _ in range(index) :
            next_node = next_node.address

        temp_addr = next_node.address
        next_node.address = new_node
        new_node.address = temp_addr

    def add_head_node(self, values) :
        new_node = Node(values)
        new_node.address = self.head
        self.head = new_node

    def delete_head_node(self) :
        temp_addr = self.head.address
        del self.head
        self.head = temp_addr

    def delete_tail_node(self) :
        next_node = self.head
        while next_node.address is not None:
            next_node = next_node.address
        temp = next_node
        next_node = self.head
        while next_node.address != temp:
            next_node = next_node.address
        next_node.address = None
        del temp

    def delete_mid_node(self, values) :
        next_node = self.head
        while next_node.values != values :
            next_node = next_node.address
        temp = next_node
        if temp == self.head :
            self.delete_head_node()
            return 0
        next_node = self.head
        while next_node.address != temp:
            next_node = next_node.address
        next_node.address = temp.address
        del temp

    def print(self) :
        next_node = self.head
        while next_node is not None:
            print(next_node.values)
            next_node = next_node.address
            

if __name__ == "__main__" :
    head = Node(1)
    linked = SinglyLinkedList(head)
    for i in range(2,10) :
        linked.add_tail_node(i)
    linked.add_mid_node(5,11)
    linked.add_head_node(1.1)
    linked.delete_head_node()
    linked.delete_tail_node()
    linked.delete_mid_node(11)
    linked.print()