import mysql.connector
from mysql.connector import Error

# Function to create a connection to the SQL server
def create_connection(host_name, user_name, user_password, db_name):
    """Create a database connection to the SQL database."""
    conn = None
    try:
        conn = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        if conn.is_connected():
            print(f"Connected to the database {db_name}")
        return conn
    except Error as e:
        print(f"Error: '{e}'")
        return None

# Function to execute any SQL query and fetch results if necessary
def execute_query(conn, query, params=None):
    """Execute a SQL query. Fetch and return results if it's a SELECT query."""
    cursor = conn.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        
        if query.strip().lower().startswith('select'):
            # Fetch all results for SELECT queries
            result = cursor.fetchall()
            return result
        else:
            conn.commit()
            print("Query executed successfully.")
    except Error as e:
        print(f"Error: '{e}'")
        return None

def get_tables_and_columns(conn, db_name):
    """Get all tables and their columns from the database in the desired format."""
    query_tables = f"""
    SELECT table_name 
    FROM information_schema.tables 
    WHERE table_schema = '{db_name}';
    """
    tables = execute_query(conn, query_tables)
    
    if tables:
        tables_and_columns = {}
        for (table,) in tables:
            query_columns = f"""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_schema = '{db_name}' 
            AND table_name = '{table}';
            """
            columns = execute_query(conn, query_columns)
            tables_and_columns[table] = [column[0] for column in columns]
        return tables_and_columns
    return None


# Example usage of the functions
def main():
    # Database connection details
    host = "localhost"
    user = "root"
    password = ""
    database = "schoola"

    # Create a connection to the database
    conn = create_connection(host, user, password, database)

    if conn:
        # Example query: Select data from student table
        select_query = "SELECT * FROM student"
        result = execute_query(conn, select_query)
        if result:
            for row in result:
                print(row)

        # Close the connection
        conn.close()

if __name__ == '__main__':
    main()
