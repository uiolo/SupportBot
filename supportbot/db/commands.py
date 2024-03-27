from aiogram.types import User


def check_user_exists(user: User, connection) -> bool:
    '''returns True if user exists. False otherwise'''
    with connection.cursor() as cur:
        cur.execute('SELECT id FROM users WHERE id = (%s);', (user.id, ))
        res = cur.fetchone()
    return bool(res)


def add_user_to_db(user: User, connection):
    if check_user_exists(
        connection=connection,
        user=user
    ):
        return
    
    with connection.cursor() as cur:
        cur.execute('INSERT INTO users VALUES (%s, %s);', (user.id, user.username))
        connection.commit()
    

def delete_user_from_db(user: User, connection):
    if not check_user_exists(
        connection=connection,
        user=user
    ):
        return
    
    with connection.cursor() as cur:
        cur.execute('DELETE FROM users WHERE id = (%s);', (user.id, ))
        connection.commit()
    

def get_all_titles(connection) -> set[str]:
    with connection.cursor() as cur:
        cur.execute('SELECT * FROM titles;')
        res = {item[0] for item in cur.fetchall()}
    return res


def get_all_sizes(connection) -> set[str]:
    with connection.cursor() as cur:
        cur.execute('SELECT * FROM sizes;')
        res = {item[0] for item in cur.fetchall()}
    return res

