import sqlite3
connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

cursor.execute("""
    create table if not exists movies (
        id integer primary key autoincrement,                        
        title text not null,
        year integer,
        director text,
        genre text,
        franchise text
    )                                                
""")

cursor.execute("""
    create table if not exists movies_rating (
        id integer primary key autoincrement,                           
        movie_id integer,
        rating integer check(rating>=0 and rating <=10),
        status text default "want to watch",
        date_watched text,
        notes text

    )                                                
""")

connection.commit()
connection.close()