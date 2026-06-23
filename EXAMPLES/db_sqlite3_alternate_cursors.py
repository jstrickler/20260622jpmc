"""
Generic functions that can be used with any DB API compliant
package.

To use, pass in a cursor after execute()-ing a
SQL query. Then iterate over the generator that is
returned
"""
import sqlite3
from db_alternate_cursors import *

sql_select = """
SELECT firstname, lastname, party
FROM presidents
WHERE termnum > 39
"""

conn = sqlite3.connect("../DATA/presidents.db")

cursor = conn.cursor()

cursor.execute(sql_select)

for row in dict_cursor(cursor):
    print(row['firstname'], row['lastname'], row['party'])

print('-' * 60)


cursor.execute(sql_select)

for row in namedtuple_cursor(cursor):
    print(row.firstname, row.lastname, row.party)

print('-' * 60)


cursor.execute(sql_select)

for row in dataclass_cursor(cursor):
    print(row.firstname, row.lastname, row.party)
