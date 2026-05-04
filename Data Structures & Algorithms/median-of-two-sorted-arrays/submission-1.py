class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # O(m+n) soln is trivial

        p1 = 0
        p2 = 0
        l = []

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                l.append(nums1[p1])
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                l.append(nums2[p2])
                p2 += 1
            else:
                l.append(nums1[p1])
                l.append(nums2[p2])
                p1 += 1
                p2 += 1

        
        while p1 < len(nums1):
            l.append(nums1[p1])
            p1 += 1
        while p2 < len(nums2):
            l.append(nums2[p2])
            p2 += 1

        n = len(l)
        return l[n//2] if n % 2 == 1 else (l[n//2 - 1] + l[n//2]) / 2


