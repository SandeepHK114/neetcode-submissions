class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #map = {pots: (pots,tops)}
        
        char_map = {}
        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
            if s not in char_map.keys():
                char_map[s] = []

            char_map[s].append(strs[i])
        
        return list(char_map.values())

        
