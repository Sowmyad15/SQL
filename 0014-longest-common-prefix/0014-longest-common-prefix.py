class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix=min(strs,key=len)
        print(prefix)
        for s in strs:
            while not s.startswith(prefix):
                prefix=prefix[:-1]
        return prefix