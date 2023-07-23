from avl_tree import AvlTree

if __name__ == '__main__':
    tree = AvlTree()
    root = None

    root = tree.insert(root, 10)
    root = tree.insert(root, 20)
    root = tree.insert(root, 30)
    root = tree.insert(root, 40)

    tree.inorder_traversal(root)
