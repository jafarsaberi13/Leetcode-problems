class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        s1 = {}
        s2 = {}

        for i in nums1:
            if i in nums2 and i not in s1:
                s1[i] = nums1.count(i)

        for i in nums2:
            if i in nums1 and i not in s2:
                s2[i] = nums2.count(i)

    
        res = []

        for i in s1.keys():
            if s1[i] > s2[i]:
                for j in range(s2[i]):
                    res.append(i)
            else:
                for j in range(s1[i]):
                    res.append(i)

        return res