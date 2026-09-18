class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 1
        c = -2 * n

        d = (b * b) - 4 * a * c

        root1 = (-b + math.sqrt(d)) / (2*a)
        

        return int(root1)