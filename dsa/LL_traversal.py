class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
# traversal using iterative method
# time complexity: O(n)

def traverse_list(head):
    while head is not None:
        print(head.data, end=" ")
        if head.next is not None:
            print(" -> ", end="")
        head = head.next
    print()


#it's a hard-coded LL
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

traverse_list(head)
'''

# recursive function for traversal
def traverse_list(head):

    if head is None:
        print()
        return
    #print current node data
    print(head.data, end="")

    #print arrow for non last node
    if head.next is not None:
        print(" -> ", end="")

    #move to next node
    traverse_list(head.next)

#hard-coded LL
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

traverse_list(head)
