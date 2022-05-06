import psycopg2
from datetime import datetime, timezone


def insert_measurement(name, location, timestamp, value, puser=-999.7, scale='C', comment=''):

    sql = """INSERT INTO measurement(name, location, timestamp, puser, value, scale, comment)
             VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING id;"""
    conn = None
    id = None
    try:

        conn = psycopg2.connect(
            host="dbmonitor.cbrj5eqdoing.us-east-1.rds.amazonaws.com",
            database="",
            user="postgres",
            password="")
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (name, location, timestamp, puser, value, scale, comment,))
        id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return id


if __name__ == '__main__':
    # insert one measurement
    dt = datetime.now(timezone.utc)
    id = insert_measurement(name="fake", location="fake_location", timestamp=dt, puser='fake_user', value='-999.7', scale='C', comment='no comment')
    print(id)