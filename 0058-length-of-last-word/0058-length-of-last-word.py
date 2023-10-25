class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst=s.split(" ")
        while "" in lst:
            lst.remove("")
        x=lst[-1]
    
        return len(x)