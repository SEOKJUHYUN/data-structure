"""Type Hint Modules"""
from typing import Any
class Node :
    """연결 리스트에 사용할 노드를 생성하는 class."""
    def __init__(self, values, address = None, prev = None) -> None:
        self.values = values
        self.address = address
        self.prev = prev

class SinglyLinkedList :
    """단일 연결 리스트"""
    def __init__(self, head : object) -> None:
        self.head = head

    def add_head_node(self, values : Any) -> None :
        """단일 연결 리스트 맨 앞에 노드를 추가.

        Args:
            values (Any): [추가할 노드에 들어갈 데이터.]
        """
        new_node = Node(values)
        new_node.address = self.head
        self.head = new_node

    def add_tail_node(self, values : Any) -> None :
        """단일 연결 리스트 맨 뒤에 노드를 추가.

        Args:
            values (Any): [추가할 노드에 들어갈 데이터.]
        """
        new_node = Node(values)
        next_node = self.head

        while next_node.address is not None :
            next_node = next_node.address

        next_node.address = new_node

    def add_mid_node(self, index : int, values : Any) -> None :
        """원하는 단일 연결 리스트 index에 노드를 추가.

        Args:
            index (int): [노드가 추가될 index 번호.]
            values (Any): [추가할 노드에 들어갈 데이터.]
        """
        new_node = Node(values)
        next_node = self.head

        if index == 0 :
            self.add_head_node(values)
            return 0

        for _ in range(index - 1) :
            next_node = next_node.address

        temp_addr = next_node.address
        next_node.address = new_node
        new_node.address = temp_addr

    def delete_head_node(self) -> None :
        """단일 연결 리스트 맨 앞에 있는 노드를 제거."""
        temp_addr = self.head.address
        del self.head
        self.head = temp_addr

    def delete_tail_node(self) -> None :
        """단일 연결 리스트 맨 뒤에 있는 노드를 제거."""
        next_node = self.head

        while next_node.address is not None:
            next_node = next_node.address

        temp = next_node
        next_node = self.head

        while next_node.address != temp:
            next_node = next_node.address

        next_node.address = None
        del temp

    def delete_mid_node(self, values : Any) -> None :
        """사용자가 입력한 데이터 값을 찾아서 노드를 제거

        Args:
            values (Any): [제거하길 원하는 데이터.]
        """
        next_node = self.head

        if values == self.head.values :
            self.delete_head_node()
            return 0

        while next_node.values != values :
            next_node = next_node.address

        temp = next_node

        next_node = self.head
        while next_node.address != temp:
            next_node = next_node.address
        next_node.address = temp.address
        del temp

    def print(self) -> None :
        """단일 연결 리스트를 순회하면서 데이터를 출력."""
        next_node = self.head

        while next_node is not None:
            print(next_node.values, end=" ")
            next_node = next_node.address

class DoublyLinkedList :
    """이중 연결 리스트"""
    def __init__(self, head : object) -> None:
        self.head = head
        self.tail = self.head

    def add_head_node(self, values : Any) -> None :
        """이중 연결 리스트 맨 앞에 노드를 추가.

        Args:
            values (Any): [추가할 노드에 들어갈 데이터.]
        """
        new_node = Node(values)
        new_node.address = self.head
        self.head.prev = new_node
        self.head = new_node

    def add_tail_node(self, values : Any) -> None :
        """이중 연결 리스트 맨 뒤에 노드를 추가.

        Args:
            values (Any): [추가할 노드에 들어갈 데이터.]
        """
        new_node = Node(values)

        next_node = self.head
        while next_node.address is not None :
            next_node = next_node.address

        next_node.address = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def add_mid_node(self, index : int, values : Any) -> None :
        """이중 연결 리스트에 원하는 index에 노드를 추가.

        Args:
            index (int): [노드가 추가될 index 번호.]
            values (Any): [추가할 노드에 들어갈 데이터.]
        """
        new_node = Node(values)
        next_node = self.head

        if index == 0 :
            self.add_head_node(values)
            return 0

        for _ in range(index - 1) :
            next_node = next_node.address

        if next_node.address is None :
            next_node.address = new_node
            new_node.prev = self.tail
            self.tail = new_node
            return 0

        temp_addr = next_node.address
        next_node.address = new_node
        new_node.address = temp_addr
        new_node.prev = next_node
        temp_addr.prev = new_node

    def delete_head_node(self) -> None :
        """이중 연결 리스트 맨 앞에 있는 노드를 제거."""
        temp_addr = self.head.address
        del self.head
        temp_addr.prev = None
        self.head = temp_addr

    def delete_tail_node(self) -> None :
        """이중 연결 리스트 맨 뒤에 있는 노드를 제거."""
        prev_node = self.tail
        self.tail = prev_node.prev
        self.tail.address = None
        del prev_node

    def delete_mid_node(self, values : Any, reverse : bool = False) -> None :
        """사용자가 입력한 값을 찾아서 노드를 제거.

        Args:
            values (Any): [제거하길 원하는 값.]
            reverse (bool, optional): [앞에서부터 탐색할 지 뒤에서 부터 탐색할 지 여부 기본적으로 앞에서 부터 탐색]. Defaults to False.
        """
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

    def forward_print(self) -> None :
        """이중 연결 리스트를 앞에서부터 순회하면서 데이터를 출력."""
        next_node = self.head
        while next_node is not None:
            print(next_node.values, end=" ")
            next_node = next_node.address

    def reverse_print(self) -> None :
        """이중 연결 리스트를 뒤에서부터 순회하면서 데이터를 출력."""
        prev_node = self.tail
        while prev_node is not None:
            print(prev_node.values, end=" ")
            prev_node = prev_node.prev
