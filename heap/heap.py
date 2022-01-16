class MaxHeap :
    def __init__(self, values) -> None:
        self.heap = list()
        self.heap.append(None)
        self.heap.append(values)

    def cmp_max(self, index) :
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

    def insert(self, values) :
        self.heap.append(values)
        index = self.heap.index(values)

        while self.cmp_max(index) :
            parnet_index = index // 2
            self.heap[index], self.heap[parnet_index] = self.heap[parnet_index], self.heap[index]
            index = parnet_index

        return True

    def delete(self) :
        result = self.heap[1]
        self.heap[1] = self.heap[-1]
        del self.heap[-1]
        l_index = 2
        r_index = 3

        while True :
            if l_index+r_index >= len(self.heap) * 2 -1 :
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
    def __init__(self, values) -> None:
        self.heap = list()
        self.heap.append(None)
        self.heap.append(values)

    def cmp_min(self, index) :
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

    def insert(self, values) :
        self.heap.append(values)
        index = self.heap.index(values)

        while self.cmp_min(index) :
            parnet_index = index // 2
            self.heap[index], self.heap[parnet_index] = self.heap[parnet_index], self.heap[index]
            index = parnet_index

        return True

    def delete(self) :
        result = self.heap[1]
        self.heap[1] = self.heap[-1]
        del self.heap[-1]
        l_index = 2
        r_index = 3


        while True :
            if l_index+r_index >= len(self.heap) * 2 -1 :
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
