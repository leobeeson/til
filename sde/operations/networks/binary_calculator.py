

decimal_to_hexadecimal_table = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
}


hexadecimal_to_decimal_table = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
}


def convert_decimal_to_binary(decimal_number: int) -> None:
    if decimal_number > 1:
        convert_decimal_to_binary(decimal_number // 2)
    print(decimal_number % 2, end = "")


def convert_binary_to_decimal(binary_number: int) -> None:
    decimal_number = 0
    for digit in str(binary_number):
        decimal_number = decimal_number*2 + int(digit)
    print(decimal_number)


def convert_decimal_to_hexadecimal(decimal_number: int) -> str:
    if (decimal_number <= 0):
        return ""
    remainder = decimal_number % 16
    return convert_decimal_to_hexadecimal(decimal_number//16) + decimal_to_hexadecimal_table[remainder]


def convert_hexadecimal_to_decimal(hexadecimal_number: str) -> int:
    decimal_number = 0
    hexadecimal_number_length = len(hexadecimal_number) - 1
    for digit in hexadecimal_number:
        decimal_number += hexadecimal_to_decimal_table[digit]*16**hexadecimal_number_length
        hexadecimal_number_length -= 1
    return decimal_number


if __name__ == "__main__":
    convert_decimal_to_binary(192)
    print("\n")
    convert_binary_to_decimal(11000000)
    print(convert_decimal_to_hexadecimal(229))
    print(convert_hexadecimal_to_decimal("E9"))
