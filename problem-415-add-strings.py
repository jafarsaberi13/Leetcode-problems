class Solution(object):
    # num1 is the smaller number
    # num2 is the larger number
    def addfunc(self, num1, num2, s1, s2):
        res = []
        carry = 0

        # Align the smaller number with the larger number
        tmpnum2 = num2[s2 - s1:]

        # Add the digits that both numbers have
        for i in range(s1 - 1, -1, -1):
            tmp = int(num1[i]) + int(tmpnum2[i]) + carry

            one = tmp % 10
            carry = tmp // 10

            res.append(str(one))

        # Add the remaining digits of the larger number
        for i in range(s2 - s1 - 1, -1, -1):
            tmp = int(num2[i]) + carry

            one = tmp % 10
            carry = tmp // 10

            res.append(str(one))

        # If carry > 0, add it
        if carry > 0:
            res.append(str(carry))

        return "".join(res[::-1])

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = list(num1)
        l2 = list(num2)

        s1 = len(l1)
        s2 = len(l2)

        if s1 <= s2:
            return self.addfunc(l1, l2, s1, s2)
        else:
            return self.addfunc(l2, l1, s2, s1)