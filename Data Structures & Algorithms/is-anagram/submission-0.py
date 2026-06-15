class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map = defaultdict(int)
        for ch in s:
            s_map[ch] +=1
        for ch in t:
            s_map[ch] -=1

        for _, val in s_map.items():
            if val != 0:
                return False
        return True