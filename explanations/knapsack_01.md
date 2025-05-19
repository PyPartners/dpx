# Solving the 0/1 Knapsack Problem with Dynamic Programming

The 0/1 Knapsack problem is a classic optimization problem. Imagine you have a knapsack (a bag) with a specific weight capacity. You're also given a set of items, each with its own weight and value. Your goal is to choose which items to put into the knapsack so that the total value of the items is maximized, without exceeding the knapsack's weight capacity.

The "0/1" part means for each item, you have two choices:
*   **0:** You leave the item (don't put it in the knapsack).
*   **1:** You take the entire item (put it in the knapsack). You can't take a fraction of an item.

We'll use dynamic programming, specifically the **tabulation (bottom-up)** method, to solve this.

## The Dynamic Programming Approach (Tabulation)

The core idea is to build a table (often called `dp_table`) that helps us keep track of the maximum value we can achieve for various subproblems.

**Understanding the DP Table:**

Let `dp_table[i][w]` represent the maximum value we can obtain by considering:
*   Only the **first `i` items** (from item 0 up to item `i-1` in our list of items).
*   With a knapsack that has a **maximum capacity of `w`**.

**Table Dimensions:**
*   **Rows:** The number of rows will be `num_items + 1`. Row 0 represents the case with "no items considered yet". Row `i` corresponds to decisions made considering up to the `(i-1)`-th item.
*   **Columns:** The number of columns will be `knapsack_capacity + 1`. Column 0 represents a knapsack with "0 capacity". Column `w` represents a knapsack with capacity `w`.

**Initialization:**
We typically initialize the entire table with zeros.
*   `dp_table[0][w] = 0` for all `w`: If you have no items to choose from, the maximum value is 0, regardless of knapsack capacity.
*   `dp_table[i][0] = 0` for all `i`: If your knapsack has 0 capacity, you can't put any items in it, so the maximum value is 0.

**Filling the Table (The Core Logic):**

We fill the table row by row, and for each row, column by column.
For each cell `dp_table[i][current_weight_capacity]`, we are essentially deciding what to do with the *i-th item* (which is `item_weights[i-1]` and `item_values[i-1]` in 0-indexed arrays).

Let `current_item_weight = item_weights[i-1]` and `current_item_value = item_values[i-1]`.

We have two choices for the current item:

1.  **Choice 1: Exclude the current item (`item_weights[i-1]`).**
    If we don't include the current item, the maximum value we can get is the same as the maximum value we could get with the *previous `i-1` items* and the *same `current_weight_capacity`*.
    This value is already computed and stored in `dp_table[i-1][current_weight_capacity]`.
    So, `value_without_current_item = dp_table[i-1][current_weight_capacity]`.

2.  **Choice 2: Include the current item (`item_weights[i-1]`).**
    We can only do this if the `current_item_weight` is less than or equal to the `current_weight_capacity`.
    *   If `current_item_weight <= current_weight_capacity`:
        The value we get from this item is `current_item_value`.
        The remaining capacity in the knapsack will be `current_weight_capacity - current_item_weight`.
        We then need to add the maximum value we could get from the *previous `i-1` items* with that *remaining capacity*. This is `dp_table[i-1][current_weight_capacity - current_item_weight]`.
        So, `value_with_current_item = current_item_value + dp_table[i-1][current_weight_capacity - current_item_weight]`.
    *   If `current_item_weight > current_weight_capacity` (item doesn't fit):
        We cannot include the current item, so this choice effectively leads to the same outcome as Choice 1, or we can think of `value_with_current_item` as 0 (or negative infinity) for this path.

**The Decision:**
The value we store in `dp_table[i][current_weight_capacity]` is the maximum of these two choices:
`dp_table[i][current_weight_capacity] = max(value_without_current_item, value_with_current_item)`
(If the item doesn't fit, `value_with_current_item` wouldn't be considered or would be less than `value_without_current_item`).

**The Final Answer:**

After filling the entire table, the cell `dp_table[num_items][knapsack_capacity]` will contain the maximum total value that can be achieved by considering all available items with the full knapsack capacity. This is our solution!

This bottom-up approach ensures that when we need to make a decision for `dp_table[i][w]`, the values from `dp_table[i-1][...]` (which represent solutions to smaller subproblems) have already been optimally computed.

The Python code demonstrating this method can be found in a file like [`knapsack_01.py`](https://github.com/PyPartners/dpx/blob/main/problems/knapsack_01.py).
