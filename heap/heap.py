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

        while self.cmp_max(l_index) :
            parnet_index = l_index // 2
            self.heap[l_index], self.heap[parnet_index] = self.heap[parnet_index], self.heap[l_index]
            l_index = self.heap.index(self.heap[l_index]) * 2

        while self.cmp_max(r_index) :
            parnet_index = r_index // 2
            self.heap[r_index], self.heap[parnet_index] = self.heap[parnet_index], self.heap[r_index]
            r_index = self.heap.index(self.heap[r_index]) * 2 + 1

        return result


if __name__ == "__main__" :
    heap = MaxHeap(15)
    heap.insert(10)
    heap.insert(8)
    heap.insert(5)
    heap.insert(4)
    heap.insert(20)
    heap.insert(25)
    heap.delete()
    print(heap.heap)