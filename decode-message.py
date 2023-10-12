def decodeMessage(key: str, message: str) -> str:
    alphabet_letters = "abcdefghijklmnopqrstuvwxyz"
    cipher_dict = dict()
    output = ""
    currentLetterIndex = 0

    for letter in key:
        if letter == " ":
            continue

        if letter not in cipher_dict:
            cipher_dict[letter] = alphabet_letters[currentLetterIndex]
            currentLetterIndex += 1

    for letter in message:
        if letter == " ":
            output += " "
        else:
            output += cipher_dict.get(letter)

    return output


result = decodeMessage(
    "the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"
)

print(result)

result = decodeMessage(
    "eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
)

print(result)
