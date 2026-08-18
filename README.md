LeetCode 3471 - Find the Largest Almost Missing Integer

Problem

Given an integer array "nums" and an integer "k", find the largest integer that appears in exactly one subarray of length "k".

If no such integer exists, return "-1".

Approach

There are three cases:

1. "k == 1"

Every element forms its own subarray.

So, we find the largest element whose frequency in the entire array is exactly "1".

2. "k == len(nums)"

There is only one subarray, which is the complete array.

Therefore, the answer is the maximum element in the array.

3. "1 < k < len(nums)"

Only the first and last elements can appear in exactly one subarray of length "k".

We check whether the first and last elements occur only once in the entire array and choose the larger valid value.

Example

Input

"nums = [3, 9, 2, 1, 7]"
"k = 3"

Subarrays of length "3" are:

- "[3, 9, 2]"
- "[9, 2, 1]"
- "[2, 1, 7]"

Here:

- "3" appears in exactly one subarray.
- "7" appears in exactly one subarray.

The largest almost missing integer is:

"7"

Output

"7"

Complexity

- Time Complexity: "O(n)"
- Space Complexity: "O(n)"

LeetCode

"Find the Largest Almost Missing Integer" (https://leetcode.com/problems/find-the-largest-almost-missing-integer/)