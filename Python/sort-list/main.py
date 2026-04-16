from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sort(self, head: ListNode):
        if head is None or head.next is None:
            return head
        fast_pointer, slow_pointer = head, head
        while fast_pointer.next is not None and fast_pointer.next.next is not None and slow_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        right_pointer = slow_pointer.next
        slow_pointer.next = None
        left_pointer = head
        new_pointer = None
        if left_pointer.next is None and right_pointer.next is None:
            if left_pointer.val > right_pointer.val:
                right_pointer.next = left_pointer
                if new_pointer is None:
                    new_pointer = right_pointer
                else:
                    new_pointer.next = right_pointer
            else:
                left_pointer.next = right_pointer
                if new_pointer is None:
                    new_pointer = left_pointer
                else:
                    new_pointer.next = left_pointer
        else:
            new_pointer = ListNode(0, None)
            main_el = new_pointer
            left_pointer = self.sort(left_pointer)
            right_pointer = self.sort(right_pointer)
            while True:
                if left_pointer.val < right_pointer.val:
                    new_pointer.next = left_pointer
                    left_pointer = left_pointer.next
                    new_pointer = new_pointer.next
                else:
                    new_pointer.next = right_pointer
                    right_pointer = right_pointer.next
                    new_pointer = new_pointer.next
                if right_pointer == None:
                    new_pointer.next = left_pointer
                    break
                if left_pointer == None:
                    new_pointer.next = right_pointer
                    break

        
            return main_el.next
        return new_pointer
        

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        return self.sort(head)





Solution().sortList(ListNode(-1,ListNode(5,ListNode(3, ListNode(4, ListNode(0))))))
# Solution().sortList(ListNode(4,ListNode(2, ListNode(1, ListNode(3)))))
# Solution().sortList(ListNode(2,ListNode(1, ListNode(3))))
                
                



            


print("Hello from sort-list!")
