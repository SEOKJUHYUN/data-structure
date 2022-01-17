class MaxHeap :
    """MaxHeap을 생성하는 Class이다.
    생성자를 통해서 Root Node를 입력받고 개발할 때 편하기 위해서 0번 index를 None으로 사용한다.
    """
    def __init__(self, values: int) -> None:
        self.heap = list()
        self.heap.append(None)
        self.heap.append(values)

    def cmp_max(self, index: int) -> bool :
        """입력받은 index 번호를 통해서 부모 index 번호를 계산하고 부모 Node와 값을 비교해서
        자식 노드 값이 더 크면 True를 리턴한다.

        Args:
            index (int): [자식 Node의 Index 번호]

        Returns:
            bool: [자식 Node가 부모 Node 값보다 크면 True를 리턴한다.]
        """
        result: bool = False

        parnet_index = index // 2

        if index == 1 :
            return result

        elif index >= len(self.heap) :
            return result

        elif self.heap[index] > self.heap[parnet_index] :
            result = True
            return result

        else :
            return result

    def insert(self, values: int) -> None :
        """Heap에 추가하고 싶은 값을 추가해주는 메소드이다.

        Args:
            values (int): [추가하고 싶은 값.]

        Returns:
            None: [별도의 리턴은 없다.]
        """
        self.heap.append(values)
        index = self.heap.index(values)

        while self.cmp_max(index) :
            parnet_index = index // 2
            self.heap[index], self.heap[parnet_index] = self.heap[parnet_index], self.heap[index]
            index = parnet_index

    def delete(self) -> int :
        """MaxHeap Root Node를 삭제하는 메소드이다.

        Returns:
            int: [삭제된 값을 리턴한다.]
        """
        result: int = self.heap[1]
        self.heap[1] = self.heap[-1]
        del self.heap[-1]
        l_index = 2
        r_index = 3

        while True :
            if l_index+r_index > len(self.heap) * 2 - 2 :
                break

            if self.heap[l_index] > self.heap[r_index] :
                if self.cmp_max(l_index) :
                    parnet_index = l_index // 2
                    self.heap[l_index], self.heap[parnet_index] = self.heap[parnet_index], self.heap[l_index]
                    r_index = self.heap.index(self.heap[l_index]) * 2 + 1
                    l_index = self.heap.index(self.heap[l_index]) * 2
                else :
                    break

            elif self.heap[r_index] > self.heap[l_index] :
                if self.cmp_max(r_index) :
                    parnet_index = r_index // 2
                    self.heap[r_index], self.heap[parnet_index] = self.heap[parnet_index], self.heap[r_index]
                    l_index = self.heap.index(self.heap[r_index]) * 2
                    r_index = self.heap.index(self.heap[r_index]) * 2 + 1
                else :
                    break

        return result

class MinHeap :
    """MinHeap을 생성하는 Class이다.
    생성자를 통해서 Root Node를 입력받고 개발할 때 편하기 위해서 0번 index를 None으로 사용한다.
    """
    def __init__(self, values: int) -> None:
        self.heap = list()
        self.heap.append(None)
        self.heap.append(values)

    def cmp_min(self, index: int) -> bool :
        """입력받은 index 번호를 통해서 부모 index 번호를 계산하고 부모 Node와 값을 비교해서
        자식 노드 값이 더 작으면 True를 리턴한다.

        Args:
            index (int): [자식 Node의 Index 번호]

        Returns:
            bool: [자식 Node가 부모 Node 값보다 작으면 True를 리턴한다.]
        """
        result: bool = False

        parnet_index = index // 2

        if index == 1 :
            return result

        elif index >= len(self.heap) :
            return result

        elif self.heap[index] < self.heap[parnet_index] :
            result = True
            return result

        else :
            return result

    def insert(self, values: int) -> None :
        """Heap에 추가하고 싶은 값을 추가해주는 메소드이다.

        Args:
            values (int): [추가하고 싶은 값.]

        Returns:
            None: [별도의 리턴은 없다.]
        """
        self.heap.append(values)
        index = self.heap.index(values)

        while self.cmp_min(index) :
            parnet_index = index // 2
            self.heap[index], self.heap[parnet_index] = self.heap[parnet_index], self.heap[index]
            index = parnet_index

    def delete(self) -> int :
        """MinHeap Root Node를 삭제하는 메소드이다.

        Returns:
            int: [삭제된 값을 리턴한다.]
        """
        result = self.heap[1]
        self.heap[1] = self.heap[-1]
        del self.heap[-1]
        l_index = 2
        r_index = 3


        while True :
            if l_index+r_index > len(self.heap) * 2 - 2 :
                break

            if self.heap[l_index] < self.heap[r_index] :
                if self.cmp_min(l_index) :
                    parnet_index = l_index // 2
                    self.heap[l_index], self.heap[parnet_index] = self.heap[parnet_index], self.heap[l_index]
                    r_index = self.heap.index(self.heap[l_index]) * 2 + 1
                    l_index = self.heap.index(self.heap[l_index]) * 2
                else :
                    break

            elif self.heap[r_index] < self.heap[l_index] :
                if self.cmp_min(r_index) :
                    parnet_index = r_index // 2
                    self.heap[r_index], self.heap[parnet_index] = self.heap[parnet_index], self.heap[r_index]
                    l_index = self.heap.index(self.heap[r_index]) * 2
                    r_index = self.heap.index(self.heap[r_index]) * 2 + 1
                else :
                    break

        return result


if __name__ == "__main__" :
    max_heap = MaxHeap(15)
    max_heap.insert(10)
    max_heap.insert(8)
    max_heap.insert(5)
    max_heap.insert(4)
    max_heap.insert(20)
    print(max_heap.heap)
    print(max_heap.delete())
    print(max_heap.heap)
    min_heap = MinHeap(15)
    min_heap.insert(10)
    min_heap.insert(8)
    min_heap.insert(5)
    min_heap.insert(4)
    min_heap.insert(20)
    print(min_heap.heap)
    print(min_heap.delete())
    print(min_heap.heap)
