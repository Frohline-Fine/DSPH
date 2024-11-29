"""
Path library
"""
# imports
from pathlib import Path

src_file = Path(__file__).parent.parent / 'data_extractor' / 'source' / 'datei.pdf'
csv_file = Path(__file__).parent.parent / 'data_extractor' / 'data' / 'test.csv'
