class Solution:
    def shift_right(self, arr: list[int], start: int, k: int = 1) -> None:
        for i in range(len(arr) - 1, start + k - 1, -1):
            arr[i] = arr[i - k]
        for i in range(start, min(start + k, len(arr))):
            arr[i] = 0

    def duplicateZeros(self, arr: list[int]) -> None:
        ptr = 0
        while ptr < len(arr):
            if arr[ptr] == 0:
                self.shift_right(arr, ptr)
                ptr += 1
            ptr += 1
