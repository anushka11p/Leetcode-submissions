class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        result = []

        dummy = ListNode(0)
        curr = dummy
        
        for i in lists:
            while i:
                result.append(i.val)
                i=i.next
        result.sort()
        for num in result:
            curr.next = ListNode(num)
            curr = curr.next
            
        return dummy.next

            
        