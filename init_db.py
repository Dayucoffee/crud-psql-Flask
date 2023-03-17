import psycopg2

conn = psycopg2.connect(database="flask_db",
						user="dayu",
						password="",
						host="localhost", port="5433")

cur = conn.cursor()

conn.commit()

cur.close()
conn.close()

