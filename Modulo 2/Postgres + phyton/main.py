import psycopg2


connection = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="123",
    dbname="postgres",
)
print("Connected to database!")

cursor = connection.cursor()

cursor.execute("SELECT id, full_name, email, password FROM lifter_duad.users;")
print("Query executed")

results = cursor.fetchall()
print(results)

