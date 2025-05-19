# Longest Increasing Subsequence (LIS)

## Problem Statement

Given an array of integers, find the length of the longest subsequence in which all elements are sorted in strictly increasing order. A subsequence is derived from the original array by deleting zero or more elements without changing the order of the remaining elements.

For example, given the array `[10, 9, 2, 5, 3, 7, 101, 18]`, one LIS is `[2, 3, 7, 101]`, and its length is 4. Other LISs of the same length might exist, like `[2, 5, 7, 101]` or `[2, 3, 7, 18]`.

## Dynamic Programming Approaches

### 1. Tabulation (Bottom-Up DP) - O(n²)

This is a more straightforward DP approach.
Let `dp[i]` be the length of the Longest Increasing Subsequence that *ends* at index `i` (i.e., `nums[i]` is the last element of this LIS).

**Initialization:**
*   Initialize `dp[i] = 1` for all `i` from `0` to `n-1`. This is because each element itself forms an LIS of length 1.

**Iteration:**
*   Iterate `i` from `0` to `n-1` (for each element `nums[i]`):
    *   Iterate `j` from `0` to `i-1` (for all elements `nums[j]` before `nums[i]`):
        *   If `nums[i] > nums[j]`: This means `nums[i]` can extend an increasing subsequence ending at `nums[j]`.
        *   The length of such an LIS would be `dp[j] + 1`.
        *   Update `dp[i] = max(dp[i], dp[j] + 1)`.

**Result:**
*   The length of the LIS for the entire array is the maximum value in the `dp` array, because the LIS can end at any index. `max(dp)`.

**Time Complexity:** `O(n^2)` due to the nested loops.
**Space Complexity:** `O(n)` for the `dp` array.

### 2. Optimized Approach with Patience Sorting Intuition - O(n log n)

This approach is more efficient and draws intuition from Patience Sorting. We maintain a list, let's call it `tails`.
`tails[k]` stores the smallest ending element of an increasing subsequence of length `k+1`.
This `tails` list will always be sorted in increasing order.

**Algorithm:**
1.  Initialize an empty list `tails`.
2.  Iterate through each number `num` in the input array `nums`:
    *   **Case 1:** If `tails` is empty or `num` is greater than `tails[-1]` (the largest element in `tails`):
        This means `num` can extend the longest increasing subsequence found so far. Append `num` to `tails`. The length of the LIS increases by 1.
    *   **Case 2:** If `num` is not greater than `tails[-1]`:
        We need to find an increasing subsequence of some length `k+1` that ends with a smaller number than `num`.
        Find the smallest element in `tails` that is greater than or equal to `num`. This can be done using binary search (e.g., `bisect_left` in Python or a manual binary search). Let this element be `tails[j]`.
        Replace `tails[j]` with `num`. This step is crucial: we are not necessarily extending an existing subsequence directly, but rather we are saying: "For subsequences of length `j+1`, we've now found one that ends with `num`, which is smaller (or equal) to the previous `tails[j]`. This might allow us to build longer subsequences later on."

3.  **Result:** The length of the `tails` list at the end of the iteration is the length of the LIS.

**Example Trace for `[10, 9, 2, 5, 3, 7, 101, 18]`:**
*   `num = 10`: `tails = [10]`
*   `num = 9`: `tails = [9]` (9 replaces 10, LIS of length 1 ends with 9)
*   `num = 2`: `tails = [2]` (2 replaces 9)
*   `num = 5`: `tails = [2, 5]`
*   `num = 3`: `tails = [2, 3]` (3 replaces 5)
*   `num = 7`: `tails = [2, 3, 7]`
*   `num = 101`: `tails = [2, 3, 7, 101]`
*   `num = 18`: `tails = [2, 3, 7, 18]` (18 replaces 101)

Final `tails` list length is 4.

**Time Complexity:** `O(n log n)`. Iterating through `n` numbers. For each number, the binary search on `tails` takes `O(log k)` where `k` is the current length of `tails` (at most `n`).
**Space Complexity:** `O(n)` in the worst case for the `tails` list (e.g., if the input array is already sorted).

### Reconstructing the LIS

Reconstructing the actual LIS sequence is more straightforward with the `O(n^2)` DP approach.
1.  During the DP table calculation, store `parent[i]` as the index `j` that led to `dp[i] = dp[j] + 1`.
2.  Find the index `end_index` where `dp[end_index]` is maximum. This `nums[end_index]` is the last element of one LIS.
3.  Backtrack from `end_index` using the `parent` array until `parent[current_index]` is -1 (or some initial marker). Collect the `nums[current_index]` values.
4.  Reverse the collected list to get the LIS in the correct order.

Reconstructing the LIS from the `O(n log n)` approach is more complex and typically involves storing predecessor indices or values during the `tails` list updates.

## Time and Space Complexity Summary

| Approach                                     | Time Complexity | Space Complexity |
| -------------------------------------------- | --------------- | ---------------- |
| Tabulation (DP)                              | `O(n^2)`        | `O(n)`           |
| Optimized (Patience Sorting / Binary Search) | `O(n log n)`    | `O(n)`           |

## Example Usage (Python)

```python
from longest_increasing_subsequence import (
    longest_increasing_subsequence_tabulation_n2,
    longest_increasing_subsequence_optimized_nlogn,
    get_lis_string_n2
)

nums_arr = [10, 9, 2, 5, 3, 7, 101, 18]

# Using O(n^2) Tabulation
length_n2 = longest_increasing_subsequence_tabulation_n2(list(nums_arr))
print(f"LIS Length (O(n^2)) for {nums_arr}: {length_n2}")
# Expected Output: LIS Length (O(n^2)) for [10, 9, 2, 5, 3, 7, 101, 18]: 4

# Using O(n log n) Optimized Approach
length_nlogn = longest_increasing_subsequence_optimized_nlogn(list(nums_arr))
print(f"LIS Length (O(n log n)) for {nums_arr}: {length_nlogn}")
# Expected Output: LIS Length (O(n log n)) for [10, 9, 2, 5, 3, 7, 101, 18]: 4

# Reconstructing one LIS (using O(n^2) logic for simplicity)
lis_sequence = get_lis_string_n2(list(nums_arr))
print(f"One LIS sequence: {lis_sequence}")
# Expected Output (one possibility): One LIS sequence: [2, 3, 7, 18] or [2, 3, 7, 101] etc.
```
[`longest_increasing_subsequence.py`](https://github.com/PyPartners/dpx/blob/main/problems/longest_increasing_subsequence.py).
