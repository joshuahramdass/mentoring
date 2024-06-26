
### Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Quick version. Find the sum of all multiples of 3 below 4
We count each number beginning from 1 to N-1 (For N=4)
	For number 1, 1mod3. That's 1, and it's not 0.  So we continue
	For number 2, 2mod3. That's 2, and it's not 0. So we continue
	For number 3, 3mod3. That's 0. That's multiple of 3, we add that as a result
	
For N=4
We count each number beginning from 1 to N-1. Assign that number to i
	For number i, i mod 3. That's 1, and it's not 0.  So we continue
	Increase i by 1
	For number i, i mod 3. That's 2, and it's not 0. So we continue
	Increase i by 1
	For number i, i mod 3. That's 0. That's multiple of 3, we add that as a result
	i equals to N-1 now. So we stop counting
	
	
We count each number beginning from 1 to N-1. Assign that number to i
	For number i, i mod 3 equals 1 which doesn't equal 0. We don't add i
	Increase i by 1
	For number i, i mod 3. equals 2 which doesn't equal 0. We don't add i
	Increase i by 1
	For number i, i mod 3. equals 0 which equals 0. We add i
	i equals to N-1 now. So we stop counting
	
	
We count each number beginning from 1 to N-1. Assign that number to i. After each line increase i by 1:
	For number i, i mod 3=1, which != 0. We don't add i
	For number i, i mod 3=2, which != 0. We don't add i
	For number i, i mod 3=0, which = 0. We add i
	i equals to N-1 now. So we stop counting

We count each number beginning from 1 to N-1. Assign that number to i. After each line increase i by 1:
	For number i, do i mod 3 and i mod 5. If either results equal to 0, add i to results table. If it doesn't, do nothing.


****The modular rule is a python3 rule (3%5)**








