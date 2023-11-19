#!/usr/bin/python3
"""
    Lists all the states in the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    """
        Connects to the database and selects the list of states in the database
    """
    import MySQLdb
    import sys

    data_connector = MySQLdb.connect(host = "localhost",
                                   port = 3306,
                                   user = sys.argv[1],
                                   passwd = sys.argv[2],
                                   db = sys.argv[3])
    cursor = data_connector.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id;")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    data_connector.close()