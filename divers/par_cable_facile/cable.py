cable = [1,1,1,-1,1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,-1,-1,-1,-1,-1,1,-1,-1,1,1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,-1,-1,1,-1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,-1,-1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,-1,1,1,1,1,-1,1,1,1,-1,1,1,-1,1,-1,-1,-1,1,1,1,1,-1,1,1,1,1,1,1,-1,-1,1,-1,1,-1,1,1,-1,-1,-1,1,1,1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,1,-1,1,1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,-1,-1,1,-1,1,-1,1,1,-1,1,1,1,-1,1,1,1,1,-1,1,1,1,1,1,1,-1,1,-1,-1,-1,1,1,1,1,-1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,-1,1,-1,1,-1,1,1,-1]

binary_str = ""

for i in range(len(cable) - 1):
    if cable[i] == cable[i+1]:
        binary_str += "0"
    else:
        binary_str += "1"

# https://www.geeksforgeeks.org/python-program-to-convert-binary-to-ascii/

# Python program to illustrate the
# conversion of Binary to ASCII

# Initializing a binary string in the form of
# 0 and 1, with base of 2
binary_int = int(binary_str, 2);

# Getting the byte number
byte_number = binary_int.bit_length() + 7 // 8

# Getting an array of bytes
binary_array = binary_int.to_bytes(byte_number, "big")

# Converting the array into ASCII text
ascii_text = binary_array.decode()

# Getting the ASCII value
print(ascii_text)
