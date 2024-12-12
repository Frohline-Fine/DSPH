"""

Path library

"""

from pathlib import Path

from helper.constants import DB_NAME

src_file = Path(__file__).parent.parent / 'db' / 'data' / 'datei.pdf'
db_file = Path(__file__).parent.parent / 'db' / 'data' / DB_NAME
