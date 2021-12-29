class Node :
    def __init__(self, values, address = None, prev = None) -> None:
        self.values = values
        self.address = address
        self.prev = prev

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

        if index == 0 :
            self.add_head_node(values)
            return 0

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
            print(next_node.values, end=" ")
            next_node = next_node.address

class DoublyLinkedList :
    def __init__(self, head : object) -> None:
        self.head = head
        self.tail = self.head

    def add_tail_node(self, values) :
        new_node = Node(values)
        next_node = self.head
        while next_node.address is not None :
            next_node = next_node.address
        next_node.address = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def add_head_node(self, values) :
        new_node = Node(values)
        new_node.address = self.head
        self.head.prev = new_node
        self.head = new_node
    
    def add_mid_node(self, index, values) :
        new_node = Node(values)
        next_node = self.head

        if index == 0 :
            self.add_head_node(values)
            return 0

        for _ in range(index) :
            next_node = next_node.address

        temp_addr = next_node.address
        next_node.address = new_node
        new_node.address = temp_addr
        new_node.prev = next_node
        temp_addr.prev = new_node

    def delete_head_node(self) :
        temp_addr = self.head.address
        del self.head
        temp_addr.prev = None
        self.head = temp_addr

    def delete_tail_node(self) :
        prev_node = self.tail
        self.tail = prev_node.prev
        self.tail.address = None
        del prev_node

    def delete_mid_node(self, values, reverse = False) :
        if values == self.head.values :
            self.delete_head_node()
            return 0

        elif values == self.tail.values :
            self.delete_tail_node()
            return 0

        else :
            if reverse is True :
                next_node = self.tail
                while next_node.values != values :
                    next_node = next_node.prev
                temp_prev = next_node.prev
                temp_addr = next_node.address
                temp_prev.address = temp_addr
                temp_addr.prev = temp_prev
                del next_node

            else :
                next_node = self.head
                while next_node.values != values :
                    next_node = next_node.address
                temp_prev = next_node.prev
                temp_addr = next_node.address
                temp_prev.address = temp_addr
                temp_addr.prev = temp_prev
                del next_node

    def forward_print(self) :
        next_node = self.head
        while next_node is not None:
            print(next_node.values, end=" ")
            next_node = next_node.address

    def reverse_print(self) :
        prev_node = self.tail
        while prev_node is not None:
            print(prev_node.values, end=" ")
            prev_node = prev_node.prev


if __name__ == "__main__" :
    head = Node(1)
    head2 = Node(1)
    link = SinglyLinkedList(head)
    dou = DoublyLinkedList(head2)
    for i in range(2,9) :
        link.add_tail_node(i)
        dou.add_tail_node(i)
    link.add_mid_node(0,11)
    link.add_mid_node(8,99)
    link.delete_mid_node(99)
    link.print()
    print()
    dou.add_mid_node(0,11)
    dou.add_mid_node(7,99)
    dou.delete_mid_node(99)
    dou.forward_print()
        