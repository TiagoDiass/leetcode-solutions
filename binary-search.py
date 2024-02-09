def binarySearch(self, array: List[int], target: int) -> int:
        start = 0
        end = len(array) - 1

        while start <= end:
            mid = (start + end) // 2

            if array[mid] == target:
                while mid > 0 and array[mid - 1] == target:
                    mid -= 1
            
                return mid

            if array[mid] > target:
                end = mid - 1

            if array[mid] < target:
                start = mid + 1

        return -1
