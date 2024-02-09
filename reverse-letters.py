def reverseLetters(s):
    outputArr = [None] * len(s)
    left, right = 0, len(s) - 1

    while left < right:
        leftCh = s[left].lower()
        rightCh = s[right].lower()

        isLeftChLetter = 97 <= ord(leftCh) <= 122
        isRightChLetter = 97 <= ord(rightCh) <= 122

        if isLeftChLetter and isRightChLetter:
            outputArr[left] = rightCh
            outputArr[right] = leftCh

            left += 1
            right -= 1
            continue

        if not isLeftChLetter:
            outputArr[left] = leftCh
            left += 1

        if not isRightChLetter:
            outputArr[right] = rightCh
            right -= 1

    print(outputArr)


print(reverseLetters("ab-cd"))  # dc-ba
print(reverseLetters("a-Bc-deF!!"))  # F-ed-cBa!!
