# Movie Database
- Python scripts to create and manage a movie database. Creates a table for movies and a second table for ratings.

## Database Structure

### Movies
| Column | Type | Description |
|--------|------|-------------|
| ID | INTEGER | Auto-generated unique identifier |
| Title | TEXT | Movie title (required) |
| Year | INTEGER | Release year |
| Director | TEXT | Director name |
| Genre | TEXT | Movie genre |
| Franchise | TEXT | Franchise/series name (optional) |

### Ratings
| Column | Type | Description |
|--------|------|-------------|
| ID | INTEGER | Auto-generated unique identifier |
| Movie_ID | INTEGER | Links to movie in Movies table |
| Rating | INTEGER | Score from 0-10 |
| Watched | TEXT | Watch status |
| Watched_date | TEXT | Date watched (YYYY-MM-DD) |
| Notes | TEXT | Personal notes |

## Tools used
- Python 3.6
- SQLite

## Features
 - You can add movies, view entries, update existing ones, delete and rate movies from within this script.

## Quick start:

```bash
# Clone the repository
git clone https://github.com/Santho-D/Movies_db.git
cd Movies_db

# Run the script
python database_movies.py
python sql_app.py
```

## Requirements

- Python3.6 or higher
- No external dependencies

## How to

### Step 1
- Create the database by running database_movies.py.

### Step 2
- Manage it by running sql_app.py.
 
### Step 3 
- Add your own movies and ratings and enjoy.

## Author

Santho-D
Fachinformatiker Anwendungsentwicklung in Ausbildung
