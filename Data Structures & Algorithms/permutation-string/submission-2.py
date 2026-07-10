class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ln=len(s2)
        if ln< len(s1):
            return False
        l=0
        r=0
        freq1={}
        freq2={}
        while r<len(s1):
            freq2[s2[r]]=freq2.get(s2[r],0)+1
            freq1[s1[r]]=freq1.get(s1[r],0)+1
            r+=1
        while r< ln:
            if freq1==freq2:
                return True
            freq2[s2[l]]-=1
            if freq2[s2[l]]==0:
                del freq2[s2[l]]
            l+=1
            freq2[s2[r]]=freq2.get(s2[r],0)+1
            r+=1
        return freq1==freq2

        
        