import sqlite3
import functools
import logging


def deco_level(level):
    def deco(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            try:
                l = logging.getLevelName(level)
                logger = logging.getLogger(__name__)
                logger.setLevel(l)
                result: sqlite3.Cursor = func(*args, **kwargs)
                logging.error(result)
            except sqlite3.DatabaseError as error:
                logging.error(error)
        return inner
    return deco


def connect_to_db(path_to_db: str) -> sqlite3.Connection:
    conn = None
    try:
        logging.basicConfig(filename="newfile.log",
                            format='%(asctime)s %(message)s',
                            filemode='w')
        conn = sqlite3.connect(path_to_db)
        conn.set_trace_callback(logging.error)
    except sqlite3.DatabaseError as error:
        print(error)
    return conn


@deco_level('CRITICAL')
def create_table(conn):
    cursor = conn.cursor()
    create_query = "CREATE TABLE user (id int, height real, name text, deleted bool, created DATETIME)"
    result = cursor.execute(create_query)
    return result.fetchall()


@deco_level('ERROR')
def read(conn):
    cursor = conn.cursor()
    read_query = "SELECT * FROM user"
    result = cursor.execute(read_query)
    return result.fetchall()


@deco_level('WARNING')
def delete(conn):
    cursor = conn.cursor()
    delete_query = "DELETE FROM user WHERE name == 'user2'"
    result = cursor.execute(delete_query)
    conn.commit()
    return cursor.execute("SELECT * FROM user").fetchall()


@deco_level('INFO')
def update(conn):
    cursor = conn.cursor()
    update_query = "UPDATE user SET deleted = 1 WHERE id == 1"
    result = cursor.execute(update_query)
    conn.commit()
    return cursor.execute("SELECT * FROM user").fetchall()


def insert_values(conn, list_of_tuples):
    cursor = conn.cursor()
    INSERT_NAMED_QUERY = "INSERT OR IGNORE INTO user VALUES (:id, :height, :name, :deleted, :created)"
    for t in list_of_tuples:
        cursor.execute(INSERT_NAMED_QUERY, t)
        conn.commit()


list_of_tuples = [{"id": 1, "height": 1.81, "name": 'user1', "deleted": 0, "created": '2022-03-02 14:03:21'},
                  {"id": 2, "height": 1.82, "name": 'user2', "deleted": 0, "created": '2022-03-02 14:03:22'},
                  {"id": 3, "height": 1.83, "name": 'user1', "deleted": 0, "created": '2022-03-02 14:03:24'},
                  {"id": 100, "height": 1.90, "name": 'Nick', "deleted": 1, "created": '2022-03-02 14:03:28'}]

connection = connect_to_db("zhukov.db")

create_table(connection)
read(connection)
insert_values(connection, list_of_tuples)
read(connection)
update(connection)
delete(connection)



