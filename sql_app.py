import sqlite3


def find_movie():
    title = input ("What Title: ")
    connection = sqlite3.connect("movies.db")
    cursor = connection.cursor()
    cursor.execute("""
    select * from movies
    where title = ?
    """,(title,))
    result = cursor.fetchall() 
    if not result:
        print("Movie not found.")
        return None
    connection.close()
    return result

def add_movie():
    title = input("Title: ")
    year = input("Year: ")
    director = input("Director: ")
    genre = input("Genre: ")
    franchise = input ("Franchise: ")

    connection = sqlite3.connect("movies.db")
    cursor = connection.cursor()
    cursor.execute("""
    insert into movies (title,year,director,genre,franchise)
    values (?,?,?,?,?)""", (title,year,director,genre,franchise))
    connection.commit()
    connection.close()

def add_rating():
    result = find_movie()
    if result is None:
        return
    rating = input ("Rating: ")
    status = input ("Watched: ")
    date_watched = input ("Watching Date: ")
    notes = input("Notes: ")
    connection = sqlite3.connect("movies.db")
    cursor = connection.cursor()
    cursor.execute("""
    insert into movies_rating (movie_id,rating,status,date_watched,notes)
    values(?,?,?,?,?)
    """,(result[0][0],rating,status,date_watched,notes))
    connection.commit()
    connection.close()

def view_movies():
    connection = sqlite3.connect("movies.db")
    cursor = connection.cursor()
    cursor.execute("""
    select * from movies
    left join movies_rating on movies.id = movies_rating.movie_id
    """)
    result = cursor.fetchall()
    for row in result:
        print(f"\n{row[1]} ({row[2]}) - {row[3]} | {row[4]}")
        if row[5] != None:
            if row[8]:
                print(f"Rating: {row[8]}/10 | Watched: {row[9]}")
                print(f"Date: {row[10]}")
                print(f"Notes: {row[11]}")
            else:
                print("Not yet rated")
    print("-" * 40)

    connection.commit()
    connection.close()

def update_movie():
    result = find_movie()
    if result is None:
        return
    column = input ("What do you want to update(Title,Year,Directo,Genre): ")
    updated = input ("What do you want to update it to? ")
    connection = sqlite3.connect("movies.db")
    cursor = connection.cursor()
    cursor.execute(f"""
    update movies
    set {column} = ?
    where title = ?
    """,(updated,result[0][1]))
    print (result)
    print(f"Current: {result}")
    print(f"Will change {column} to: {updated}")
    choice = input("Commit? (y/n)")
    if choice == ("y"):
        connection.commit()
        connection.close()
    elif choice == ("n"):
        connection.close()
    else:
        print ("Wrong input")
        connection.close()

def delete_movie():
    result = find_movie()
    if result is None:
        return
    connection = sqlite3.connect("movies.db")
    cursor = connection.cursor()
    cursor.execute("""
    delete from movies 
    where title = ? 
    """,(result[0][1],))
    print (result)
    choice = input ("You want to delete that?(y/n) ")
    if choice == ("y"):
        connection.commit()
        connection.close()
    elif choice == ("n"):
        connection.close()
    else:
        print ("Wrong input")
        connection.close()

while True:
    print ("\n1. Add movie ")
    print ("2. View all movies ")
    print ("3. Update movie ")
    print ("4. Delete movie ")
    print ("5. Rate movie")
    print ("6. Quit ")

    choice = input("\nWhat do you want to do? ")
    if choice == "1":
        add_movie()
    elif choice == "2":
        view_movies()
    elif choice == "3":
        update_movie()
    elif choice == "4":
        delete_movie()
    elif choice == "5":
        add_rating()
    elif choice == "6":
        break
    else:
        print("Wrong input")

#results = cursor.fetchall()
#print(results)
