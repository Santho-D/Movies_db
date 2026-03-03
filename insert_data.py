import sqlite3
connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

cursor.execute("""
    insert into movies (title,year,director,genre)
    values 
        ("The Matrix", 1999, "Wachowski", "Sci-Fi"),
        ("Interstellar",2014,"Nolan","Sci-Fi"),
        ("Inception", 2010, "Nolan", "Sci-Fi")
""")

connection.commit()
connection.close()