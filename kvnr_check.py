# kvnr_check.py
import re

def calculate_checksum(kvnr: str) -> int:
    card_no = f"{ord(kvnr[0]) - ord('@'):02d}{kvnr[1:9]}"
    total_sum = 0
    for i in range(10):
        d = int(card_no[i]) - int('0')
        if i % 2 == 1:
            d *= 2
        if d > 9:
            d -= 9
        total_sum += d
    return total_sum % 10

def validate_kvnr(kvnr: str) -> bool:
    if not re.match(r"^([A-Z]{1})([0-9]{9})$", kvnr):
        return False
    calculated_checksum = calculate_checksum(kvnr[:9])
    return calculated_checksum == int(kvnr[9])