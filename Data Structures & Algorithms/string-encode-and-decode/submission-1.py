class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for word in strs:
            l=len(word)
            s=s+str(l)+"#"+word
        return s


    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        num=""
        while(i<len(s)):
            while(s[i]!='#'):
                num=num+s[i]
                i+=1
            n=int(num)
            w=s[i+1:i+n+1]
            result.append(w)
            i=i+n+1
            num=""
        return result


