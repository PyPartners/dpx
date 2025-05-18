def solve_knapsack_01(item_weights, item_values, knapsack_capacity):
    """
    Solves the 0/1 Knapsack problem using bottom-up dynamic programming (tabulation).

    Args:
        item_weights: A list of integers representing the weights of the items.
        item_values: A list of integers representing the values of the items.
        knapsack_capacity: An integer representing the maximum weight the knapsack can hold.

    Returns:
        The maximum total value of items that can be put into the knapsack.
    """

    # First, let's find out how many items we have.
    # It's good practice to make sure weights and values lists are the same length.
    num_items = len(item_values)
    if len(item_weights) != num_items:
        print("Error: Weights and values lists must have the same number of items.")
        return 0 # Or raise an error

    # --- Setting up our DP Table ---
    # We're going to build a table (a list of lists, like a spreadsheet).
    # Let's call it `dp_table`.
    # `dp_table[i][w]` will store the maximum value we can get by:
    #   - considering only the first `i` items (from item 0 up to item `i-1`)
    #   - with a knapsack that can hold a maximum weight of `w`.

    # The table needs `num_items + 1` rows.
    # Row 0 will represent the case with "no items considered yet".
    # Row `i` will correspond to considering items up to `item_weights[i-1]`.
    # So, row `num_items` will consider all available items.

    # The table needs `knapsack_capacity + 1` columns.
    # Column 0 will represent a knapsack with "0 capacity".
    # Column `w` will represent a knapsack with capacity `w`.
    # So, column `knapsack_capacity` is our target capacity.

    # Initialize the table with all zeros.
    # This means, initially, we assume we can get 0 value.
    dp_table = [[0 for _ in range(knapsack_capacity + 1)] for _ in range(num_items + 1)]

    # --- Filling the DP Table (The Core Logic) ---
    # We'll iterate through each item, and for each item, we'll consider all possible knapsack capacities.

    # `i` will go from 1 up to `num_items`.
    # This `i` represents "considering the i-th item" (which is at index `i-1` in our lists).
    for i in range(1, num_items + 1):
        # Get the weight and value of the *current* item we are considering.
        # Since our `i` is 1-based for the table (1st item, 2nd item, etc.),
        # the actual index in our 0-based `item_weights` and `item_values` lists is `i-1`.
        current_item_weight = item_weights[i-1]
        current_item_value = item_values[i-1]

        # `w` will go from 0 up to `knapsack_capacity`.
        # This `w` represents the current maximum capacity of the knapsack we are trying to fill.
        for current_weight_capacity in range(knapsack_capacity + 1):
            # Now, for each item `i` and each capacity `w`, we have two choices:

            # Choice 1: We DO NOT include the current item (`item_weights[i-1]`) in the knapsack.
            # If we don't include it, the maximum value is whatever we could get
            # with the *previous* items (`i-1`) and the *same* knapsack capacity (`w`).
            # This value is already stored in `dp_table[i-1][w]`.
            value_without_current_item = dp_table[i-1][current_weight_capacity]

            # Choice 2: We DO include the current item (`item_weights[i-1]`) in the knapsack.
            # But, we can only do this if the current item's weight is less than or equal to
            # the current knapsack capacity `w`.
            value_with_current_item = 0 # Initialize to 0, in case we can't take it
            if current_item_weight <= current_weight_capacity:
                # If we take this item, its value is `current_item_value`.
                # The remaining capacity in the knapsack will be `w - current_item_weight`.
                # We then need to find the best value we could get from the *previous* items (`i-1`)
                # with that *remaining* capacity. This is `dp_table[i-1][w - current_item_weight]`.
                value_with_current_item = current_item_value + dp_table[i-1][current_weight_capacity - current_item_weight]

            # So, `dp_table[i][w]` should be the maximum of these two choices.
            dp_table[i][current_weight_capacity] = max(value_without_current_item, value_with_current_item)

    # --- The Final Answer ---
    # After filling the whole table, the cell `dp_table[num_items][knapsack_capacity]`
    # will contain the maximum value we can get by considering all `num_items`
    # with the full `knapsack_capacity`. This is our answer!
    max_total_value = dp_table[num_items][knapsack_capacity]
    
    # If you want to see the whole table (for learning/debugging):
    # print("\nDP Table:")
    # for row_index in range(num_items + 1):
    #     print(f"Item {row_index (0=none)}: {dp_table[row_index]}")

    return max_total_value

# --- Let's demonstrate with an example! ---
if __name__ == "__main__":
    print("Solving the 0/1 Knapsack Problem!")

    # Sample items:
    # Item | Weight | Value
    #  A   |   2    |   6
    #  B   |   2    |  10
    #  C   |   3    |  12
    #  D   |   5    |  15  (let's add one more)
    
    # For a smaller, easier-to-trace example first:
    example_values = [60, 100, 120] # Values of the items
    example_weights = [10, 20, 30]   # Weights of the items
    example_capacity = 50           # Maximum weight the knapsack can hold

    print(f"\nItems available:")
    for i in range(len(example_values)):
        print(f"  - Item {chr(65+i)}: Weight = {example_weights[i]}, Value = {example_values[i]}")
    print(f"Knapsack Capacity: {example_capacity}")

    max_value_can_carry = solve_knapsack_01(example_weights, example_values, example_capacity)
    print(f"\nMaximum value that can be carried: {max_value_can_carry}")
    # Expected output for this example:
    # Items: (20, 100) + (30, 120) = Weight 50, Value 220.
    # Or (10,60) + (20,100) = Weight 30, Value 160.
    # If we take 30 (value 120), remaining capacity 20. Take 20 (value 100). Total 220.
    # If we take 20 (value 100), remaining capacity 30. Take 30 (value 120). Total 220.
    # If we take 10 (value 60), remaining capacity 40. Take 30 (value 120). Total 180.
    # So 220 is correct.

    print("\n--- Another Example ---")
    item_values_2 = [10, 40, 30, 50]
    item_weights_2 = [5, 4, 6, 3]
    knapsack_capacity_2 = 10

    print(f"Items available:")
    for i in range(len(item_values_2)):
        print(f"  - Item {chr(65+i)}: Weight = {item_weights_2[i]}, Value = {item_values_2[i]}")
    print(f"Knapsack Capacity: {knapsack_capacity_2}")
    
    max_value_2 = solve_knapsack_01(item_weights_2, item_values_2, knapsack_capacity_2)
    print(f"\nMaximum value that can be carried: {max_value_2}")
    # For this example (capacity 10):
    # Item D (weight 3, value 50) + Item B (weight 4, value 40) = Total Weight 7, Total Value 90
    # Item D (weight 3, value 50) + Item A (weight 5, value 10) = Total Weight 8, Total Value 60
    # Item C (weight 6, value 30) + Item B (weight 4, value 40) = Total Weight 10, Total Value 70
    # So 90 should be the answer.