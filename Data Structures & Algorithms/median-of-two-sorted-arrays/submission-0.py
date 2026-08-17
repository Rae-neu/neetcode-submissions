class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m
        half = (m + n) // 2

        while left <= right:
            i = (left + right) // 2
            j = half - i

            Aleft = nums1[i-1] if i > 0 else float("-inf")
            Aright = nums1[i] if i < m else float("inf")

            Bleft = nums2[j-1] if j > 0 else float("-inf")
            Bright = nums2[j] if j < n else float("inf")

            if Aleft > Bright:
                right = i - 1
            elif Bleft > Aright:
                left = i + 1
            else:
                if (m + n) % 2 == 1:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2