#!/usr/bin/python3
"""
    Lists all the states in the database
    that start with the letter N hbtn_0e_0_usa
"""

if __name__ == "__main__":
    """
        Connects to the database and selects the list of states in the database
    """
    import MySQLdb
    import sys

    data_connector = MySQLdb.connect(host="localhost",
                                     port=3306,
                                     user=sys.argv[1],
                                     passwd=sys.argv[2],
                                     db=sys.argv[3])
    cursor = data_connector.cursor()
    cursor.execute(f"SELECT cities.name FROM cities JOIN states ON \
        cities.state_id = states.id WHERE states.name LIKE BINARY \
            '{sys.argv[4]}' ORDER BY cities.id;")
    listed = []
    for row in cursor.fetchall():
        listed.append(row[0])
    print(", ".join(listed))
    cursor.close()
    data_connector.close()
