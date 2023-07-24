class Solution:
    """
        https://leetcode.com/problems/median-of-two-sorted-arrays/description/

        Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

        The overall run time complexity should be O(log (m+n)).
    """
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_nums = sorted(nums1 + nums2)
        mid_index = len(merged_nums) // 2

        median = merged_nums[mid_index]
        if len(merged_nums) % 2 == 0:
            median = (merged_nums[mid_index] + merged_nums[mid_index - 1]) / 2

        return median