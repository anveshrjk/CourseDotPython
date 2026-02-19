class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
#method 1

#create nodes
n1 = Node(7)
n2 = Node(16)
n3 = Node(25)

#link nodes
n1.next = n2
n2.next = n3

head = n1 # head points to n1

# traverse and print LL
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")
'''

#method 2
# Create the first node (head of the list)
head = Node(10)

# Link the second node
head.next = Node(20)

# Link the third node
head.next.next = Node(30)

# Link the fourth node
head.next.next.next = Node(40)

# printing linked list
temp = head
while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next









