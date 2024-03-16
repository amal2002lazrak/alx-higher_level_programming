#!/usr/bin/python3
"""
    Connects to a MySQL database and retrieves and prints data
    from the 'states' table.

    Usage: python script.py <user> <password> <database>
"""
import MySQLdb
import sys


if __name__ == "__main__":
    mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    mycursor = mydb.cursor()
    SQLquerry = "SELECT a.id, a.name, b.name\
        FROM cities AS a \
        JOIN states AS b \
        ON a.state_id = b.id \
        ORDER BY id ASC"
    SQLquerry = "SELECT cities.name \
        FROM cities, states \
        WHERE states.name = %s \
        AND cities.state_id = states.id"
    mycursor.execute(SQLquerry, (sys.argv[4], ))
    cities = mycursor.fetchall()

    city_names = ', '.join(city[0] for city in cities)
    print(city_names)
