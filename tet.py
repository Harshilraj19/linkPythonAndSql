import mysql.connector

db = mysql.connector.connect(
    user = "root",
    host = "localhost",
    passwd = "",
    database = "sky_store"
)
# my_cursor = db.cursor() # pointing to database......used with every command
# my_cursor.execute("create database skyhs")# creates database

my_cursor = db.cursor()

# my_cursor.execute("show databases")# mycursor used in every command
#
# for d in my_cursor:
#     print(d)

# query = """
# create table skydet
# (
# name VARCHAR(255),
# roll INT(10),
# class int(10)
# )
# """


# my_cursor.execute("show tables")
#
# for t in my_cursor:
#     print(t)
#
# my_cursor.execute("ALTER TABLE skydet ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# sql = """
# insert into skydet (name, roll, class) values ("tommy",2234,20)

# a = "insert into skydet (name, roll, class) values (%s, %s, %s)"
# b = [
# ("harry",22,22),
# ("lisa",33,33),
# ("andy",444,44)
# ]
# #
# """
#
# my_cursor.executemany(a,b)
# db.commit()
# print(my_cursor.rowcount, "record inserted.")

# my_cursor.execute('select * from skydet')
# result = my_cursor.fetchall()
# db.close()  # close connection
# #
def readData(sql): # function to read a table
    my_cursor = db.cursor()
    result= my_cursor.execute(sql)
    result=my_cursor.fetchall()
    db.close()
    return result


res = readData("select * from skydet where id <= 3")

for row in res:
    print(row)

