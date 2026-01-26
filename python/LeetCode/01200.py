from typing import List

def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
    arr.sort()
    n = len(arr)
    min_abs_diff = abs(arr[0] - arr[1])

    output = []
    for i in range(n):
        for j in range(i + 1, n):
            diff = abs(arr[i] - arr[j])
            if diff > min_abs_diff:
                break

            segment = sorted([arr[i], arr[j]])
            if diff < min_abs_diff:
                output.clear()
                output.append(segment)
                min_abs_diff = diff
            elif diff == min_abs_diff:
                output.append(segment)

    return output
