# import sqlite3
#
# db_connect = sqlite3.connect("d13.sqlite3")
#
# db_cursor = db_connect.cursor()
#
#
# def create_table_users():
#     db_cursor.execute("""
#         CREATE TABLE IF NOT EXISTS users(
#         id INTEGER PRIMARY KEY,
#         first_name TEXT,
#         last_name REAL)
#     """)
#
#
# def create_table_products():
#     db_cursor.execute("""
#         CREATE TABLE IF NOT EXISTS product(
#         id INTEGER PRIMARY KEY,
#         title TEXT,
#         price REAL)
#     """)
#
#
# def create_table_orders():
#     db_cursor.execute("""
#         CREATE TABLE IF NOT EXISTS orders(
#         id INTEGER PRIMARY KEY,
#         product_id TEXT,
#         user_id REAL)
#     """)
#
#
# def insert_users(firstname, lastname):
#     db_cursor.execute("""
#     INSERT INTO users (first_name, last_name) VALUES(?, ?)""", (firstname, lastname))
#
#
# def alter_users():
#     # db_cursor.execute("""
#     # ALTER TABLE users ADD COLUMN age INTEGER DEFAULT 10
#     #
#     # """)
#     # db_cursor.execute("""
#     # ALTER TABLE users RENAME dj to last_name
#     #
#     # """)
#     db_cursor.execute(""" DROP TABLE """)
#
# def insert_product(title, price):
#     db_cursor.execute("""
#     INSERT INTO product (title, price) VALUES(?, ?)""", (title, price))
#
#
# def insert_orders(product_id, user_id):
#     db_cursor.execute("""
#     INSERT INTO orders (product_id, user_id) VALUES(?, ?)""", (product_id, user_id))
#
#
# def read_users():
#     db_cursor.execute("""
#     SELECT * FROM users
#
#     """)
#     return db_cursor
#
#
# db_connect.commit()
# alter_users()
# print(read_users().fetchall())
#
# db_connect.close()


import sqlite3

db_connect = sqlite3.connect("d13.sqlite3")

db_cursor = db_connect.cursor()


def create_table_users():
    db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT)
    """)


def create_table_products():
    db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS product(
        id INTEGER PRIMARY KEY,
        title TEXT,
        price REAL,
        photo TEXT)
    """)


def create_table_orders():
    db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY,
        product_id INTEGER,
        user_id INTEGER)
    """)


def insert_users(firstname, lastname):
    db_cursor.execute("""INSERT INTO Meliodas (first_name, last_name) 
                         VALUES(?, ?)""", (firstname, lastname))


def altar_users():
    db_cursor.execute("""DELETE FROM Meliodas WHERE user_id=2""")


def insert_products(title, price, photo):
    db_cursor.execute("""INSERT INTO product (title, price, photo) 
                         VALUES(?, ?, ?)""", (title, price, photo))


def insert_orders(product_id, user_id):
    db_cursor.execute("""INSERT INTO orders (product_id, user_id) 
                         VALUES(?, ?)""", (product_id, user_id))


def get_all_product():
    products = db_cursor.execute("""SELECT * FROM product""").fetchall()
    db_connect.close()
    return products


def read_users():
    db_cursor.execute("""SELECT * FROM users""")
    return db_cursor
