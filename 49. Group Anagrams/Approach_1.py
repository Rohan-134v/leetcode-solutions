class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            arr = "".join(sorted(s))
            result[arr].append(s)
        
        return list(result.values())
