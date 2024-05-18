import psycopg2

def connect_to_pg():
    print("starting")
    try:
        with psycopg2.connect(database = "sonarqube",
                        user = "sonarqube",
                        host= 'localhost',
                        password = "admin",
                        port = 5432) as conn:
            print("connected to postgres")
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    pass

connect_to_pg()

