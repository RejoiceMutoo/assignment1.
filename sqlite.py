import sqlite3
from sqlite3 import Error


def main():
    # 1. Connect to the SQLite database (or create it if it doesn't exist)
    database_name = "example.db"
    conn = None

    try:
        conn = sqlite3.connect(database_name)
        print(f"Successfully connected to database: {database_name}")

        # Create a cursor object to execute SQL statements
        cursor = conn.cursor()

        # 2. Create a table
        # We use 'IF NOT EXISTS' so the script doesn't crash if run multiple times
        create_table_query = """
                             CREATE TABLE IF NOT EXISTS users \
                             ( \
                                 id \
                                 INTEGER \
                                 PRIMARY \
                                 KEY \
                                 AUTOINCREMENT, \
                                 name \
                                 TEXT \
                                 NOT \
                                 NULL, \
                                 email \
                                 TEXT \
                                 UNIQUE \
                                 NOT \
                                 NULL, \
                                 age \
                                 INTEGER
                             ); \
                             """
        cursor.execute(create_table_query)
        print("Table 'users' created successfully.")

        # 3. Insert some data
        # We use parameterized queries (?) to safely insert variables and prevent SQL injection
        insert_query = "INSERT INTO users (name, email, age) VALUES (?, ?, ?);"

        # Insert a single record
        cursor.execute(insert_query, ("Alice Smith", "alice@example.com", 30))

        # Insert multiple records at once using executemany
        extra_users = [
            ("Bob Jones", "bob@example.com", 25),
            ("Charlie Brown", "charlie@example.com", 35)
        ]
        cursor.executemany(insert_query, extra_users)

        # Save (commit) the changes to the database
        conn.commit()
        print("Data inserted and committed successfully.")

        # 4. Retrieve and display the data
        select_query = "SELECT id, name, email, age FROM users;"
        cursor.execute(select_query)

        # Fetch all rows from the result of the query
        rows = cursor.fetchall()

        print("\n--- Retrieved Data ---")
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Email: {row[2]} | Age: {row[3]}")

    except Error as e:
        print(f"An error occurred: {e}")

    finally:
        # 5. Always close the connection when finished
        if conn:
            conn.close()
            print("\nDatabase connection closed.")


if __name__ == "__main__":
    main()
