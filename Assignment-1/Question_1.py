# 1. Using Slicing
def reverse_string_slicing(s):
    return s[::-1]

# Explanation: This method uses Python’s slicing feature. The [::-1] slice steps through the string backwards, effectively reversing it. It’s concise and runs efficiently because Python handles the slicing operation internally.

# 2. Using a Loop

def reverse_string_loop(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Explanation: This approach iterates over each character in the original string and adds each character to the front of a new string, effectively reversing the string manually.

# 3. Using the reversed() Function and join()

def reverse_string_reversed(s):
    return ''.join(reversed(s))

# Explanation: The reversed() function returns an iterator that accesses the given sequence in the reverse order. The join() method then concatenates these characters into a new string.

"""Which is Better and Why?

Slicing ([::-1]) is generally considered the best method:
Simplicity: It's the most concise—just one line and very easy to read.
Performance: Internally, it’s implemented in C and optimized for speed. In practical tests, it's usually the fastest for small to moderately sized strings.
Pythonic Style: It leverages Python’s expressive syntax.

Other Methods:
The loop method is the least efficient since each new string construction creates a new string object, leading to more memory allocation and lower performance, especially with long strings.
The reversed() and join() method is also good—it’s clean and fast, but not as concise as slicing."""