class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wp = s.split(' ')

        return [*map(wp.index, wp)] == [*map(pattern.index, pattern)]