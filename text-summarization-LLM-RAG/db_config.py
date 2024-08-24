import time
import singlestoredb as s2
def db_connection(host, user, pwd, db, port='3306'):
    try:
        conn = s2.connect(host=host, port=port, user=user, password=pwd, database=db)
        cursor = conn.cursor()
        return conn, cursor
    except Exception as e:
        print(e)
        
def setup_table(query, host, user, pwd, db):
    try:
        conn, cursor = db_connection(host, user, pwd, db)
        start_time = time.time()
        cursor.execute(query)
        elapsed_time = (time.time() - start_time) * 1000
        print(f"Execution time for getting the question embedding: {elapsed_time:.2f} milliseconds")
        conn.commit()
    except Exception as e:
        print(e) # change to a log file later
    finally:
        conn.close()
        cursor.close()