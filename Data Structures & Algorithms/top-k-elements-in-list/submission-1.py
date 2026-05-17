class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=defaultdict(int)
        count=0
        for i in nums:
            d[i]+=1
        sorted_items= sorted(d.items(),key=lambda x: x[1],reverse=True)
        
        return [item[0] for item in sorted_items[:k]]
