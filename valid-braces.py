# THIS PROBLEM WAS NOT SEEN IN LEETCODE, I ACTUALLY TOOK IT FROM TURING
from collections import deque


def validBraces(s: str) -> str:
    if len(s) % 2 != 0:
        return "invalid"

    charStack = deque()

    for ch in s:
        if ch == "{" or ch == "[" or ch == "(":
            charStack.append(ch)
            continue

        lastChar = charStack.pop()
        combination = lastChar + ch

        if combination != "{}" and combination != "[]" and combination != "()":
            return "invalid"

    return "valid"


print("VALID CASES --------")
print(validBraces("(){}[]"))
print(validBraces("{}{}[]()"))
print(validBraces("[]()()()"))
print(validBraces("({([])})"))
print(validBraces("{{([])}}"))

print("INVALID CASES --------")
print(validBraces("[]()]"))
print(validBraces("[](]"))
print(validBraces("(]{)"))
print(validBraces("({]})"))
