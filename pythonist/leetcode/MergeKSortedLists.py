
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def mergeKLists(lists):
    if not lists:
        return None
    while len(lists) > 1:
        merged_lists = []
        lists_len = len(lists)
        if idx in range(0, lists_len, 2):
            l1 = lists[idx]
            next_id = idx + 1
            l2 = lists[next_id] if next_id < lists_len else None
            new_list = merge_two_sorted_lists(l1, l2)
            merged_lists.append(new_list)
        lists = merged_lists

    return lists[0]

def merge_two_sorted_lists(list1, list2):
    dummy = ListNode()
    tail = dummy
    while list1 and list2:
        if list1.value < list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list2 or list1

    return dummy.next

def main():
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', mergeKLists([[1,4,5],[1,3,4],[2,6]]))



if __name__ == "__main__":
    main()
