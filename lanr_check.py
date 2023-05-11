import re

def calculate_checksum(lanr: str) -> int:
    weights = [4, 9, 4, 9, 4, 9]
    partial_sums = []
    for i, digit in enumerate(lanr[0:6]):
        product = int(digit) * weights[i]
        partial_sum = sum(map(int, str(product)))
        partial_sums.append(partial_sum)

    total_sum = sum(partial_sums)
    remainder = total_sum % 10
    checksum =  10 -  remainder
    return checksum

def validate_lanr(lanr: str) -> bool:
    if not re.match(r"^([0-9]{6})([0-9]{1})([0-9]{2})$", lanr):
        print("invalid FORMAT")
        return False

    calculated_checksum = calculate_checksum(lanr[:6])
    checksum = int(lanr[6])

    return calculated_checksum == checksum