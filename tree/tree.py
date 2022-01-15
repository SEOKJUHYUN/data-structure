class Node :
    def __init__(self, values) -> None:
        self.values = values
        self.left = None
        self.right = None

class Tree :
    def __init__(self, root_node : object) -> None:
        self.root_node = root_node

    def insert(self, values) :
        new_node = Node(values)

        now_node = self.root_node

        while True :
            if new_node.values < now_node.values :
                if now_node.left is None :
                    now_node.left = new_node
                    break
                else :
                    now_node = now_node.left

            elif new_node.values > now_node.values :
                if now_node.right is None :
                    now_node.right = new_node
                    break
                else :
                    now_node = now_node.right

    def search(self, values) :
        now_node = self.root_node
        result: bool = False

        while now_node is not None :
            if values == now_node.values :
                result = True
                break

            elif values < now_node.values :
                now_node = now_node.left

            else :
                now_node = now_node.right

        return result


    def delete(self, values) :
        now_node = self.root_node
        parent_node = self.root_node
        result: bool = False
        left_node = None
        left_parent_node = None

        while now_node is not None :
            if values == now_node.values :
                break

            elif values < now_node.values :
                parent_node = now_node
                now_node = now_node.left

            else :
                parent_node = now_node
                now_node = now_node.right
            

        while now_node is not None :
            if values == now_node.values :
                if now_node.right is None and now_node.left is None :
                    if now_node.values < parent_node.values  :
                        parent_node.left = None
                    else :
                        parent_node.right = None
                    del now_node
                    result = True
                    return result

                elif now_node.right is not None and now_node.left is None :
                        if now_node.values < parent_node.values  :
                            parent_node.left = now_node.right
                        else :
                            parent_node.right = now_node.right
                        del now_node
                        result = True
                        return result

                elif now_node.right is None and now_node.left is not None :
                    if  parent_node.values < now_node.values :
                        parent_node.left = now_node.left
                    else :
                        parent_node.right = now_node.left
                    del now_node
                    result = True
                    return result

                elif now_node.right is not None and now_node.left is not None :
                        left_node = now_node.right
                        while left_node.left is not None :
                            left_parent_node = left_node
                            left_node = left_node.left

                        if left_node.right is not None :
                            left_parent_node.left = left_node.right

                        left_node.left = now_node.left
                        left_node.right = now_node.right

                        if now_node.values < parent_node.values :
                            parent_node.left = left_node
                        else :
                            parent_node.right = left_node

                        del now_node
                        result = True
                        return result
                    
            else :
                return result

        return result


if __name__ == "__main__" :
    import random

    # 0 ~ 999 중, 100 개의 숫자 랜덤 선택
    bst_nums = set()
    while len(bst_nums) != 100:
        bst_nums.add(random.randint(0, 999))
    # print (bst_nums)

    # 선택된 100개의 숫자를 이진 탐색 트리에 입력, 임의로 루트노드는 500을 넣기로 함
    head = Node(500)
    tree = Tree(head)
    for num in bst_nums:
        tree.insert(num)

    # 입력한 100개의 숫자 검색 (검색 기능 확인)
    for num in bst_nums:
        if tree.search(num) == False:
            print ('search failed', num)
        else :
            print ('search success', num, end=" ")

    # 입력한 100개의 숫자 중 10개의 숫자를 랜덤 선택
    delete_nums = set()
    bst_nums = list(bst_nums)
    while len(delete_nums) != 10:
        delete_nums.add(bst_nums[random.randint(0, 99)])

    # 선택한 10개의 숫자를 삭제 (삭제 기능 확인)
    for del_num in delete_nums:
        if tree.delete(del_num) == False:
            print('delete failed', del_num)
        else :
            print ('search success', del_num)