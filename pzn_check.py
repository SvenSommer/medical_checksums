import re

def calculate_checksum(pzn: str) -> int:
    weights = list(range(1, 8))
    products = [int(pzn[i]) * weights[i] for i in range(7)]
    total_sum = sum(products)
    checksum = total_sum % 11
    return checksum

def validate_pzn(pzn: str) -> bool:
    if not re.match(r"^([0-9]{7})([0-9]{1})$", pzn):
        return False

    calculated_checksum = calculate_checksum(pzn[:7])
    return False if calculated_checksum == 10 else calculated_checksum == int(pzn[7])