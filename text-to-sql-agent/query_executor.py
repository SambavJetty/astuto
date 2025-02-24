import pandas as pd
from sqlalchemy import create_engine

# Database connection string
DATABASE_URI = "postgresql+psycopg2://postgres:SAMBAV@localhost:5432/pagila"
engine = create_engine(DATABASE_URI)

def execute_query(sql_query):
    try:
        # Execute the query and fetch results
        with engine.connect() as connection:
            result = connection.execute(sql_query)
            rows = result.fetchall()
            columns = result.keys()
            return pd.DataFrame(rows, columns=columns)
    except Exception as e:
        print(f"Error executing query: {e}")
        return None

# Example usage
sql_query = "SELECT * FROM film WHERE release_year = 2006;"  # Replace with generated query
result_df = execute_query(sql_query)
print(result_df)
