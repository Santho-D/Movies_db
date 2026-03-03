import sqlite3
connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

cursor.execute("""
delete from movies
where id not in (
    select min (id)              
    from movies
    group by title
)
""")
results = cursor.fetchall()
print(results)
connection.commit()
connection.close()