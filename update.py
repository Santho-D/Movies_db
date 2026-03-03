import sqlite3
connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

cursor.execute("""
update movies
set director = "The Wachowskis"
where title = "The Matrix"
""")
results = cursor.fetchall()
print(results)
connection.commit()
connection.close()