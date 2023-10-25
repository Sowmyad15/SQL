class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_n=(len(nums)*(len(nums)+1))/2
        sum_list=sum(nums)
        return sum_n-sum_list
        