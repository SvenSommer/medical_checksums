def calculate_checksum(ik_number: str) -> int:
    weights = [2, 1, 2, 1, 2, 1]
    partial_sums = []

    for i, digit in enumerate(ik_number[2:8]):
        product = int(digit) * weights[i]
        partial_sum = sum(map(int, str(product)))
        partial_sums.append(partial_sum)

    total_sum = sum(partial_sums)

    checksum = total_sum % 10
    return checksum

def validate_ik(ik_number: str) -> bool:
    if len(ik_number) != 9:
        return False

    calculated_checksum = calculate_checksum(ik_number)
    return calculated_checksum == int(ik_number[8])