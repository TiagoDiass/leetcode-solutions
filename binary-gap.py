def solution(n):
  binary = bin(n)

  canStartCount = False
  gapsLengths = []
  currentGapLength = 0

  for ch in (binary[2:]):
    if ch == '1':
      canStartCount = True

      if currentGapLength > 0:
        gapsLengths.append(currentGapLength)
        currentGapLength = 0

    if ch == '0':
      if canStartCount:
        currentGapLength += 1

  if len(gapsLengths) == 0:
    return 0
  else:
    return max(gapsLengths)
      


# print(solution(529))
# print(solution(9))
# print(solution(1041))
# print(solution(32))
print(solution(20))
