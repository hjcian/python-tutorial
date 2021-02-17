import sqlite3


def showUsers(db):
    try:
        c = db.cursor()
        c.execute("SELECT * FROM users")
        rows = c.fetchall()
        for row in rows:
            print(row)
    except Exception as err:
        print("select error:", err)


def showUserpets(db):
    try:
        c = db.cursor()
        c.execute("SELECT * FROM user_pets")
        rows = c.fetchall()
        for row in rows:
            print(row)
    except Exception as err:
        print("select error:", err)


class Cursor:
    def __init__(self):
        pass


if __name__ == "__main__":
    db = sqlite3.connect(":memory:")
    db.isolation_level = None  # 取消 python sqlite3 autocommit 的功能，TX 才會由我們自己控制
    db.execute("pragma foreign_keys = on")  # https://www.sqlite.org/pragma.html#pragma_foreign_keys

    users = """
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE
    )
    """

    user_pets = """
    CREATE TABLE user_pets (
        name TEXT,
        type TEXT,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """
    # create tables
    try:
        c = db.cursor()  # thread1 (c1) -> db(shared memory, race condition) <- thread2 (c2)
        c.execute(users)  # multi-thread python app(db object) <- (rows) <- DB
        c.execute(user_pets)
        db.commit()
    except Exception as err:
        print("create table error:", err)

    # insert max OK
    try:
        c = db.cursor()
        c.execute("BEGIN")
        name = "max"  # user input
        # name = "max'); DROP TABLE users; ('"  # sql injection example
        # string concatenate
        # stmt = 'INSERT INTO users (name) VALUES (\'{0}\')'.format(name)
        # stmt = f"INSERT INTO users (name) VALUES ('{name}')"
        # stmt = "INSERT INTO users (name) VALUES ('" + name + "')"
        # SQL injection

        # best practice: 參數化 parameterized
        c.execute("INSERT INTO users (name) VALUES (?)", ("max",))
        db.commit()
    except Exception as err:
        print("insert OK, should not print this error:", err)
        db.rollback()

    showUsers(db)

    # insert bob and max, but max is already exists due to UNIQUE constraint
    # the bob would not insert into table due to rollback
    try:
        c = db.cursor()
        c.execute("BEGIN")
        c.execute("INSERT INTO users (name) VALUES (?)", ("bob",))
        c.execute("INSERT INTO users (name) VALUES (?)", ("max",))
        db.commit()
    except Exception as err:
        print("max is exists, should raise error:", err)
        db.rollback()

    showUsers(db)

    # insert bob then insert pet but failed with "FOREIGN KEY constraint failed"
    try:
        c = db.cursor()
        c.execute("BEGIN")
        c.execute("INSERT INTO users (name) VALUES (?)", ("bob",))
        # isnert bob 之後，users 裡只有兩筆資料，id 流水號只編到 2
        # 故下面故意插入一筆 user_id = 3 的資料會造成錯誤

        pets = [
            ("taro", "cat", 1),
            ("chuchu", "cat", 3),  # user_id=3 is not exists
            ]
        c.executemany("INSERT INTO user_pets (name, type, user_id) VALUES (?,?,?)", pets)
        db.commit()
    except Exception as err:
        print("user_id=3 is not exists, should raise error:", err)
        db.rollback()

    showUserpets(db)
    db.close()
