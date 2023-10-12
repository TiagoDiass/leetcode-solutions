def numJewelsInStones(jewels: str, stones: str) -> int:
  jewelsAmount = 0

  for ch in stones:
      if (ch in jewels): 
          jewelsAmount += 1

  return jewelsAmount

print(numJewelsInStones('ABCDefg', 'zxyABcdEFG'))