import psycopg2

from config_reader import config

try:
    connection = psycopg2.connect(
        host=config.db_host,
        user=config.db_user,
        password=config.db_password.get_secret_value(),
        database=config.db_name
    )
    
    with connection.cursor() as cur:
        cur.execute(
            'SELECT version();'
        )
        print(f'Server version: {cur.fetchone()}')

    with connection.cursor() as cur:
        cur.execute('CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY NOT NULL, username varchar(100) NOT NULL)')
        connection.commit()
        
    with connection.cursor() as cur:
        cur.execute("INSERT INTO users VALUES ('1233112331', '12331vlad')")
        cur.execute('SELECT * FROM users')
        print(cur.fetchall())

except Exception as _ex:
    print('[ERROR] POSTRGE ERROR: ', _ex)
    
finally:
    connection.close()