def numIdenticalPairs(nums: list[int]) -> int:
  goodPairsAmount = 0

  for i in range(len(nums)):
      for j in range(len(nums)):
          if (nums[i] == nums[j] and i < j):
              goodPairsAmount += 1

  return goodPairsAmount

