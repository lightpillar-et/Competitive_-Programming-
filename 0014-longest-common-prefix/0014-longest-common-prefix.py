class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i in range (len(strs[0])):
            ch = strs[0][i]
            for j in strs :
                if i == len(j) or j[i] != ch :
                    return ans
            ans += ch
        return ans 