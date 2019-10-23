import os
import sys

import sqlite3

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

conn = sqlite3.connect(r'db.sqlite3', check_same_thread=False)