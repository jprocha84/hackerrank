class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        current = head
        while current:
            if current.next is not None:
                if current.data == current.next.data:
                    current.next = current.next.next
                else:
                    current = current.next
            else:
                current = None
        return head

mylist= Solution()
T=int("6")
head=None
#lstData = [1,2,3,3,3,3,4,4]
lstData = [1,1,1,1,1,1]
for data in lstData:
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head);
