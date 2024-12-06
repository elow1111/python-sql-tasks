import psycopg2

conn = psycopg2.connect('postgresql://postgres:@localhost:5432/test_db')


# BEGIN (write your solution here)
def add_movies(conn):
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO movies (title, release_year, duration) VALUES (%s, %s, %s)",
            ('Godfather', 1972, 175)
        )
        cursor.execute(
            "INSERT INTO movies (title, release_year, duration) VALUES (%s, %s, %s)",
            ('The Green Mile', 1999, 189)
        )
        conn.commit()

def get_all_movies(conn):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM movies")
        movies = cursor.fetchall()
        return [(movie[1], movie[2], movie[3]) for movie in movies]
# END
