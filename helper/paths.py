"""
Path library
"""
# imports
from pathlib import Path

src_file = Path(__file__).parent.parent / 'init_db' / 'source' / 'datei.pdf'
csv_file = Path(__file__).parent.parent / 'init_db' / 'data' / 'test.csv'
