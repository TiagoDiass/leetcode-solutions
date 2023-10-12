def groupThePeople(groupSizes: list[int]) -> list[list[int]]:
    result = []
    groups = dict()

    for personId, size in enumerate(groupSizes):
        if size not in groups:
            groups[size] = []

        groups[size].append(personId)

        if len(groups[size]) == size:
            result.append(groups[size])
            groups[size] = []

    return result


print(groupThePeople([3, 3, 3, 3, 3, 1, 3]))
