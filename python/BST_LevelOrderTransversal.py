import sys

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


    lstQueue = []
    def levelOrder(self,root):
        self.lstQueue.append(root)
        lstControl = []
        while len(self.lstQueue) > 0:
            aNode = self.lstQueue.pop(0)
            print(aNode.data,end=" ")

            if aNode.left is not None:
                self.lstQueue.append(aNode.left)
            if aNode.right is not None:
                self.lstQueue.append(aNode.right)


T=int("6")
myTree=Solution()
lstNumbers = [3,5,4,7,2,1]

root=None
for data in lstNumbers:
    root=myTree.insert(root,data)
myTree.levelOrder(root)
