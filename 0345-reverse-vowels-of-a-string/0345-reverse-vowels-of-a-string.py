class Solution:
    def reverseVowels(self, s: str) -> str:
        vow=[]
        for i in range(len(s)):
            if s[i] in "AEIOUaeiou":
                vow.append(s[i])
        s2=vow[::-1]
        s=list(s)
        k=0
        for i in range(len(s)):
            if s[i] in "AEIOUaeiou":
                s[i]=s2[k]
                k+=1
        return "".join(s)
            
        