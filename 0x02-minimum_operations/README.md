# 0x02. Minimum Operations

For this project, you will need to understand several key algorithmic and mathematical concepts to devise a solution that efficiently calculates the minimum number of operations to achieve a given number of characters using only “Copy All” and “Paste” operations. 

# TASK

0. Minimum Operations
mandatory
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.
* Prototype: def minOperations(n)
* (Returns an integer
* If n is impossible to achieve, return 0


## Explanation:
   Initialization: We initialize operations to 0 and start with the smallest divisor, 2.
Loop:
We keep dividing n by the smallest divisor until it’s no longer divisible, adding the divisor to operations each time.
Then we move to the next divisor.
Return: Once n is reduced to 1, the loop ends, and we return the total number of operations.
## Example:
For n = 9, the function would work as follows:

Start with H (1 character).
9 is divisible by 3. Perform Copy All (1 operation) and Paste 2 times (2 operations) -> Now, we have HHH.
3 is divisible by 3. Perform Copy All (1 operation) and Paste 2 times (2 operations) -> Now, we have HHHHHHHHH.
Total operations = 6
