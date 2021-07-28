def twoSum(self, nums, target):
    """
    type nums : List[int]
    type target: int
    rtype List[int]
    """
    dict = {}
    for i in range(len(nums)):
       if target -nums[i] not in dict:
            dict[nums[i]] = i
       else:
           return [dict[target-nums[i]],i]
if __name__ == "__main__":
    nums = [2,7,11,24]
    target = 9
    tt = twoSum(' ', nums, target)
    print(tt)

