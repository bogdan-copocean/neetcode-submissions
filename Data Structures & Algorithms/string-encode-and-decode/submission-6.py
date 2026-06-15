class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = []
        for sstr in strs:
            enc.append(f"{len(sstr)}!")
            enc.append(sstr)
        return "".join(enc)
                
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        # 123!Worldasdsd

        while i < len(s):
            j = i
            while s[j] != "!":
                j += 1

            ln = int(s[i:j])
            i = j + 1
            j = i + ln
            res.append(s[i:j])
            i = j

        return res






       