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
        version = cur.execute(
            'SELECT version()'
        ).fetchone()
        print(f'Server version: {version}')

except Exception as _ex:
    print('[ERROR] POSTRGE ERROR: ', _ex)
    
finally:
    connection.close()