def hex_to_decimal(hex_str):
    hexNumbers = {
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
    # Clear space before and after the string
    hex_str = hex_str.strip()
    # Uppercase the string to match dictionary keys
    upper_hex_str = hex_str.upper()
    # Clear spaces from the string
    clean_hex_str = upper_hex_str.replace(" ", "")

    # Decimal value initialization
    decimal_value = 0
    result = 0

    for char in clean_hex_str:
        if char not in hexNumbers:
            return None
        else:
            for key in hexNumbers:
                if char == key:
                    value = hexNumbers[key]
                    # Find position (1-based index)
                    position = clean_hex_str.index(char) + 1
                    # calculate decimal value
                    decimal_value = value * (16 ** (len(clean_hex_str) - position))
                    result += decimal_value
    return result


obj = hex_to_decimal("cab")
print(obj)
