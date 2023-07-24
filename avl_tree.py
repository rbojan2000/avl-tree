from tree_node import TreeNode

class AvlTree(object):
 
     def insert(self, root, key):
          
          if not root:
               return TreeNode(key)
          elif key < root.val:
               root.left = self.insert(root.left, key)
          else:
               root.right = self.insert(root.right, key)
     
          root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))
     
          balance = self.get_balance(root)
     
          # Case 1 - Left Left
          if balance > 1 and key < root.left.val:
               return self.right_rotate(root)
     
          # Case 2 - Right Right
          if balance < -1 and key > root.right.val:
               return self.left_rotate(root)
     
          # Case 3 - Left Right
          if balance > 1 and key > root.left.val:
               root.left = self.left_rotate(root.left)
               return self.right_rotate(root)
     
          # Case 4 - Right Left
          if balance < -1 and key < root.right.val:
               root.right = self.right_rotate(root.right)
               return self.left_rotate(root)
     
          return root
     
     def left_rotate(self, z):
     
          y = z.right
          T2 = y.left
     
          y.left = z
          z.right = T2
     
          z.height = 1 + max(self.get_height(z.left),
                              self.get_height(z.right))
          y.height = 1 + max(self.get_height(y.left),
                              self.get_height(y.right))
          return y
     
     def right_rotate(self, z):
     
          y = z.left
          T3 = y.right
     
          y.right = z
          z.left = T3
     
          z.height = 1 + max(self.get_height(z.left),
                         self.get_height(z.right))
          y.height = 1 + max(self.get_height(y.left),
                         self.get_height(y.right))
     
          return y
     
     def get_height(self, root):
          if not root:
               return 0
     
          return root.height
     
     def get_balance(self, root):
          if not root:
               return 0
     
          return self.get_height(root.left) - self.get_height(root.right)
     
     def find_key(self, root, key):
          if root.val == key:
               return root
          elif key > root.val:
               return self.find_key(root.right, key)
          else:
               return self.find_key(root.left, key)

     def inorder_traversal(self, root, level=0, prefix="Root:"):
          if root:
               print(" " * (level * 4) + prefix + str(root.val))
               if root.left or root.right:
                    self.inorder_traversal(root.left, level + 1, "L--- ")
                    self.inorder_traversal(root.right, level + 1, "R--- ")