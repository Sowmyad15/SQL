class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1=list(word1)
        word2=list(word2)
        merged=[]
        i=0
        j=0
        k=0
        while i<len(word1) and j<len(word2):
            if k%2==0:
                merged.append(word1[i])
                i=i+1  
            else:
                merged.append(word2[j])
                j=j+1
            k=k+1
              
        while i<len(word1):
            merged.append(word1[i])
            i=i+1
        while j<len(word2):
            merged.append(word2[j])
            j=j+1
        return "".join(merged)
           
        