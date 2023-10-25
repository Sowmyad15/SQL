class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        sorted(d)
        lst=min(d.values())
        for i in d:
            if lst==d[i]:
                return i
       