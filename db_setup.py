import psycopg2

try:
    connection = psycopg2.connect(database="crimemap", user = "crime", password = "crime", host = "127.0.0.1", port = "5432")
except:
    print "I am unable to connect to the database"

try:
    with connection.cursor() as cursor:

        sql = """CREATE TABLE IF NOT EXISTS crimes(
            id int PRIMARY KEY NOT NULL,
            latitude Numeric(10,6),
            longitude Numeric(10,6),
            Date_when_created date,
            category VARCHAR(50),
            description VARCHAR(1000),
            updated_at TIMESTAMP)"""
        cursor.execute(sql)
    connection.commit()

finally:
    connection.close()
