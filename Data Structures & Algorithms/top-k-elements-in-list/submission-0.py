class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #[1,2,2,3,3,3,]
        #map_values = {1: 1, 2:2, 3:3}
        #freq counts = {3,2,1}

        map_values = {}
        for i in nums:
            map_values[i] = 1 + map_values.get(i,0)
        freq_counts = sorted(list(map_values.values()),reverse = True)
        ans = []
        for i in range(k):
            target_freq = freq_counts[i]

            for key,val in map_values.items():
                if val == target_freq and key not in ans:
                    ans.append(key)
                    break
        
        return ans



        