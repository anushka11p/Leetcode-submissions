class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merge = nums1+nums2
        merge.sort()
        if len(merge) % 2 == 0:
            return float(merge[len(merge)/2 - 1] + merge[len(merge)/2]) / 2.0
        else:
            return float(merge[len(merge)/2])