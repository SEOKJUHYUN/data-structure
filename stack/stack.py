"""Type Hint Modules"""
from typing import Any

class StackClass :
    """Stack 자료구조와 Push, Pop 메소드"""
    def __init__(self) -> None :
        self.stack : list = []

    def push(self, insert_value : Any) -> None:
        """stack에 마지막 인덱스에 데이터를 넣어주는 메소드."""
        self.stack[len(self.stack):] = [insert_value]

    def pop(self) -> Any :
        """stack에 마지막 인덱스 값을 꺼내는 메소드."""
        result = self.stack[-1]
        self.stack.remove(result)

        return result
