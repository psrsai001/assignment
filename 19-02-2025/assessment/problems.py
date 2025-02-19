from ll import LinkedList, Node


def mid_ll():
    def mid(head: Node | None):
        if not head:
            print("LL is empty")
            return
        slow = fast = head

        while fast and slow and fast.next:
            fast = fast.next.next
            slow = slow.next

        if slow:
            print(slow.data, "is the mid element")
        else:
            print("no mid found")

    ll1 = LinkedList()
    ll1.insert_end(1)
    ll1.insert_end(2)
    ll1.insert_end(3)
    ll1.insert_end(4)
    ll1.insert_end(5)
    mid(ll1.head)
    ll2 = LinkedList()
    ll2.insert_end(1)
    ll2.insert_end(2)
    ll2.insert_end(3)
    ll2.insert_end(4)
    ll2.insert_end(5)
    ll2.insert_end(6)
    mid(ll2.head)


mid_ll()


def medion_of_sorted_arrays():
    class Solution:
        def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
            new = []
            i1 = i2 = 0

            n1 = len(nums1)
            n2 = len(nums2)
            if n1 == 0 and n2 == 0:
                return 0

            while i1 < n1 and i2 < n2:
                if nums1[i1] <= nums2[i2]:
                    new.append(nums1[i1])
                    i1 += 1
                else:
                    new.append(nums2[i2])
                    i2 += 1
            while i1 < n1:
                new.append(nums1[i1])
                i1 += 1

            new_len = n1 + n2
            mid = new_len >> 1
            if new_len & 1 == 0:
                return round((new[mid - 1] + new[mid]) / 2, 1)
            else:
                return round(new[mid], 1)


def find_sub_str():
    class Solution:
        def strStr(self, haystack: str, needle: str) -> int:
            import re

            match = re.search(needle, haystack)
            if match:
                return match.start()
            return -1
