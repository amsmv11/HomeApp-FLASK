import sqlite3

# conn = sqlite3.connect("database.db")


import hashlib


conn = sqlite3.connect("database.db")

c = conn.cursor()

# c.execute("""CREATE TABLE cars(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             street TEXT NOT NULL
#             )""")



# conn.commit()


# c.execute("""CREATE TABLE shopping(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL
#             )""")



# conn.commit()


# c.execute("INSERT INTO cars (name, street) VALUES (?, ?)", ("Mercedes", "BES"))
# c.execute("INSERT INTO cars (name, street) VALUES (?, ?)", ("Peugeot", "BES"))
# c.execute("INSERT INTO cars (name, street) VALUES (?, ?)", ("Renault", "BES"))
# c.execute("INSERT INTO shopping (name) VALUES (?)", ("Pao",))
# c.execute("INSERT INTO shopping (name) VALUES (?)", ("Agua",))

# conn.commit()


# c.execute("SELECT * FROM cars")

# conn.commit()


# list = c.fetchall()

# print(list)



name = "Brinquedo cao roer"
c.execute("Delete FROM shopping WHERE name = '{}'".format(name))

conn.commit()






c.execute("SELECT * FROM cars")

conn.commit()


list = c.fetchall()

print(list)










c.execute("SELECT * FROM shopping")

conn.commit()


list = c.fetchall()

print(list)




conn.close()
