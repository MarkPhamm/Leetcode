## Day 1 (10/27/2024):
- **1480.** Running Sum of 1d Array
- **412.** Fizz Buzz
- **1342.** Number of Steps to Reduce a Number to Zero
- **9.** Palindrome Number
- **1.** Two Sum
  - 2 for loop (O n^2)
  - Hashmap
- **26.** Remove Duplicates from Sorted Array
  - Index to remove
  - Two Pointer

## Day 2 (10/28/2024)
- **1.** Two Sum
    - Two Pointer (requires a sorted list)
- **2239.** Find Closest Number to Zero
- **1768.** Merge Strings Alternately
  - Two Pointer
- **13.** Roman to Integer
  - Hash map
- **392.** Is Subsequence
  - Two Pointer
- **121.** Best Time to Buy and Sell Stock
- **228.** Summary Ranges

## Day 3 (10/29/2024)
- **27.** Remove Element 
- **771.** Jewels and Stones
- **217.** Contains Duplicate
- **383.** Ransom Note
- **20.** Valid Parentheses

## Day 4 (10/30/2024) - Review Day
- **228.** Summary Ranges
  - two-pointer:
    1. loop for i < n
    2. if i = n-1 (n is the last element): append "i" if i == j else append "i->j"
    3. else check nums[i] and nums[i+1]:
       - if num[i]+1 != nums[i]: log "i" if i == j else append "i->j", j=i+1
       - else: do nothing
       
- **27.** Remove Element
  - two-pointer:
    - while i<=j:
      1. check if num i is the value:
         - if yes: switch nums[i] and nums[j], reduce j by 1
         - if no: increase i by 1
      2. return i+1   
- **771.** Jewels and Stones
- **217.** Contains Duplicate
- **383.** Ransom Note
- **20.** Valid Parentheses


  
