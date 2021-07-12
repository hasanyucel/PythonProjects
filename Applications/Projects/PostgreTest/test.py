import psycopg2

db = psycopg2.connect(user = "postgres",
                      password = "1234",
                      host = "localhost",
                      port = "5432",
                      database = "test")

imlec = db.cursor()

komut_SELECT = "SELECT * FROM isimler;"
imlec.execute(komut_SELECT)

liste = imlec.fetchall()
for i in liste:
    print(i)