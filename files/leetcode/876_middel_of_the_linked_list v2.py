class List_Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_middle_node(head):
    slow = head
    fast = head
        
    # 快慢指針移動
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow
    
def traverse_linked_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next

# initiate a linked list    
node1 = List_Node(1)
node2 = List_Node(2)
node3 = List_Node(3)
node4 = List_Node(4)
node5 = List_Node(5)
node6 = List_Node(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = None

head = node1
mid = find_middle_node(head)
traverse_linked_list(mid)

