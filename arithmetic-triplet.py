# TRASH PERFORMANCE
def poorArithmeticTriplets(nums: list[int], diff: int) -> int:
    triplets_amount = 0

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                if nums[k] - nums[j] == diff and nums[j] - nums[i] == diff:
                    triplets_amount += 1

    return triplets_amount


result = poorArithmeticTriplets([0, 1, 4, 6, 7, 10], 3)

# print(result)  # should be 2


def arithmeticTriplets(nums: list[int], diff: int) -> int:
    nums_dict = dict()
    triplets_amount = 0

    for n in nums:
        nums_dict[n] = n

    for i in nums:
        j = i + diff
        k = i + diff * 2

        if j in nums_dict and k in nums_dict:
            triplets_amount += 1

    return triplets_amount


result = arithmeticTriplets([0, 1, 4, 6, 7, 10], 3)

print(result)
