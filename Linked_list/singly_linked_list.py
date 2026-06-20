# class Node:
#     def __init__(self, new_data):
#         self.data = new_data
#         self.next = None

# def traverseList(head):
#     while head is not None:
#         print(head.data, end='')
#         if head.next is not None:
#             print('->', end='')
#         head = head.next
#     print()

# if __name__=='__main__':
#     head = Node(10)
#     head.next= Node(20)
#     head.next.next = Node(30)
#     head.next.next.next=Node(40)

#     traverseList(head)

#Insertion at the beginning

# class Node:
#     def __init__(self, new_data):
#         self.data = new_data
#         self.next = None
# def insertList(head, new_data):
#     newNode = Node(new_data)
#     newNode.next = head
#     return newNode
# def printlist(head):
#     curr= head
#     while curr is not None:
#         print(curr.data, end='')
#         if curr.next is not None:
#             print('->', end='')
#         curr = curr.next
#     print()

# if __name__=='__main__':

#     head = Node(2)
#     head.next = Node(3)
#     head.next.next = Node(4)

#     new_data=1
#     head = insertList(head, new_data) 

#     printlist(head)

#insert at the end
# class Node:

#     def __init__(self, new_data):
#         self.data = new_data
#         self.next = None

# def insertend(head , new_data):
#     newNode = Node(new_data)

#     if head is None:
#         return newNode
#     last = head

#     while last.next is not None:
#         last = last.next
    
#     last.next = newNode

#     return head

# def printlist(node):
#     while node is not None:
#         print(node.data, end='')
#         if node.next is not None:
#             print('->', end = '')
#         node = node.next
#     print()

# if __name__=='__main__':

#     head = Node(1)
#     head.next = Node(2)
#     head.next.next = Node(3)
#     head.next.next.next = Node(4)

#     head = insertend(head, 6)

#     printlist(head)


# insert at any position

# class Node:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# def insertpos(head, pos, val):
#     if pos < 1:
#         return head
    

#     if pos == 1:
#         newNode = Node(val)
#         newNode.next = head
#         return newNode
#     curr = head
#     for i in range(1, pos-1):
#         if curr is None:
#             return head
#         curr = curr.next

#         if curr is None:
#             return head
#         newNode = Node(val)

#         newNode.next = curr.next
#         curr.next = newNode

#         return head
# def printlist(head):
#     curr = head
#     while curr is not None:
#         print(curr.val, end = '')
#         if curr.next is not None:
#             print('->', end='')

#         curr = curr.next

#     print()

# if __name__=='__main__':

#     head = Node(1)
#     head.next = Node(2)
#     head.next.next = Node(4)

#     val, pos = 3,3

#     head = insertpos(head, pos, val)
#     printlist(head)


# deletion from the beginning

# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.next = None
    

# def deleteFromend(head):

#     if head is None:
#         return None
    
#     temp = head
#     head = head.next

#     temp = None

#     return head
# def printlist(head):
#     while head is not None:
#         print(head.data, end='')
#         if head.next is not None:
#             print('->', end='')
#         head = head.next
#     print()

# if __name__=='__main__':
#     head = Node(1)
#     head.next = Node(2)
#     head.next.next = Node(3)
#     head.next.next.next = Node(4)
#     head.next.next.next.next = Node(5)

#     head = deleteFromend(head)
#     printlist(head)


# delete  from end

class Node :
    def __init__(self, x):
        self.data = x
        self.next = None
def deletefromend(head):
    if head is  None:
        return None
    if head.next is  None:
        return None
    
    secondlast = head
    while secondlast.next.next is not None:
        secondlast = secondlast.next

    secondlast.next = None
    return head
def printlist(head):
    while head is not None:
        print(head.data, '->', end='')
        head = head.next
    print()

if __name__=='__main__':

    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = Node(5)

    deletefromend(head)
    printlist(head)




