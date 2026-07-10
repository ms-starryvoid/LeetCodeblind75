class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        window={}
        need={}
        left=0
        for ch in t:
            need[ch]=need.get(ch,0)+1
        
        needCount=len(need)
        res=[-1,-1]
        have=0
        resL=float('inf')
        for right in range(len(s)):
            window[s[right]]=window.get(s[right],0)+1
            if s[right] in need and window[s[right]]==need[s[right]]:
                have+=1
            while have==needCount:
                if (right-left+1) < resL:
                    resL=right-left+1
                    res=[left,right]
                window[s[left]]-=1
                if s[left] in need and window[s[left]]<need[s[left]]:
                    have-=1
                left+=1
                l,r=res
        return s[l:r+1] if resL!=float('inf') else ""
            
    
            
            
