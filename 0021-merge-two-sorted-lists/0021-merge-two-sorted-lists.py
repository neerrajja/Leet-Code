class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to start the merged list
        dummy = ListNode()
        current = dummy

        # Traverse both lists and merge them
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach the remaining nodes from either list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next  # Return the merged list starting at the first real node
