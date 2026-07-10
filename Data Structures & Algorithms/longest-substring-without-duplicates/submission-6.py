class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window
        if not s:
            return 0
        seen=set()
        l=0
        maxl=0
        for i in range(len(s)):
            if s[i] in seen:
                while s[i] in seen:
                    seen.remove(s[l])
                    l+=1
            
            seen.add(s[i])
            maxl=max(i-l+1,maxl)
        return maxl




        


        