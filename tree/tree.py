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

head = Node(21)
tree = Tree(head)
tree.insert(14)
tree.insert(28)
tree.insert(11)
tree.insert(18)
tree.insert(5)
tree.insert(12)
tree.insert(15)
tree.insert(19)
tree.insert(25)
tree.insert(32)
tree.insert(23)
tree.insert(27)
tree.insert(30)
tree.insert(37)
print()