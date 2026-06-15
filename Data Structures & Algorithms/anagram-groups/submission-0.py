class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_map = defaultdict(list)
        for s in strs:
            bitmap = [0] * 26
            for ch in s:
                bitmap[ord(ch) - ord('a')] += 1
            tup = tuple(bitmap)
            s_map[tup].append(s)

        return [pairs for pairs in s_map.values()]
