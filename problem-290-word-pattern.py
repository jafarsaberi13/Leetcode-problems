class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:


        plist = list(pattern)
        slist = s.split()
        if len(plist) != len(slist):
            return False
        d = {}

        for i in range(len(plist)):
            if plist[i] in d:
                if d[plist[i]] != slist[i]:
                    return False
                    break
            else:
                if slist[i] in d.values():
                    return False
                    break
                d[plist[i]] = slist[i]
        else:
            return True