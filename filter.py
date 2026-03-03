import sqlite3
connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

cursor.execute("""
select * from movies
where director = "Nolan" and year > 2010
""")
results = cursor.fetchall()
print(results)
connection.commit()
connection.close()