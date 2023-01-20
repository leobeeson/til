

def convert_decimal_to_binary(decimal_number: int) -> None:
    if decimal_number > 1:
        convert_decimal_to_binary(decimal_number // 2)
    print(decimal_number % 2, end = "")


def convert_binary_to_decimal(binary_number: int) -> None:
    decimal_number = 0
    for digit in str(binary_number):
        decimal_number = decimal_number*2 + int(digit)
    print(decimal_number)


if __name__ == "__main__":
    convert_decimal_to_binary(192)
    print("\n")
    convert_binary_to_decimal(11000000)
