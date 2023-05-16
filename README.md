# Prüfziffernvalidierung für medizinische Identifikationsnummern

Dieses Repository enthält Python-Module zur Berechnung und Validierung von Prüfziffern für verschiedene medizinische Identifikationsnummern, einschließlich der Institutionskennzeichen (IK), Krankenversichertennummer (KVNR), lebenslangen Arztnummer (LANR) und Pharmazentralnummer (PZN).

## Installation

Stellen Sie sicher, dass Sie Python 3.6 oder höher auf Ihrem System installiert haben. Sie können die Skripte direkt in Ihrer Python-Umgebung ausführen.

## Nutzung

Jedes Modul (ik_check.py, kvnr_check.py, lanr_check.py und pzn_check.py) enthält zwei Hauptfunktionen:

1. `calculate_checksum()`: Berechnet die Prüfziffer basierend auf den Eingabedaten.
2. `validate_<ik/kvnr/lanr/pzn>()`: Überprüft, ob eine gegebene Nummer gültig ist, basierend auf ihrer Prüfziffer.

Sie können diese Funktionen in Ihren eigenen Skripten importieren und verwenden.

## Tests

Für jedes Modul gibt es auch ein entsprechendes Testskript (test_ik_check.py, test_kvnr_check.py, test_lanr_check.py und test_pzn_check.py), das die Funktionalität der Hauptfunktionen überprüft. Sie können diese Tests ausführen, indem Sie das Testskript in Ihrer Python-Umgebung ausführen:

```bash
python test_ik_check.py
```
Ersetzen Sie test_ik_check.py durch das gewünschte Testskript.

## Beitrag
Pull-Anfragen sind willkommen. Für größere Änderungen öffnen Sie bitte zuerst ein Issue, um zu besprechen, was Sie ändern möchten.

## Lizenz
MIT
