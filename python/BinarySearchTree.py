class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root


    # def getHeight(self,root):
    #     return self.calcHeight(root, 0)
    #
    # def calcHeight(self, node, iCounter):
    #     iCounter +=1
    #     if node.right is not None:
    #         return self.calcHeight(node.right, iCounter)
    #     if node.left is not None:
    #         return self.calcHeight(node.left, iCounter)
    #     if node.left is not None and node.right is not None:
    #         return max(self.calcHeight(node.left, iCounter),self.calcHeight(node.right, iCounter))
    #     else:
    #         return iCounter-1

    def getHeight(self, root):
        if root.left is not None and root.right is not None:
            return 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        elif root.right is not None:
            return 1+self.getHeight(root.right)
        elif root.left is not None:
            return 1+self.getHeight(root.left)
        if root.left is None and root.right is None:
            return 0
        else:
            return 1


arrNumbers = [3,5,2,1,4,6,7]
arrNumbers = [20,50,35,44,9,15,62,11,13]

myTree=Solution()
root=None
for i in arrNumbers:
    data=i
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)
