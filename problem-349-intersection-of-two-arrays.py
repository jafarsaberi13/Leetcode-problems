#solution 1
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
        

# solution 2

class Solution(object):
    def set_inters(self, set1, set2):
        return [i for i in set1 if i in set2]

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) > len(set2):
            return self.set_inters(set2, set1)
        else:
            return self.set_inters(set1, set2)
        