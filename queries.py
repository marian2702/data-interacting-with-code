import sqlite3

conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()
db.execute("SELECT * FROM directors")
rows = db.fetchall()
print(rows)
# => list (rows) of tuples (columns)

def directors_count(db):
    query = "SELECT COUNT(*) AS total_directors FROM directors"

    result = db.execute(query)
    result = db.fetchone()
    return result[0]

def directors_list(db):
    query = "SELECT * FROM directors ORDER BY name ASC"

    result = db.execute(query)
    director_names = [row[0] for row in result.fetchall()]
    return director_names


def love_movies(db):
    query = """
        SELECT title
        FROM movies
        WHERE UPPER(title) LIKE '% LOVE %'
        OR UPPER(title) LIKE 'LOVE %'
        OR UPPER(title) LIKE '% LOVE'
        OR UPPER(title) LIKE 'LOVE'
        OR UPPER(title) LIKE '% LOVE''%'
        OR UPPER(title) LIKE '% LOVE.'
        OR UPPER(title) LIKE 'LOVE,%'
        ORDER BY title
    """

    result = db.execute(query)
    movie_titles = [row[0] for row in result.fetchall()]

    return movie_titles


def directors_named_like_count(db, name):
    query = """SELECT COUNT(*) FROM directors WHERE LOWER(name) LIKE ?"""

    db.execute(query, (f"%{name}%",))
    count = db.fetchone()
    return count[0]
    # return the number of directors which contain a given word in their name



def movies_longer_than(db, min_length):
    query = """
        SELECT title
        FROM movies
        WHERE minutes > ?
        ORDER BY title
    """
    db.execute(query, (min_length,))
    movies = db.fetchall()
    return [movie[0] for movie in movies]
