class Solution:
    def reverseString(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    def reverseStr(self, s, k):
        values = list(s)
        result = []

        while len(values) > 0:

            if len(values) >= 2 * k:
                tmp = values[:2 * k]
                del values[:2 * k]

                self.reverseString(tmp, 0, k - 1)
                result.extend(tmp)

            elif len(values) < k:
                self.reverseString(values, 0, len(values) - 1)
                result.extend(values)
                break

            else:
                tmp = values[:]
                self.reverseString(tmp, 0, k - 1)
                result.extend(tmp)
                break

        return "".join(result)
