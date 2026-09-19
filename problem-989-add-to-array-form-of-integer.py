class Solution(object):
    def addfunc(self, num1, num2, s1, s2):
        res = []
        carry = 0

        # Align the smaller number with the larger number
        tmpnum2 = num2[s2 - s1:]

        # Add the digits that both numbers have
        for i in range(s1 - 1, -1, -1):
            tmp = num1[i] + tmpnum2[i] + carry

            one = tmp % 10
            carry = tmp // 10

            res.append(one)

        # Add the remaining digits of the larger number
        for i in range(s2 - s1 - 1, -1, -1):
            tmp = num2[i] + carry

            one = tmp % 10
            carry = tmp // 10

            res.append(one)

        # If carry > 0, add it
        if carry > 0:
            res.append(carry)

        return res[::-1]

    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        l = []

        while k > 0:
            one = k % 10
            k = k // 10
            l.append(one)

        l.reverse()
        s1 = len(num)
        s2 = len(l)

        if s1 <= s2:
            return self.addfunc(num, l, s1 , s2)
        else:
            return self.addfunc(l, num, s2 , s1)    
        