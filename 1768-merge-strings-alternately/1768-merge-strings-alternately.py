class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        list=[]
        i=0
        while i <len(word1) and i<len(word2):
            list.append(word1[i])
            list.append(word2[i])
            i+=1
        list.append(word1[i:])
        list.append(word2[i:])
        return "".join(list)