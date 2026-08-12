class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a....z
            for c in s:  # for every char in each string
                count[ord(c) - ord('a')] += 1              # add count 1 to each char using its ascii value - 'a' ascii value     
            res[tuple(count)].append(s)       # Once we've identified the key (the tuple), we append the current string s to the list of values for that key.




        return list(res.values())
