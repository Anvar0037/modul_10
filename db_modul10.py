import sqlite3

db_connect = sqlite3.connect("d13.sqlite3")

db_cursor = db_connect.cursor()

db_cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
first_name TEXT,
last_name REAL)
""")

db_cursor.execute("""
CREATE TABLE IF NOT EXISTS product(
id INTEGER PRIMARY KEY,
title TEXT,
price REAL)
""")


db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY,
    product_id TEXT,
    user_id REAL)
""")

db_cursor.execute("""
INSERT INTO users (first_name, last_name) VALUES ('Anvar', 'Nosirov')""")


db_cursor.execute("""
INSERT INTO product (title, price) VALUES ('Banan', 20.000)
""")


db_cursor.execute("""
INSERT INTO orders (product_id, user_id) VALUES (1, 1)""")

db_connect.commit()

db_connect.close()