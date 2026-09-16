solution 1
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        l = 0 
        tmplist1 = []
        tmplist2 = []
        if len(nums1) > len(nums2):
            l = len(nums2)
            tmplist1 = nums2
            tmplist2 = nums1
        else:
            l = len(nums1)
            tmplist1 = nums1
            tmplist2 = nums2

        result = []
        for i in range(l):
            tmp = tmplist1[i]
            if tmp in tmplist2:
                if tmp not in result:
                    result.append(tmp)

        return result 
        