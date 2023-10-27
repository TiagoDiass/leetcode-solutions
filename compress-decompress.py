def compress(string: str) -> str:
    if len(string) <= 1:
        return string

    output = ""
    lastLetter = ""
    lastLetterCount = 0

    for letter in string:
        if lastLetter == "":
            lastLetter = letter
            lastLetterCount = 1
            continue

        if letter != lastLetter:
            if lastLetterCount == 1:
                output += lastLetter
            else:
                output += lastLetter + str(lastLetterCount)

            lastLetter = letter
            lastLetterCount = 1
            continue

        lastLetterCount += 1

    if lastLetterCount == 1:
        output += lastLetter
    else:
        output += lastLetter + str(lastLetterCount)

    return output


def decompress(string: str) -> str:
    if len(string) <= 1:
        return string

    output = ""
    lastChar = ""

    for ch in string:
        if lastChar == "" or lastChar.isnumeric():
            lastChar = ch
            continue

        if ch.isnumeric():
            output += lastChar * int(ch)
            lastChar = ch
            continue

        output += lastChar
        lastChar = ch

    if not lastChar.isnumeric():
        output += lastChar

    return output


print("## COMPRESS -------")
print("aaaabbbcdddee ->", compress("aaaabbbcdddee"))
print("a ->", compress("a"))
print("aaccdefghhiijjkkkkkk ->", compress("aaccdefghhiijjkkkkkk"))

print("## DECOMPRESS -------")
print("a2b2c3defg3j ->", decompress("a2b2c3defg3j"))
print("a2c3def2 ->", decompress("a2c3def2"))
print("a ->", decompress("a"))
