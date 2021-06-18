# Algorithms-and-DataStructures1

1. MaxAverageSum.py :
Given an array with positive and negative numbers, find the maximum average subarray of given length.

Example: 

Input:  arr[] = {1, 12, -5, -6, 50, 3}, k = 4
Output: Maximum average subarray of length 4 begins
        at index 1.
Maximum average is (12 - 5 - 6 + 50)/4 = 51/4

Solution : Sliding Window Approach

2. MaxSum.py
Given an array of integers and a number k, find the maximum sum of a subarray of size k. 

Examples: 

Input  : arr[] = {100, 200, 300, 400}
         k = 2
Output : 700

Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}
         k = 4 
Output : 39
We get maximum sum by adding subarray {4, 2, 10, 23}
of size 4.

Input  : arr[] = {2, 3}
         k = 3
Output : Invalid
There is no subarray of size 3 as size of whole
array is 2. 

Solution : Sliding Window Approach
