# Generiere 100 negative und 100 positive LANRs
from lanr_check import generate_negative_lanr, generate_positive_lanr


negative_lanrs = [generate_negative_lanr() for _ in range(100)]
positive_lanrs = [generate_positive_lanr() for _ in range(100)]

with open('lanr_values.py', 'w') as file:
    file.write('negatives = [\n')
    for lanr in negative_lanrs:
        file.write(f'    "{lanr}",\n')  # Wrap lanr in quotes to make it a string
    file.write(']\n\n')
    file.write('positives = [\n')
    for lanr in positive_lanrs:
        file.write(f'    "{lanr}",\n')  # Wrap lanr in quotes to make it a string
    file.write(']\n')
