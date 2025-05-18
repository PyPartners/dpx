# Let's find Fibonacci numbers!
# Remember, the sequence starts: 0, 1, 1, 2, 3, 5, 8, ...
# F(n) = F(n-1) + F(n-2)
# With F(0) = 0 and F(1) = 1

# --- Method 1: Memoization (Top-Down) ---
# We'll use a "memo" (like a notepad) to store results we've already calculated.

# This is our little notepad (a dictionary) to store computed Fibonacci values.
# We initialize it outside the main recursive function, or it would get reset with each call.
# A better way for helper recursion is to pass it or use an inner function.
memo_pad = {}

def fibonacci_with_memoization(number):
    """
    Calculates Fibonacci(number) using memoization.
    It's like a recursive solution, but it remembers previous results.
    """
    global memo_pad # Using the global memo_pad for simplicity in this example

    # First, check if we've already solved for this number.
    if number in memo_pad:
        # print(f"Memo: Found F({number}) in memo_pad!") # Uncomment to see memoization in action
        return memo_pad[number]

    # Base cases: F(0) and F(1) are the starting points.
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        # If not a base case and not in our memo_pad, we calculate it.
        # This is the recursive part: F(n) = F(n-1) + F(n-2)
        result = fibonacci_with_memoization(number - 1) + fibonacci_with_memoization(number - 2)
        
        # IMPORTANT: Store this new result in our memo_pad before returning!
        # So next time we need F(number), we don't have to recalculate.
        memo_pad[number] = result
        return result

# A slightly cleaner way to handle the memo_pad for memoization,
# avoiding global variables and making it fresh for each top-level call if needed.
def fibonacci_memo_cleaner(n):
    """
    A wrapper for a memoized Fibonacci function that initializes its own cache.
    """
    cache = {} # This cache is local to each call of fibonacci_memo_cleaner

    def _calculate_fib(num):
        # Check if we've already figured this one out.
        if num in cache:
            return cache[num]

        # The simplest cases we know.
        if num == 0:
            return 0
        if num == 1:
            return 1

        # If not, we calculate it by asking for the previous two.
        # This is where the recursion happens.
        fib_value = _calculate_fib(num - 1) + _calculate_fib(num - 2)
        
        # And very importantly, we save it in our cache for next time!
        cache[num] = fib_value
        return fib_value

    return _calculate_fib(n)


# --- Method 2: Tabulation (Bottom-Up) ---
# We'll build a table (a list) of Fibonacci numbers from the start.

def fibonacci_with_tabulation(number):
    """
    Calculates Fibonacci(number) using tabulation.
    It builds the solution from the ground up.
    """
    # For F(0) and F(1), the answer is just the number itself.
    if number == 0:
        return 0
    if number == 1:
        return 1

    # We need a list to store our Fibonacci numbers as we calculate them.
    # It needs to be big enough to hold values up to F(number).
    # So, number + 1 spots (e.g., for F(5), we need indices 0, 1, 2, 3, 4, 5).
    fib_table = [0] * (number + 1)

    # We know the first two values:
    fib_table[0] = 0  # F(0)
    fib_table[1] = 1  # F(1)

    # Now, let's fill in the rest of the table, starting from F(2).
    # We go up to 'number' (inclusive).
    for i in range(2, number + 1):
        # Each Fibonacci number is the sum of the two before it.
        # F(i) = F(i-1) + F(i-2)
        fib_table[i] = fib_table[i-1] + fib_table[i-2]
        # print(f"Tab: Calculated F({i}) = {fib_table[i]}") # Uncomment to see tabulation steps

    # The answer we want, F(number), is now at the end of our table.
    return fib_table[number]


# --- Let's test them out! ---
if __name__ == "__main__":
    how_many_fibs = 10 # We want the first 10 (F(0) to F(9))

    print(f"Calculating the first {how_many_fibs} Fibonacci numbers:\n")

    print("Using Memoization (Top-Down with cleaner cache):")
    for i in range(how_many_fibs):
        # For the global memo_pad version, you'd clear it before this loop
        # if you wanted each call to 'fibonacci_with_memoization' series
        # to be independent of a previous series.
        # For fibonacci_memo_cleaner, the cache is fresh for each `fibonacci_memo_cleaner(i)` call's internal work.
        print(f"F({i}) = {fibonacci_memo_cleaner(i)}")
    
    print("\n-------------------------------------\n")

    # If using the global memo_pad version, let's reset it for a fair comparison
    # or to show it works from scratch again.
    memo_pad = {} 
    print("Using Memoization (Top-Down with global memo_pad):")
    for i in range(how_many_fibs):
        print(f"F({i}) = {fibonacci_with_memoization(i)}")

    print("\n-------------------------------------\n")

    print("Using Tabulation (Bottom-Up):")
    for i in range(how_many_fibs):
        print(f"F({i}) = {fibonacci_with_tabulation(i)}")

    print("\nBoth methods should give the same results!")

    # Example of a larger number to see the efficiency:
    # print(f"\nF(20) with memoization (cleaner): {fibonacci_memo_cleaner(20)}")
    # memo_pad = {} # Reset global for this specific call
    # print(f"F(20) with memoization (global): {fibonacci_with_memoization(20)}")
    # print(f"F(20) with tabulation: {fibonacci_with_tabulation(20)}")