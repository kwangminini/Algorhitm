class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)


def get_linked_list_sum(linked_list_1, linked_list_2):
    linked_list_1_cur = linked_list_1.head
    linked_list_2_cur = linked_list_2.head
    linked_list_1_data=""
    linked_list_2_data=""
    while linked_list_1_cur is not None:
        linked_list_1_data+=str(linked_list_1_cur.data)
        linked_list_1_cur = linked_list_1_cur.next
    while linked_list_2_cur is not None:
        linked_list_2_data+=str(linked_list_2_cur.data)
        linked_list_2_cur = linked_list_2_cur.next

    # 구현해보세요!
    return int(linked_list_1_data)+int(linked_list_2_data)


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))