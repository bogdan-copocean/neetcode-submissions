class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map = defaultdict(int)
        for i in range(len(s)):
            s_map[s[i]] +=1
            s_map[t[i]] -=1

        for _, val in s_map.items():
            if val != 0:
                return False
        return True