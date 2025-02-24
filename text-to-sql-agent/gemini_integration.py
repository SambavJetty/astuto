import google.generativeai as genai

# Set up Gemini API key
genai.configure(api_key="AIzaSyADk0R4_VFW9Qt0pq4XOh9GoOgbReI_ufM")

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-pro')

def generate_sql_query(prompt):
    # Provide a system message to guide the model
    system_message = """
    You are a SQL expert. Given a natural language query, generate a SQL query for the Pagila database.
    The database schema includes tables like film, actor, customer, rental, staff, payment, inventory, country, city, address, customer, dummy_category, language, film_actor, film_category, store.
    Always use proper table and column names.
    """

    # Combine the system message and user prompt
    full_prompt = f"{system_message}\n\nUser Query: {prompt}\nSQL Query:"

    # Generate SQL query using Gemini
    response = model.generate_content(full_prompt)
    return response.text

# Example usage
user_query = "Find all films released in 2006."
sql_query = generate_sql_query(user_query)
print("Generated SQL Query:", sql_query)