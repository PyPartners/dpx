# Understanding Fibonacci with Dynamic Programming

The Fibonacci sequence is a famous series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.
So, it goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on.
Mathematically:
*   F(0) = 0
*   F(1) = 1
*   F(n) = F(n-1) + F(n-2) for n > 1

A naive recursive approach to calculate F(n) would be very inefficient because it recalculates the same Fibonacci numbers many times. Dynamic Programming (DP) helps us solve this efficiently by storing the results of subproblems so we don't have to compute them again.

We explored two main DP techniques:

## 1. Memoization (Top-Down Approach)

Think of memoization as "smart recursion" or "remembering what you've already done."
We start by trying to solve the main problem (e.g., F(5)) from the top. If we need a smaller piece (e.g., F(3)) that we've already figured out, we just look up its answer instead of re-calculating it.

**How it works in our code (`fibonacci_with_memoization` or `fibonacci_memo_cleaner`):**

1.  **The "Memo Pad":** We use a dictionary (like `memo_pad` or `cache`) to store the Fibonacci numbers we've already computed. The key is the number `n`, and the value is `F(n)`.
2.  **Check the Pad First:** When the function is called for a number `n`:
    *   It first checks if `n` is already in our `memo_pad`.
    *   If yes, great! We just return the stored value.
3.  **Base Cases:** If `n` is 0 or 1 (the simplest cases), we return 0 or 1 respectively.
4.  **Calculate and Remember:** If `n` is not in the `memo_pad` and not a base case:
    *   We calculate `F(n)` by recursively calling the function for `F(n-1)` and `F(n-2)`.
    *   **Crucially**, before returning the result, we store it in our `memo_pad`. So, `memo_pad[n] = result`.
    *   Then, we return the result.

The `fibonacci_memo_cleaner` function provides a slightly neater way by encapsulating the cache within the function scope, making it fresh for each top-level call if needed, avoiding reliance on a global variable.

## 2. Tabulation (Bottom-Up Approach)

Think of tabulation as "building up" the solution from the very beginning. Instead of starting from F(n) and going down, we start from F(0) and F(1) and work our way up to F(n).

**How it works in our code (`fibonacci_with_tabulation`):**

1.  **The "Table":** We create a list (or an array), let's call it `fib_table`, to store the Fibonacci numbers. The size of this table will be `n + 1` to store values from F(0) up to F(n).
2.  **Seed the Base Cases:** We know F(0) and F(1). So, we fill these in first:
    *   `fib_table[0] = 0`
    *   `fib_table[1] = 1`
3.  **Fill the Table Iteratively:** We then loop from `i = 2` up to `n`. In each step of the loop, we calculate `fib_table[i]` using the values we've already computed and stored in our table:
    *   `fib_table[i] = fib_table[i-1] + fib_table[i-2]`
4.  **The Final Answer:** After the loop finishes, the value for `F(n)` will be stored in `fib_table[n]`, which we then return.

## Conclusion

Both memoization and tabulation are powerful dynamic programming techniques that significantly improve the efficiency of calculating Fibonacci numbers by ensuring that each Fibonacci subproblem is solved only once.

The Python code demonstrating these methods can be found in a file like `fibonacci_dp.py` (or whatever you named it!).