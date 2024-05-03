"""Implement two ways of inserting data into the PhoneBook.
upload data from csv file
entering user name, phone from console"""

import psycopg2

conn = psycopg2.connect(
    host='localhost',
	database = "postgres",
	user = 'postgres',
	password = 4268,
)

cursor = conn.cursor()
conn.autocommit = True

# from CSV to TABLE
f = open("people.csv", "r")
cursor.copy_from(f, 'phonebook', sep=',')
f.close()


# insert entering user fisrt name, last name, phone number from console
firstName = str(input("First name: "))
lastName = str(input("Last name: "))
phoneNum = int(input("Phone Number: "))

postgres_insert_query = """INSERT INTO phonebook(first_name, last_name, phone_number) VALUES (%s,%s,%s)"""
record_to_insert = (firstName, lastName, phoneNum)
cursor.execute(postgres_insert_query, record_to_insert)

conn.commit()
print("[INFO] Data was inserted successfully");
conn.close()