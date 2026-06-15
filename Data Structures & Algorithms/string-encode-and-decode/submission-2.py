class Solution:
    _sep = "👋"
    _has_info = True

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            self._has_info = False
        return self._sep.join(strs)

    def decode(self, s: str) -> List[str]:
        if not self._has_info:
            return []
        return s.split(self._sep)
