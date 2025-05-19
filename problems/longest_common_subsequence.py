from typing import List, Dict, Tuple

# --- Problem: Longest Common Subsequence (LCS) ---
# Given two strings, find the length of the longest subsequence present in both of them.
# A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
# For example, "ace" is a subsequence of "abcde".

# ======================================================================================
# Approach 1: Memoization (Top-Down Dynamic Programming)
# ======================================================================================

def lcs_memoization_recursive(
    s1: str,
    s2: str,
    m: int,
    n: int,
    memo: Dict[Tuple[int, int], int]
) -> int:
    """
    Recursive helper function for LCS using memoization.

    Args:
        s1: The first string.
        s2: The second string.
        m: Current length of s1 being considered (number of characters from the end).
        n: Current length of s2 being considered.
        memo: A dictionary to store results of already computed subproblems.
              The key is a tuple (m, n), and the value is the LCS length.

    Returns:
        The length of the Longest Common Subsequence of s1[0...m-1] and s2[0...n-1].
    """
    # Base Case: If either string is empty, the LCS is 0.
    if m == 0 or n == 0:
        return 0

    # Check if this subproblem has already been solved
    if (m, n) in memo:
        return memo[(m, n)]

    # If the last characters of the current substrings match
    # Note: We use m-1 and n-1 because m and n are lengths,
    # so they are 1-based indices for string slicing/access.
    if s1[m - 1] == s2[n - 1]:
        # The matching character contributes 1 to the LCS.
        # We then recursively find the LCS of the remaining parts of the strings.
        memo[(m, n)] = 1 + lcs_memoization_recursive(s1, s2, m - 1, n - 1, memo)
    else:
        # If the last characters do not match, we have two choices:
        # 1. Exclude the last character of s1 and find LCS of s1[0...m-2] and s2[0...n-1].
        # 2. Exclude the last character of s2 and find LCS of s1[0...m-1] and s2[0...n-2].
        # We take the maximum of these two choices.
        result_option1: int = lcs_memoization_recursive(s1, s2, m - 1, n, memo)
        result_option2: int = lcs_memoization_recursive(s1, s2, m, n - 1, memo)
        memo[(m, n)] = max(result_option1, result_option2)

    return memo[(m, n)]

def longest_common_subsequence_memoization(s1: str, s2: str) -> int:
    """
    Calculates the length of the Longest Common Subsequence of two strings
    using the memoization (top-down) dynamic programming approach.

    Args:
        s1: The first string.
        s2: The second string.

    Returns:
        The length of the LCS.
    """
    m: int = len(s1)
    n: int = len(s2)
    memo: Dict[Tuple[int, int], int] = {}  # Memoization table

    # Call the recursive helper function
    return lcs_memoization_recursive(s1, s2, m, n, memo)


# ======================================================================================
# Approach 2: Tabulation (Bottom-Up Dynamic Programming)
# ======================================================================================

