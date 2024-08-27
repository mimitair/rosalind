"""
This script takes asks for 2 positive integers n and k.
n: amount of months in the future. (<= 40)
k: amount of rabbit pairs that each rabbit pair of reproductive age produces (<= 5)

result: the amount of rabbit pairs after n months.

To run this script:
`python3 main.py`

This might not be the most efficient way of solving this problem. 
When working with large numbers, the program will have to store all the items of the list.
This would require unnecessary amounts of memory.
"""

def calculate_rabbit_pairs(n: int, k: int) -> int:
	# Initiate the sequence:
	result = [1, 1]  # We start with one rabbit pair in the first month. In the second month, they will reproduce k rabbit pairs.
	i = 0
	while i < n - 2:  # Since we are already initiating the list after two months, we subtract n by 2.
		result.append(result[-1] + k * result[-2]) # F_n = F_n-1 + k*F_n-2
		i += 1
	# Return the last element in the list/sequence:
	return result[-1]
		

def main():
	n = int(input("n: "))
	k = int(input("k: "))
	print(calculate_rabbit_pairs(n, k))

if __name__ == "__main__":
	main()
