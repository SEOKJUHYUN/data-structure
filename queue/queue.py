"""Type Hint Modules"""
from typing import Any, Union

class QueueClass :
    """FIFO, LIFO, Priority 3가지 구조의 Queue"""
    def __init__(self) -> None :
        self.queue : list = []

    def enqueue(self, insert_value : Union[int, str, tuple[int, Any]]) -> None :
        """Queue 데이터를 입력하는 함수.

        Args:
            insert_value (Union[int, str, tuple[int, Any]]): [정수, 문자열, 우선 순위 Queue인 경우 (우선순위, 값)으로 입력.]
        """
        self.queue.append(insert_value)

    def fifo_dequeue(self) -> Union[int, str] :
        """FIFO 구조로 Queue 데이터를 꺼내는 함수."""
        result = self.queue.pop(0)
        return result

    def lifo_dequeue(self) -> Union[int, str] :
        """LIFO 구조로 Queue 데이터를 꺼내는 함수."""
        result = self.queue.pop()
        return result

    def priority_dequeue(self) -> Union[int, str, tuple] :
        """우선순위 Queue.
        사용자가 입력한 Tuple(우선순위, 값) 중 우선순위 숫자가 낮은 Queue 데이터를 꺼내는 함수.
        """
        priority : list = []

        for _, value in enumerate(self.queue) :
            priority.append(value[0])

        min_num = min(priority)
        index = priority.index(min_num)
        result = self.queue.pop(index)

        return result[1]
