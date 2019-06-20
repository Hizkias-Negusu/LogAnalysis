import psycopg2

dbname = "news"

db = psycogp2.connect(database = dbname)
cursor = db.cursor()
cursor.execute("select title from (select count(time) from articles join log order by desc)")
results = cursor.fetchall()
print results
db.close()


