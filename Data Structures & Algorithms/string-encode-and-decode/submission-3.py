class Solution:
    _sep = "👋"
    _sign = "✍️"

    def encode(self, strs: List[str]) -> str:
        enc = []
        enc = self._sep.join(strs)
        if len(strs) == 0:
            enc += self._sign
        return enc
            
        

    def decode(self, s: str) -> List[str]:
        if s and s[-1] == self._sign:
            return [""]
        dec = s.split(self._sep)
        if dec[-1] == self._sign:
            dec.pop()
        return dec
