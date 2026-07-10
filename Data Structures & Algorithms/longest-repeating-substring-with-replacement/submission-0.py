class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap={}
        ln=len(s)
        l=0
        r=0
        maxl=0
        while r<ln:
            hashMap[s[r]]=hashMap.get(s[r],0) +1
            while (r-l+1) - max(hashMap.values()) > k:
                hashMap[s[l]]-=1
                l+=1
            maxl=max(maxl,r-l+1)
            r+=1
        return maxl
           

        