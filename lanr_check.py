import re
import random

def calculate_checksum(lanr: str) -> int:
    weights = [4, 9, 4, 9, 4, 9]
    total_sum = 0
    for i, digit in enumerate(lanr[0:6]):
        product = int(digit) * weights[i]
        total_sum += product

    print("total_sum:",total_sum)
    remainder = total_sum % 10
    print("remainder:",remainder)
    checksum = 10 - remainder
    if checksum == 10:
        checksum = 0
    return checksum

def validate_lanr(lanr: str) -> bool:
    if not re.match(r"^([0-9]{9})$", lanr):
        print("Invalid FORMAT")
        return False


    calculated_checksum = calculate_checksum(lanr[:6])
    checksum = int(lanr[6])

    # if lanr[:7] == "4444444":
    #     print("Pseudoarztnummer im Rahmen des Reha-Entlassmanagements")
    #     return True

    # if lanr == "999999900":
    #     print("Ambulanzen in Krankenhäusern, Privatärzte ohne LANR, Ärzte in Weiterbildung etc.")
    #     return True

    # if lanr[:6] == "555555":
    #     print("Verordnungen im Rahmen der Versorgung nach § 116b Abs. 1 SGB V")
    #     return True

    # if lanr == "000000000":
    #     print("Ausnahme der Verordnungen im Rahmen der Versorgung nach § 116b Abs. 1 SGB V")
    #     return True

    # if lanr == "999999991":
    #     print("Zahnärzte in zahnärztlichen Hochschulambulanzen")
    #     return True

    return calculated_checksum == checksum



def generate_valid_lanr() -> str:
    # Generiere zufällige 6 Ziffern für die LANR
    lanr = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    # Berechne die Prüfsumme
    checksum = calculate_checksum(lanr)
    # Generiere die letzten zwei Ziffern zufällig
    last_two_digits = ''.join([str(random.randint(0, 9)) for _ in range(2)])
    # Kombiniere alle Teile um die gültige LANR zu erzeugen
    valid_lanr = lanr + str(checksum) + last_two_digits
    return valid_lanr

def generate_negative_lanr() -> str:
    # Generiere eine zufällige 9-stellige Nummer, die nicht der Checksummen-Logik folgt
    lanr = ''.join([str(random.randint(0, 9)) for _ in range(9)])
    # Überprüfe, ob die generierte Nummer tatsächlich ungültig ist. Falls nicht, generiere eine neue.
    while validate_lanr(lanr):
        lanr = ''.join([str(random.randint(0, 9)) for _ in range(9)])
    return lanr

def generate_positive_lanr() -> str:
    # Generiere eine gültige LANR
    lanr = generate_valid_lanr()
    # Überprüfe, ob die generierte Nummer tatsächlich gültig ist. Falls nicht, generiere eine neue.
    while not validate_lanr(lanr):
        lanr = generate_valid_lanr()
    return lanr

to_test = ["444444","999999","555555","000000","999999","333333","111111","222222","666666","777777"]
for id in to_test:
    print(f"ID: {id} calculated checksum: {calculate_checksum(id)}")