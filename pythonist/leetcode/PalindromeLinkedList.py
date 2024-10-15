def isPalindrome(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev = None
    while slow:
        tmp = slow.next
        slow.next = prev
        prev = slow
        slow = tmp
    tail = prev
    while tail:
        if tail.val != head.val:
            return False
        tail = tail.next
        head = head.next
    return True


def main():
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', isPalindrome([1, 2, 2, 1]))



if __name__ == "__main__":
    main()
