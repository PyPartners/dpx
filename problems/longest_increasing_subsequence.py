from typing import List, Tuple, Dict

# --- Problem: Longest Increasing Subsequence (LIS) ---
# Given an array of integers, find the length of the longest subsequence
# in which all elements are sorted in strictly increasing order.
# A subsequence is derived from an array by deleting some or no elements
# without changing the order of the remaining elements.
# Example: For [10, 9, 2, 5, 3, 7, 101, 18], the LIS is [2, 3, 7, 101], so the length is 4.

# ======================================================================================
# Approach 1: Tabulation (Bottom-Up Dynamic Programming) - O(n^2)
# ======================================================================================
def longest_increasing_subsequence_tabulation_n2(nums: List[int]) -> int:
    """
    Calculates the length of the Longest Increasing Subsequence (LIS)
    using O(n^2) tabulation dynamic programming.

    Args:
        nums: A list of integers.

    Returns:
        The length of the LIS.
    """
    n: int = len(nums)
    if n == 0:
        return 0

    # dp[i] will store the length of the LIS ending at index i,
    # where nums[i] is the last element of that LIS.
    # Initialize all LIS lengths to 1 (each element itself is an LIS of length 1).
    dp: List[int] = [1] * n

    # Iterate through the array to fill the dp table
    for i in range(n):
        # For each element nums[i], check all previous elements nums[j] (where j < i)
        for j in range(i):
            # If nums[i] is greater than nums[j], it means nums[i] can extend
            # the increasing subsequence ending at nums[j].
            if nums[i] > nums[j]:
                # The new LIS length ending at nums[i] would be dp[j] + 1.
                # We want the maximum such length.
                dp[i] = max(dp[i], dp[j] + 1)

    # The length of the LIS for the entire array is the maximum value in the dp table,
    # as the LIS can end at any element.
    if not dp: # Should not happen if n > 0, but good for empty nums edge case
        return 0
    return max(dp)

# ======================================================================================
# Approach 2: Optimized Dynamic Programming with Patience Sorting Intuition - O(n log n)
# ======================================================================================
def longest_increasing_subsequence_optimized_nlogn(nums: List[int]) -> int:
    """
    Calculates the length of the Longest Increasing Subsequence (LIS)
    using an optimized O(n log n) approach based on patience sorting.

    This method maintains a list `tails` where `tails[i]` is the smallest tail
    of all increasing subsequences of length `i+1`. This list `tails` is
    always sorted.

    Args:
        nums: A list of integers.

    Returns:
        The length of the LIS.
    """
    n: int = len(nums)
    if n == 0:
        return 0

    # `tails` will store the smallest tail of all increasing subsequences
    # with length i+1. `tails[k]` is the smallest ending element of an
    # increasing subsequence of length `k+1`.
    # This list is key because it will always be sorted.
    tails: List[int] = []

    for num in nums:
        # If `tails` is empty or `num` is greater than the largest tail,
        # it means `num` can extend the longest increasing subsequence found so far.
        if not tails or num > tails[-1]:
            tails.append(num)
        else:
            # If `num` is not greater than the largest tail, we want to find
            # the smallest tail in `tails` that is greater than or equal to `num`.
            # We then replace that tail with `num`. This helps us find shorter
            # LIS but with a smaller tail, potentially allowing more elements later.
            # This is equivalent to finding the "leftmost" insertion point for `num`
            # to maintain the sorted order of `tails`.

            # Binary search for the insertion point (first element >= num)
            low: int = 0
            high: int = len(tails) - 1
            # `insertion_point` will be the index where `num` should be placed
            # to keep `tails` sorted.
            insertion_point: int = high + 1 # Default if num is larger than all

            while low <= high:
                mid: int = low + (high - low) // 2
                if tails[mid] >= num:
                    insertion_point = mid
                    high = mid - 1
                else:
                    low = mid + 1
            
            # If a suitable position is found (insertion_point is valid index), update tails.
            # This step is crucial: we are not necessarily extending an existing subsequence,
            # but rather finding a new potential subsequence of the same length with a smaller tail.
            tails[insertion_point] = num

    # The length of the `tails` list at the end is the length of the LIS.
    return len(tails)

