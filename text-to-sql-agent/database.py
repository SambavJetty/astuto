from sqlalchemy import create_engine

# Database connection string
DATABASE_URI = "postgresql+psycopg2://postgres:@localhost:5432/pagila"

# Create a database engine
engine = create_engine(DATABASE_URI)

# Test the connection
try:
    connection = engine.connect()
    print("Connected to the database successfully!")
    connection.close()
except Exception as e:
    print(f"Error connecting to the database: {e}")