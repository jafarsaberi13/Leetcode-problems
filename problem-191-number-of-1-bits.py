class Solution:
    def hammingWeight(self, n: int) -> int:
        b = format(n, '032b')

        s = str(b)
        return s.count('1')