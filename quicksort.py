import math

def quicksort(numbers):
  if (len(numbers) < 2):
    return numbers
  else:
    pivotIndex = math.floor(len(numbers) / 2)
    pivot = numbers[pivotIndex]

    lowerThanPivot = []
    greaterThanPivot = []

    for i, n in enumerate(numbers):
      if (i == pivotIndex): continue

      if (n <= pivot): lowerThanPivot.append(n)
      else: greaterThanPivot.append(n)

    return quicksort(lowerThanPivot) + [pivot] + quicksort(greaterThanPivot)
  
sample1 = [33, 15, 10]
sample2 = [33, 15, 10, 125, 25, 3, 6]
sample3 = [3, 5, 1, 19, 26, 35]

sample1_result = quicksort(sample1)
sample2_result = quicksort(sample2)
sample3_result = quicksort(sample3)

print(sample1, sample1_result)
print(sample2, sample2_result)
print(sample3, sample3_result)
