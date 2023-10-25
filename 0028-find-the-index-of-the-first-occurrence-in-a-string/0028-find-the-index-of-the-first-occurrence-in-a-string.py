class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        h1=len(haystack)
        h2=len(needle)
        for i in range(h1):
            ch=haystack[i:h2+i]
            if ch==needle:
                return i
        return -1