# ======================================================================================
# Reconstructing the LIS (typically from the O(n^2) approach for simplicity)
# ======================================================================================
def get_lis_string_n2(nums: List[int]) -> List[int]:
    """
    Reconstructs one of the Longest Increasing Subsequences using the O(n^2) DP approach.
    Note: There can be multiple LIS. This returns one of them.

    Args:
        nums: A list of integers.

    Returns:
        A list representing one of the LIS.
    """
    n: int = len(nums)
    if n == 0:
        return []

    dp: List[int] = [1] * n  # dp[i] = length of LIS ending at nums[i]
    # `parent[i]` will store the index of the element that precedes nums[i]
    # in the LIS ending at nums[i]. Initialize with -1 (no predecessor).
    parent: List[int] = [-1] * n

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j # nums[j] is the predecessor of nums[i]

    if not dp:
        return []
        
    max_length: int = 0
    end_index: int = -1

    # Find the maximum length in dp and its index
    for i in range(n):
        if dp[i] > max_length:
            max_length = dp[i]
            end_index = i
    
    if end_index == -1: # Should only happen if nums is empty and handled above
        return []

    # Reconstruct the LIS by backtracking using the parent array
    lis: List[int] = []
    current_index: int = end_index
    while current_index != -1:
        lis.append(nums[current_index])
        current_index = parent[current_index]

    return list(reversed(lis)) # Reverse to get the correct order

# ======================================================================================
# Test Block
# ======================================================================================
if __name__ == "__main__":
    print("--- Longest Increasing Subsequence Problem ---")

    test_cases: List[Tuple[List[int], int, List[int]]] = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4, [2, 3, 7, 101]), # or [2, 5, 7, 101], [2,3,7,18], etc.
        ([0, 1, 0, 3, 2, 3], 4, [0, 1, 2, 3]),
        ([7, 7, 7, 7, 7, 7, 7], 1, [7]),
        ([], 0, []),
        ([1], 1, [1]),
        ([3, 4, -1, 0, 6, 2, 3], 4, [-1, 0, 2, 3]), # or [3,4,6] is LIS of length 3
                                                    # The expected list here implies one specific LIS
        ([10, 22, 9, 33, 21, 50, 41, 60, 80], 6, [10, 22, 33, 50, 60, 80]) # or other 6-length LIS
    ]

    for i, (arr, expected_length, expected_lis_example) in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"  Array: {arr}")

        # Test O(n^2) Tabulation
        length_n2: int = longest_increasing_subsequence_tabulation_n2(list(arr)) # Pass a copy
        print(f"  LIS Length (O(n^2) Tabulation): {length_n2}")
        assert length_n2 == expected_length, \
            f"O(n^2) Tabulation failed for {arr}. Expected {expected_length}, got {length_n2}"

        # Test O(n log n) Optimized Approach
        length_nlogn: int = longest_increasing_subsequence_optimized_nlogn(list(arr)) # Pass a copy
        print(f"  LIS Length (O(n log n) Optimized): {length_nlogn}")
        assert length_nlogn == expected_length, \
            f"O(n log n) Optimized failed for {arr}. Expected {expected_length}, got {length_nlogn}"

        # Test Reconstructing LIS string (from O(n^2) logic)
        # Note: There can be multiple LIS sequences. We check if the reconstructed one
        # is valid and has the correct length.
        reconstructed_lis: List[int] = get_lis_string_n2(list(arr))
        print(f"  Reconstructed LIS (from O(n^2)): {reconstructed_lis}")
        assert len(reconstructed_lis) == expected_length, \
            f"Reconstructed LIS for {arr} has length {len(reconstructed_lis)}, expected {expected_length}"

        # Validate if the reconstructed LIS is indeed an increasing subsequence
        if reconstructed_lis:
            is_increasing = all(reconstructed_lis[k] < reconstructed_lis[k+1] for k in range(len(reconstructed_lis)-1))
            assert is_increasing, f"Reconstructed LIS {reconstructed_lis} is not strictly increasing."
            
            # Check if it's a subsequence of the original array
            sub_iter = iter(arr)
            is_subsequence = all(elem in sub_iter for elem in reconstructed_lis)
            assert is_subsequence, f"Reconstructed LIS {reconstructed_lis} is not a subsequence of {arr}."
        elif expected_length != 0 : # If expected length is not 0, but we got an empty list
             assert False, f"Reconstructed LIS is empty for {arr}, but expected length {expected_length}"


    print("\nAll LIS tests passed successfully (or with valid alternatives)!")
