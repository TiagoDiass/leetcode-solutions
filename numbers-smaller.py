def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    result = []

    for i in range(len(nums)):
        elementsSmallerThanCurrentElement = 0

        for j in range(len(nums)):
            if nums[j] < nums[i]:
                elementsSmallerThanCurrentElement += 1

        result.append(elementsSmallerThanCurrentElement)

    return result


smallerNumbersThanCurrent([8, 1, 2, 2, 3])
