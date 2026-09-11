class Solution:
    def reverseBits(self, n: int) -> int:
        b = format(n, '032b')

        rev = b[::-1]

        result = int(rev, 2)

        return result