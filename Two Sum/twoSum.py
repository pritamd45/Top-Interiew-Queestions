class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        res=[]
        for i in range(len(nums)):
            if (target-nums[i]) in d:
                res.append(d[target-nums[i]])
                res.append(i)
            else:
                d[nums[i]]=i
        return res