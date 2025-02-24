from gemini_integration import generate_sql_query
from query_executor import execute_query

def text_to_sql_agent(user_query):
    # Step 1: Generate SQL query using Gemini
    sql_query = generate_sql_query(user_query)
    print("Generated SQL Query:", sql_query)

    # Step 2: Execute the SQL query
    result_df = execute_query(sql_query)
    if result_df is not None:
        print("Query Results:")
        print(result_df)
    else:
        print("No results or an error occurred.")

# Example usage
user_query = "Find all films released in 2006."
text_to_sql_agent(user_query)