
# Data Science Prüfungshelfer

## Beschreibung
Dieses Programm bietet eine grafische Oberfläche, mit der man sich auf die *Certified Data Science Fundamentals* Zertifizierung der *CODE S Academy* vorbereiten kann. 
Kann nur mit dem entsprechenden PDF von *CODE S Academy* verwendet werden.

Übungsmodus: Zufällige Fragen zum Üben

Trainingsmode: Wie Übungsmodus, aber mit englischer Übersetzung (sehr langsam wegen des eingebauten Google Translators)

Prüfungssimulation: Simuliert die anstehende Prüfung mit 80 zufälligen Fragen, einem Zeitlimit und anschließender Auswertung (nicht fertig!)


## Installation
1. Klonen Sie das Repository:
   ```bash
   git clone https://github.com/Frohline-Fine/DSPH.git
   ```
2. Erstellen Sie eine virtuelle Umgebung im Projektordner:
   ```bash
   python -m venv .venv
   ```
3. Aktivieren Sie die virtuelle Umgebung:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
4. Installieren Sie die Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
   ```

## Benötigte Pakete
Die wichtigsten Pakete für dieses Projekt sind:
- googletrans => 3.1.0a0
- pandas => 2.2.3
- pdfminer => 20191125
- pdfminer.six => 20240706
- PyQt6 => 6.7.1
- PyQt6-Qt6 => 6.7.3
- PyQt6_sip => 13.8.0


## Verwendung
Ersetzen Sie die leere datei.pdf in /db/data/ durch Ihre lizenzierte Datei, die Sie von *CODE S Academy* erhalten haben und passen Sie den Dateipfad in /helper/paths an.

Starten Sie das Programm über main.py

Beim ersten Start wird automatisch eine SQLite Datenbank in /db/data/ angelegt

## Lizenz
GNU General Public License 3