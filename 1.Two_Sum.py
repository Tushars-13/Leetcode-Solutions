# 1. Two Sum

from collections import Counter
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        nums1_nums2_sum = Counter()
        for i in nums1:
            for j in nums2:
                nums1_nums2_sum[i+ j] += 1
        
        count = 0
        for k in nums3:
            for l in nums4:
                target = -(k+l)
                if target in nums1_nums2_sum:
                   count += nums1_nums2_sum[target]
        return count