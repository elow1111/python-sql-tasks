from models import Course, Lesson
import psycopg2
from psycopg2.extras import NamedTupleCursor

conn = psycopg2.connect('postgresql://postgres:t@localhost:5432/test_db')


def commit(conn):
    conn.commit()


def save_course(conn, course):
    with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        if course.id is None:
            cur.execute(
                "INSERT INTO courses (name, description) VALUES (%s, %s) RETURNING id;",
                (course.name, course.description)
            )
            course.id = cur.fetchone().id
        else:
            cur.execute(
                "UPDATE courses SET name = %s, description = %s WHERE id = %s;",
                (course.name, course.description, course.id)
            )
    return course.id


def find_course(conn, course_id):
    with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute("SELECT * FROM courses WHERE id = %s;", (course_id,))
        result = cur.fetchone()
        if result:
            return Course(
                id=result.id,
                name=result.name,
                description=result.description
                )
    return None


def get_all_courses(conn):
    courses = []
    with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute("SELECT * FROM courses;")
        for row in cur.fetchall():
            courses.append(Course(
                    id=row.id,
                    name=row.name,
                    description=row.description
                    ))
        return courses


# BEGIN (write your solution here)

# END