class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        for i in range(0,len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        lis=[]
        res=[]
        for i in d.values():
            lis.append(i)
        lis.sort()
        lis=lis[-k:]
        print(lis)
        for i in lis:
            for j in d:
                if d[j]==i and j not in res:
                    res.append(j)
        return sorted(res)