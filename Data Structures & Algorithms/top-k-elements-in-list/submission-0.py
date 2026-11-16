class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        
        
        res = {}
        for n in nums:
            res[n] = res.get(n, 0) + 1
        sorted_nums = sorted(res.keys(), key=lambda x: res[x], reverse=True)
        return sorted_nums[:k]