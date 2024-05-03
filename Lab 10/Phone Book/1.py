# Design tables for PhoneBook.

import psycopg2

try:
    # connect to exist database
    connection = psycopg2.connect(
        host = 'localhost',
        user =  'postgres',
        database = 'postgres',
        password = '4268'
    )

    connection.autocommit = True

    # create a new table
    with connection.cursor() as cursor:
        cursor.execute(
            '''CREATE TABLE PhoneBook (
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            phone_number VARCHAR(11)
            )'''
        )
        print("[INFO] Table created succefully")
    
    # insert data into a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         '''INSERT INTO PhoneBook (first_name, last_name, phone_number) VALUES
    #         ('Azamat', 'Narikbay', ''87479004773')
    #         '''
    #     )
    #     print("[INFO] Data was succefully inserted")

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         '''SELECT first_name FROM PhoneBook WHERE first_name='Azamat';'''
    #     )

    #     print(cursor.fetchall())

    # delete a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         '''DROP TABLE PhoneBook'''
    #     )

    #     print("[INFO] Table was deleted")
    


except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")