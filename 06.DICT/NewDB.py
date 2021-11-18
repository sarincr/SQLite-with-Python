import sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE LANG (name, DOB)")

cur.execute("insert into LANG values (?, ?)", ("C", 1972))
 
LANG_list = [
    ("Fortran", 1957),
    ("Python", 1991),
    ("Go", 2009),
]
cur.executemany("insert into LANG values (?, ?)", LANG_list)

print(cur.fetchall())

con.close()
