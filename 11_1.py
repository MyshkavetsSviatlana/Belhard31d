import sqlite3


conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS category(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    parent INTEGER, 
    descr);
''')
conn.commit()

cur.execute('''
    CREATE TABLE IF NOT EXISTS product(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    descr TEXT,
    category INTEGER NOT NULL);
''')
conn.commit()

# cur.execute('''
#     INSERT INTO product(id, name, descr, category) VALUES(6, 'PL-BY', 'Poland to Belarus', 1);
# ''')
# conn.commit()

cur.execute('''
    SELECT id, name 
    FROM category
    WHERE id=?;
''', (1, ))
print(cur.fetchall())

cur.execute('''
    SELECT id, name 
    FROM category
    WHERE name=?;
''', ('export', ))
print(cur.fetchall())

cur.execute('''
    SELECT id, name 
    FROM product
    WHERE id=?;
''', (5, ))
print(cur.fetchall())

cur.execute('''
    SELECT id, name 
    FROM product
    WHERE category = ?;
''', (2, ))
print(cur.fetchall())
