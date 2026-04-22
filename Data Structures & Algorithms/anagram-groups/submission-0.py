class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            group_anagrams[sorted_s].append(s)

        return list(group_anagrams.values())
        