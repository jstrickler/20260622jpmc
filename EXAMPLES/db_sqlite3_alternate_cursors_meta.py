"""
This package uses the functions from db_alternate_cursors, but uses some
 metaprogramming to call the functions generically.

 It uses  getattr() to retrieve the "get" function, which is then used to retrieve columns.
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

for iter_function in dict_cursor, namedtuple_cursor, dataclass_cursor:

    cursor.execute(sql_select)

    for row in iter_function(cursor):
        if isinstance(row, dict):
            get_function_name = '__getitem__'
        else:
            get_function_name = '__getattribute__'
        get_function = getattr(row, get_function_name)

        print(get_function('firstname'), get_function('lastname'), get_function('party'))

    print('-' * 60)

