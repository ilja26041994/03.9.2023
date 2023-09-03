# 1. Создать БД
# 2. Создать таблицу computer (id primary key, firm not null, year_prod, store_count )
# 3. Запросы: получить все данные;
# 4. Запросы: получить данные в которых есть фирма и год выпуска;
# 5. Запросы: получить данные, где указан год выпуска;
# 6 Запросы: получить таблицу с полями фирма и год выпуска, которые есть на складе.

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mosk15########",
    database="computer"
)
# insert = "INSERT INTO computer (firm, year_prod, store_count) VALUES ('ipmoskalew2', null, 98798)"
mycursor = mydb.cursor()
# mycursor.execute(insert)
select = "SELECT * FROM computer"
mycursor.execute(select)
result = mycursor.fetchall()
for i in result:
    print(i)

for i in result:
    if i[1] is not None and i[2] is not None:
        print(i)

for i in result:
    if i[2] is not None:
        print(i)

for i in result:
    if i[3] is not None:
        print(i)
mydb.commit()
mycursor.close()
mydb.close()