def longest_common_subsequence_tabulation(s1: str, s2: str) -> int:
    """
    Calculates the length of the Longest Common Subsequence of two strings
    using the tabulation (bottom-up) dynamic programming approach.

    Args:
        s1: The first string.
        s2: The second string.

    Returns:
        The length of the LCS.
    """
    m: int = len(s1)
    n: int = len(s2)

    # Create a DP table `dp[i][j]` which will store the length of LCS
    # of s1[0...i-1] and s2[0...j-1].
    # The table size is (m+1) x (n+1) to handle base cases (empty strings).
    dp: List[List[int]] = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill the dp table in a bottom-up manner.
    # i iterates through characters of s1 (from 1 to m)
    # j iterates through characters of s2 (from 1 to n)
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                # Base case: If one of the strings is empty, LCS is 0.
                dp[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                # If current characters match, LCS length is 1 + LCS of previous substrings.
                # s1[i-1] refers to the i-th character of s1 (0-indexed).
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                # If current characters don't match, LCS is the max of:
                # 1. LCS of s1[0...i-2] and s2[0...j-1] (excluding char from s1)
                # 2. LCS of s1[0...i-1] and s2[0...j-2] (excluding char from s2)
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The value at dp[m][n] contains the length of LCS for s1 and s2.
    return dp[m][n]


# ======================================================================================
# Bonus: Reconstructing the Longest Common Subsequence string
# (using the DP table from tabulation)
# ======================================================================================
def get_lcs_string(s1: str, s2: str) -> str:
    """
    Reconstructs one of the Longest Common Subsequences from the DP table
    generated by the tabulation method.

    Args:
        s1: The first string.
        s2: The second string.

    Returns:
        One of the actual LCS strings.
    """
    m: int = len(s1)
    n: int = len(s2)
    dp: List[List[int]] = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # First, fill the DP table (same as in tabulation for length)
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Now, backtrack from dp[m][n] to construct the LCS string
    lcs_str_chars: List[str] = []
    i: int = m
    j: int = n

    while i > 0 and j > 0:
        # If current characters in s1 and s2 are same, then
        # this character is part of LCS
        if s1[i - 1] == s2[j - 1]:
            lcs_str_chars.append(s1[i - 1])
            i -= 1  # Move diagonally up-left
            j -= 1
        # If current characters are not same, then find the larger
        # of two and go in the direction of larger value
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1  # Move up
        else:
            j -= 1  # Move left

    # The characters are added in reverse order, so reverse the list and join
    return "".join(reversed(lcs_str_chars))


# ======================================================================================
# Test Block
# ======================================================================================
if __name__ == "__main__":
    print("--- Longest Common Subsequence Problem ---")

    test_cases: List[Tuple[str, str, int, str]] = [
        ("AGGTAB", "GXTXAYB", 4, "GTAB"),
        ("ABCDGH", "AEDFHR", 3, "ADH"),
        ("ABC", "XYZ", 0, ""),
        ("AAAA", "AA", 2, "AA"),
        ("abcdef", "ace", 3, "ace"),
        ("abc", "abc", 3, "abc"),
        ("sea", "eat", 2, "ea"), # or "et", but "ea" is also valid for some paths.
                                  # My implementation picks one consistent path.
        ("XMJYAUZ", "MZJAWXU", 4, "MJAU") # or "MZJU" etc.
    ]

    for i, (s1, s2, expected_length, expected_lcs_str) in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"  String 1: \"{s1}\"")
        print(f"  String 2: \"{s2}\"")

        # Test Memoization
        length_memo: int = longest_common_subsequence_memoization(s1, s2)
        print(f"  LCS Length (Memoization): {length_memo}")
        assert length_memo == expected_length, \
            f"Memoization failed for ({s1}, {s2}). Expected {expected_length}, got {length_memo}"

        # Test Tabulation
        length_tab: int = longest_common_subsequence_tabulation(s1, s2)
        print(f"  LCS Length (Tabulation):  {length_tab}")
        assert length_tab == expected_length, \
            f"Tabulation failed for ({s1}, {s2}). Expected {expected_length}, got {length_tab}"
        
        # Test Reconstructing LCS string
        lcs_reconstructed_str: str = get_lcs_string(s1, s2)
        print(f"  Reconstructed LCS String: \"{lcs_reconstructed_str}\"")
        # Note: There can be multiple LCS strings. The check below might need adjustment
        # if a different valid LCS is produced by the reconstruction algorithm.
        # For simplicity, we check if the length is correct and if it's one of the known valid ones.
        assert len(lcs_reconstructed_str) == expected_length, \
             f"Reconstructed LCS string length mismatch for ({s1}, {s2}). Expected {expected_length}, got {len(lcs_reconstructed_str)}"
        # A more robust check for the string itself might involve generating all possible LCS strings
        # or ensuring the reconstructed one IS a subsequence of both and has the correct length.
        # For this example, we'll assume our 'expected_lcs_str' is one of the valid ones produced by our logic.
        if s1 == "sea" and s2 == "eat": # Special case for "sea", "eat" where "et" is also valid
             assert lcs_reconstructed_str in ("ea", "et"), f"LCS string for ('sea', 'eat') was '{lcs_reconstructed_str}', expected 'ea' or 'et'"
        elif s1 == "XMJYAUZ" and s2 == "MZJAWXU": # Multiple valid LCSs like MJAU, MZJU
            valid_lcs_options = ["MJAU", "MZAU", "MZJU", "MZAWXU"] # This example might be too complex for simple string match
            # A better check: is lcs_reconstructed_str a subsequence of s1 and s2 and has length expected_length
            is_subsequence = lambda sub, main: (it := iter(main), all(c in it for c in sub))[1]
            assert is_subsequence(lcs_reconstructed_str, s1) and is_subsequence(lcs_reconstructed_str, s2) and len(lcs_reconstructed_str) == expected_length, \
                f"Reconstructed LCS '{lcs_reconstructed_str}' is not a valid LCS for ('{s1}', '{s2}')"
        else:
            assert lcs_reconstructed_str == expected_lcs_str, \
                f"Reconstructed LCS string mismatch for ({s1}, {s2}). Expected \"{expected_lcs_str}\", got \"{lcs_reconstructed_str}\""


    print("\nAll tests passed successfully for LCS!")
