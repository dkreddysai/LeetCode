def dectobinary(decimal_num):
    if decimal_num == 0:
        return 0

    binary_num = ""
    while decimal_num > 0:
        remainder = decimal_num % 2  # find the remainder
        binary_num = str(remainder) + binary_num      # add remainder to the left of the binary_num string
        decimal_num = decimal_num // 2         # update the decimal_num each time after finding the remainder
    return binary_num


print(dectobinary(6))