import functools
import sqlite3


def singleton(cls):
    instance = None

    @functools.wraps(cls)
    def inner(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance

    return inner


@singleton
class Database:
    conn = None

    def get_connection(path_to_db: str):
        try:
            conn = sqlite3.connect(path_to_db)
        except sqlite3.DatabaseError:
            print(f'Не удалось подключиться к БД: {path_to_db}')
        return conn


def db_table_create(conn: sqlite3.Connection, queries):
    try:
        crud_read_str = "SELECT * FROM user"
        crud_res = conn.execute(crud_read_str)

        for r in crud_res:
            print(r)
    except sqlite3.OperationalError as e:
        print(e)


def select_by_name(conn, tuple_data):
    try:
        cursor = conn.cursor()
        crud_read_str = "SELECT * FROM user WHERE name=:name;"
        crud_res = cursor.execute(crud_read_str, tuple_data)
        print(cursor.fetchall())
        for r in crud_res:
            print(r)
    except sqlite3.OperationalError as e:
        print('Такой таблицы нет:', e)
        try:
            create_sql = "CREATE TABLE user (id int, height real, name text, deleted bool, created Da);"
            conn.execute(create_sql)
        except:
            print('Таблица не создана, ошибка')


def insert_values(conn, list_of_tuples):
    try:
        cursor = conn.cursor()
        INSERT_NAMED_QUERY = "INSERT INTO user VALUES (:id, :height, :name, :deleted, :created);"
        for t in list_of_tuples:
            cursor.execute(INSERT_NAMED_QUERY, t)
            conn.commit()

    except sqlite3.Error as error:
        print('Ошибка при добавление данных: ', error)


def delete_by_name(conn, name):
    try:
        cursor = conn.cursor()
        crud_del_str = "DELETE FROM user WHERE name =:name;"
        cursor.execute(crud_del_str, {"name": name})

        print('-' * 40)
        crud_read_str = "SELECT * FROM user;"
        crud_res = conn.execute(crud_read_str)

        for r in crud_res:
            print(r)
    except conn.Error as error:
        print(error)


def update(conn, id):
    try:
        cursor = conn.cursor()
        crud_update_str = "UPDATE user SET deleted = 1 WHERE id =:id;"
        cursor.execute(crud_update_str, {"id": id})
        print(cursor.fetchall())
        conn.commit()
    except conn.Error as error:
        print(error)


connecter = Database.get_connection(path_to_db='example.db')
list_of_tuples = [{"id": 1, "height": 1.81, "name": 'user1', "deleted": 0, "created": '2022-03-02 14:03:21'},
                  {"id": 2, "height": 1.82, "name": 'user2', "deleted": 0, "created": '2022-03-02 14:03:22'},
                  {"id": 3, "height": 1.83, "name": 'user1', "deleted": 0, "created": '2022-03-02 14:03:24'},
                  {"id": 100, "height": 1.90, "name": 'Nick', "deleted": 1, "created": '2022-03-02 14:03:28'}]


insert_values(connecter, list_of_tuples)
select_by_name(connecter, {"name": "user1"})
