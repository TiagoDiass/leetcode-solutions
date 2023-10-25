# this is not the optimal solution, time complexity here is O(n²)
def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    alreadyUsed = {}  # index: True
    charactersMaps = []
    output = []

    for string in strs:
        chCount = {}

        for ch in string:
            if ch not in chCount:
                chCount[ch] = 1
            else:
                chCount[ch] += 1

        charactersMaps.append(chCount)

    for i in range(len(strs)):
        if i in alreadyUsed:
            continue

        stringAtI = strs[i]
        anagrams = [stringAtI]
        alreadyUsed[i] = True

        for j in range(i + 1, len(strs)):
            if j in alreadyUsed:
                continue

            stringAtJ = strs[j]

            if len(stringAtI) != len(stringAtJ):
                continue

            isAnagram = True
            for ch in charactersMaps[i]:
                if ch not in charactersMaps[j]:
                    isAnagram = False
                    break

                if charactersMaps[i][ch] != charactersMaps[j][ch]:
                    isAnagram = False
                    break

            if isAnagram:
                anagrams.append(stringAtJ)
                alreadyUsed[j] = True

        output.append(anagrams)

    return output
