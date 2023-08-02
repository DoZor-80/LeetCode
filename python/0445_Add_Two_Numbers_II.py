class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode] = None, l2: Optional[ListNode] = None) -> Optional[ListNode]:
        def reverse(node: ListNode) -> ListNode:
            previous, current = None, node
            while current:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
            return previous

        reversed_l1 = reverse(l1)
        reversed_l2 = reverse(l2)

        result = ListNode()
        current_l1 = reversed_l1
        current_l2 = reversed_l2
        cache = 0
        total_sum = 0
        while current_l1 or current_l2:
            if current_l1:
                total_sum += current_l1.val
                current_l1 = current_l1.next
            if current_l2:
                total_sum += current_l2.val
                current_l2 = current_l2.next
            result.val = total_sum % 10
            cache = total_sum // 10

            temp = ListNode(cache)
            temp.next = result
            result = temp
            total_sum = cache

        return result.next if cache == 0 else result
