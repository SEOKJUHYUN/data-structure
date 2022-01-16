""" 랜덤한 숫자를 이용하여 이진 탐색 트리를 테스트한다."""
import random

class Node :
    """Node를 생성하는 Class"""
    def __init__(self, values: int) -> None:
        self.values = values
        self.left = None
        self.right = None

class Tree :
    """이진 탐색 트리이다.
    트리에 Node를 추가하는 insert와 값이 있는지 확인하는 search와 Node를 삭제하는 delete 메소드를 구성되어있다.
    """
    def __init__(self, root_node: object) -> None :
        self.root_node = root_node

    def insert(self, values: int) -> bool :
        """이진 탐색 트리에 원하는 노드를 추가하는 메소드이다.

        Args:
            values (int): [이진 탐색 트리에 추가할 숫자.]

        Returns:
            bool: [성공 여부를 리턴한다.]
        """
        new_node = Node(values)
        now_node = self.root_node
        result: bool = False

        while True :
            if new_node.values < now_node.values :
                if now_node.left is None :
                    now_node.left = new_node
                    result = True
                    return result

                else :
                    now_node = now_node.left

            elif new_node.values > now_node.values :
                if now_node.right is None :
                    now_node.right = new_node
                    result = True
                    return result
                else :
                    now_node = now_node.right

            else :
                return result

    def search(self, values: int) -> bool :
        """이진 탐색 트리에 사용자가 원하는 값이 이진 탐색 트리에 있는지 확인해주는 메소드이다.

        Args:
            values (int): [이진 탐색 트리에서 확인할 숫자.]

        Returns:
            bool: [성공 여부를 리턴한다.]
        """
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


    def delete(self, values: int) -> bool :
        """이진 탐색 트리에서 노드를 삭제하는 메소드이다.

        Args:
            values (int): [이진 탐색 트레에서 삭제할 숫자.]

        Returns:
            bool: [성공 여부를 리턴한다.]
        """
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

                if left_node.left is None :
                    left_node.left = now_node.left

                else :
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
        if tree.search(num) is False:
            print('failed :', num, end=" ")
        else :
            print('success :', num)

    # 입력한 100개의 숫자 중 10개의 숫자를 랜덤 선택
    delete_nums = set()
    bst_nums = list(bst_nums)
    while len(delete_nums) != 10:
        delete_nums.add(bst_nums[random.randint(0, 99)])

    # 선택한 10개의 숫자를 삭제 (삭제 기능 확인)
    for del_num in delete_nums:
        if tree.delete(del_num) is False:
            print('failed :', del_num, end=" ")
        else :
            print('success :', del_num, end=" ")
