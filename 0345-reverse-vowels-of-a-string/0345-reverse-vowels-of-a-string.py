class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst=list(s)
        vowel='AEIOUaeiou'
        f=0
        l=len(s)-1
        while f<l:
            if lst[f] in vowel and lst[l] in vowel:
                lst[f],lst[l]=lst[l],lst[f]
                f=f+1
                l=l-1
            elif lst[f] not in vowel:
                f=f+1
            elif lst[l] not in vowel:
                l=l-1
            else:
                f=f+1
                l=l-1
    
            

        return "".join(lst)
