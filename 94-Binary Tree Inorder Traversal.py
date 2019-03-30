class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
 
class BinaryTree(object):
    def __init__(self):
        self.root = None

    def add(self,value):
        treenode = TreeNode(value)
        if self.root == None:
            self.root = treenode
        else:
            q = [self.root]
            while True:
                pop_treenode = q.pop(0)
                if pop_treenode.left is None:
                    pop_treenode.left = treenode
                    return
                elif pop_treenode.right is None:
                    pop_treenode.right = treenode
                    return
                else:
                    q.append(pop_treenode.left)
                    q.append(pop_treenode.right)


class Solution(object):
    def inorderTraversal(self, root):
        """
        依次将所有子树的根节点入栈，然后依次按出栈顺序获取结果；相同于递归过程。
        para:
            root -- root node,TreeNode

        return:
            result -- traversal result,list of python
        """
        result = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right
        return result


if __name__ == '__main__':
    bt = BinaryTree()
    so = Solution()
    alist = [1,3,5,7]
    for i in alist:
        bt.add(i)
    print(bt.root.val, bt.root.left.val, bt.root.right.val, bt.root.left.left)
    print(so.inorderTraversal(bt.root))
    