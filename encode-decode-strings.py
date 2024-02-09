def encode(strs):
    output = ""

    for string in strs:
        output += str(len(string)) + "#" + string

    return output


def decode(string: str):
    expectedSize = int(string[0])
    currentCount = 0
    currentString = ""
    skipNext = False

    output = []

    for ch in string[2:]:
        if skipNext:
            skipNext = False
            continue

        if currentCount < expectedSize:
            currentString += ch
            currentCount += 1
            continue

        if currentCount == 0 and expectedSize == 0:
            expectedSize = int(ch)
            skipNext = True
            continue

        if currentCount == expectedSize:
            output.append(currentString)
            currentString = ""
            expectedSize = 0
            currentCount = 0
            continue

    return output


encoded = encode(["lint", "code", "love", "you"])
print(encoded)
print(decode(encoded))
